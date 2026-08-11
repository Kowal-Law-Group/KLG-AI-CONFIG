#!/usr/bin/env python3
"""
generate_conflict_waiver.py

Takes a JSON config file and the unpacked letterhead directory,
replaces the document body with a conflict waiver letter while
preserving the original XML shell (namespaces, sectPr, etc.).

Usage:
    python generate_conflict_waiver.py config.json unpacked_dir/ output.docx original_template.docx
"""

import json
import sys
import os
import subprocess


def xml_escape(text):
    """Escape text for XML."""
    text = text.replace("&", "&amp;")
    text = text.replace("<", "&lt;")
    text = text.replace(">", "&gt;")
    text = text.replace('"', "&quot;")
    # Smart apostrophes
    text = text.replace("'", "\u2019")
    return text


def wt(text):
    """Create a <w:t> element string."""
    escaped = xml_escape(text)
    if text and (text[0] == ' ' or text[-1] == ' '):
        return f'<w:t xml:space="preserve">{escaped}</w:t>'
    return f'<w:t>{escaped}</w:t>'


def wr(text, bold=False, italic=False):
    """Create a <w:r> element string with optional formatting."""
    parts = ['<w:r>']
    if bold or italic:
        parts.append('<w:rPr>')
        if bold:
            parts.append('<w:b/><w:bCs/>')
        if italic:
            parts.append('<w:i/><w:iCs/>')
        parts.append('</w:rPr>')
    parts.append(wt(text))
    parts.append('</w:r>')
    return ''.join(parts)


def wp(style, content='', indent_left=None):
    """Create a <w:p> element string."""
    parts = ['<w:p><w:pPr>']
    parts.append(f'<w:pStyle w:val="{style}"/>')
    if indent_left:
        parts.append(f'<w:ind w:left="{indent_left}"/>')
    parts.append('</w:pPr>')
    parts.append(content)
    parts.append('</w:p>')
    return ''.join(parts)


def wp_right(content='', size='26'):
    """Create a right-aligned paragraph with size."""
    return (f'<w:p><w:pPr>'
            f'<w:spacing w:after="0"/>'
            f'<w:jc w:val="right"/>'
            f'<w:rPr><w:sz w:val="{size}"/><w:szCs w:val="{size}"/></w:rPr>'
            f'</w:pPr>{content}</w:p>')


def sized_run(text, size='26'):
    """Create a run with explicit size."""
    return (f'<w:r><w:rPr><w:sz w:val="{size}"/>'
            f'<w:szCs w:val="{size}"/></w:rPr>{wt(text)}</w:r>')


def build_addressee_paras(client):
    """Build Addressees-style paragraphs for one client."""
    lines = [client['name']]
    if client.get('care_of'):
        lines.append("c/o " + client['care_of'])
    for addr in client.get('address', []):
        lines.append(addr)
    if client.get('email'):
        lines.append(client['email'])
    return ''.join(wp('Addressees', wr(line)) for line in lines)


def build_subject_runs(config):
    """Build the subject line runs (after Re: tab)."""
    caption = config['case_caption']
    court = config['court']
    case_no = config['case_number']
    appeal_no = config.get('appellate_case_number', '')
    fmt = config.get('subject_format', 'appellate')

    parts = []
    if fmt == 'trial':
        parts.append(wr('Informed Consent of and Waiver of Potential Conflicts of Interest in '))

    # Italic case caption
    parts.append(wr(caption, italic=True))

    # Court and case number
    if appeal_no:
        suffix = f", {court} case no.\u00a0{case_no}, Court of Appeal case no. {appeal_no}"
    else:
        suffix = f", {court} case no.\u00a0{case_no}"
    parts.append(wr(suffix))

    return ''.join(parts)


def build_body(config):
    """Build all body paragraphs as XML string."""
    clients = config['clients']
    matter_type = config.get('matter_type', 'lawsuit')
    case_specific = config.get('case_specific_scenarios', '')

    client_names = [c['name'] for c in clients]
    if len(client_names) == 2:
        names_str = f"both {client_names[0]} and {client_names[1]}"
    elif len(client_names) == 1:
        names_str = client_names[0]
    else:
        names_str = ", ".join(client_names[:-1]) + ", and " + client_names[-1]

    paras = []

    # Opening paragraph
    opening = (
        f"You have requested that our law firm, Kowal Law Group, APC, "
        f"represent {names_str}, in the "
        f"{matter_type} mentioned above. Whenever an attorney has more than "
        f"one client in the same {matter_type}, there is a potential for "
        f"conflicts. After discussing the case with you, it appears there are "
        f"no conflicts now. But things may change, and parties may wish to "
        f"pursue different strategies or objectives in the case. These and "
        f"other things may create a potential for a future conflict."
    )
    paras.append(wp('BodyText', wr(opening)))

    # Professional conduct paragraph
    prof = (
        "The California Rules of Professional Conduct requires that I obtain "
        "your informed consent, in writing, that you are aware of the potential "
        "of future conflicts, and the consequences. In other words, while "
        "sharing an attorney holds out certain advantages to parties whose "
        "interests appear to be aligned, there may be reasons why it could be "
        "a bad idea. So I need to disclose to you the ways in which it might "
        "be a bad idea so you can consider them independently."
    )
    paras.append(wp('BodyText', wr(prof)))

    # First disclosure
    first_text = (
        "you need to be aware that when two parties are jointly "
        "represented by the same attorney there is no client "
        "confidentiality between them. (Evid. Code, \u00a7\u00a0962.) "
        "That means that whatever the attorney learns about one client "
        "may be required to be disclosed to the other client."
    )
    paras.append(wp('BodyText', wr("First, ", bold=True) + wr(first_text)))

    # Second disclosure
    second_text = (
        "a common way that conflicts arise in these situations is when "
        "selecting litigation and settlement strategies. These strategies "
        "can impact different parties differently, and the parties may have "
        "different ideas about them. "
    )
    if case_specific:
        second_text += case_specific + " "
    second_text += (
        "At this time, I am not aware of any information indicating there "
        "would be a conflict between your respective interests. But if such "
        "information surfaces suggesting a conflict concerning a settlement "
        "or litigation strategy, there may be a need for you to consult "
        "independent counsel."
    )
    paras.append(wp('BodyText', wr("Second, ", bold=True) + wr(second_text)))

    # Third disclosure (with Flatt citation)
    third_text = (
        "you should be aware of what happens in the future if your interests "
        "do become adverse. The most immediate consequence of a conflict "
        "arising is that one or both of the clients may need to obtain new "
        "counsel. A more serious problem could occur if a lawsuit were to "
        "arise between the two clients. While we all hope that would never "
        "happen, if it did, the attorney (me) might have to testify about "
        "communications I had with one of you while I jointly represented "
        "you both. This kind of uncomfortable possibility would present a "
        "problem for me as the attorney because of the duty of loyalty I "
        "would owe to each client. This duty prevents joint representation "
        "without informed written consent even if the adversity is unrelated "
        "to the representation. ("
    )
    third_content = (
        wr("Third, ", bold=True) +
        wr(third_text) +
        wr("Flatt v. Superior Court", italic=True) +
        wr(" (1994) 9 Cal.4th 275, 284.)")
    )
    paras.append(wp('BodyText', third_content))

    # Fourth disclosure
    fourth_text = (
        "issues could arise regarding the custody of the original file. "
        "Our firm policy is not to maintain custody of the originals. You "
        "are encouraged to come to an agreement about which one of you "
        "will maintain any original documents that relate to this case. "
        "By signing this agreement, each of you agree that if our firm "
        "stops representing one of you, but continues to represent the "
        "other, the client we continue to represent will be entitled to "
        "maintain custody or control of the original file. The other "
        "party is entitled to a copy of Client Papers as defined in "
        "Rule 3-700(D) of the Rules of Professional Conduct."
    )
    paras.append(wp('BodyText', wr("Fourth, ", bold=True) + wr(fourth_text)))

    # Fifth disclosure
    fifth_text = (
        "in the event of a dispute or conflict between any of the "
        "clients, there is a risk that the attorney may be disqualified "
        "from representing one or more of the clients or that it may "
        "otherwise be inappropriate for the attorney to continue with "
        "the joint representation absent written consent from each of "
        "the clients."
    )
    paras.append(wp('BodyText', wr("Fifth, ", bold=True) + wr(fifth_text)))

    # Sixth disclosure
    sixth_text = (
        "if there is insufficient insurance or assets to cover the "
        "damages of each client, there may be disputes regarding how to "
        "allocate the insurance proceeds or assets between the clients."
    )
    paras.append(wp('BodyText', wr("Sixth, ", bold=True) + wr(sixth_text)))

    # Consent introduction
    consent = (
        "Given there is currently no conflict of interest, we may jointly "
        "represent the clients in this matter, provided that the clients "
        "give informed consent in writing. Each client should feel free to "
        "consult with independent counsel before finalizing the client\u2019s "
        "decision to proceed with the joint representation, including "
        "whether to sign this conflict disclosure and waiver. As the "
        "attorney, I need to emphasize that each client remains free to "
        "seek independent counsel at any time even if the client decides to "
        "sign this consent."
    )
    paras.append(wp('BodyText', wr(consent)))

    # Waiver transition
    paras.append(wp('BodyTextContinued', wr(
        "With those disclosures having been made, please carefully consider "
        "consenting to the following waiver:"
    )))

    # Waiver text (indented)
    INDENT = 720
    waiver_intro = (
        "The attorney\u2019s current understanding is that each client "
        "desires to have the attorney jointly represent them in connection "
        "with the matter referenced above. By signing this Disclosure and "
        "Consent, each client expressly acknowledges that the client:"
    )
    paras.append(wp('BodyTextContinued', wr(waiver_intro), indent_left=INDENT))

    waiver_items = [
        "(1) has carefully read and fully understands the disclosures described above;",
        "(2) has carefully considered all of the circumstances and potential conflicts described above;",
        "(3) has had the opportunity to consult with independent counsel regarding the disclosures and consent in this agreement; and",
        "(4) agrees to the joint representation of the clients by the attorney in connection with the referenced matter.",
    ]
    for item in waiver_items:
        paras.append(wp('BodyTextContinued', wr(item), indent_left=INDENT))

    # Signature blocks
    for client in clients:
        paras.append(wp('BodyTextContinued', wr("Client Name: " + client['name'])))
        paras.append(wp('BodyTextContinued'))
        sig_line = "Signed: " + "_" * 34 + " Date:" + "_" * 19
        paras.append(wp('BodyTextContinued', wr(sig_line)))
        if client.get('title'):
            paras.append(wp('BodyTextContinued', wr("         " + client['title'])))
        paras.append(wp('BodyTextContinued'))

    # Closing
    paras.append(wp('BodyTextContinued', wr("Very truly yours,")))
    paras.append(wp('BodyTextContinued'))
    paras.append(wp('BodyTextContinued'))
    paras.append(wp('BodyTextContinued', wr("Timothy M. Kowal")))

    return '\n'.join(paras)


def generate_document_body(config):
    """Generate the full <w:body> inner content (before sectPr)."""
    clients = config['clients']
    primary_idx = config.get('primary_addressee_index', 0)
    primary_client = clients[primary_idx]
    sal_name = config.get('salutation_name', primary_client['name'].split()[0])
    date_str = config['date']
    delivery = config.get('delivery_method', 'Via Email')

    parts = []

    # 1. Empty first paragraph (spacing above sender)
    parts.append(wp_right())

    # 2. Sender with bookmark
    sender_content = (
        '<w:bookmarkStart w:id="0" w:name="Sender"/>'
        + sized_run("Timothy M. Kowal") +
        '<w:bookmarkEnd w:id="0"/>'
        + sized_run(", Esq.")
    )
    parts.append(wp_right(sender_content))

    # 3. Email
    parts.append(wp_right(sized_run("Tim@KowalLawGroup.com")))

    # 4. Date with bookmark
    parts.append(
        '<w:bookmarkStart w:id="1" w:name="Date"/>'
        + wp('BodyTextContinued', '<w:r>' + wt(date_str) + '</w:r>'
              + '<w:bookmarkEnd w:id="1"/>')
    )

    # 5. Delivery method (bold)
    parts.append(wp('BodyTextContinued',
        '<w:r><w:rPr><w:b/><w:bCs/></w:rPr>' + wt(delivery) + '</w:r>'))

    # 6. Addressee table
    left_paras = build_addressee_paras(primary_client)
    other_clients = [c for i, c in enumerate(clients) if i != primary_idx]
    if other_clients:
        right_parts = []
        for oc in other_clients:
            right_parts.append(wp('Addressees', wr(oc['name'])))
            if oc.get('signing_person') and oc.get('title'):
                right_parts.append(wp('Addressees',
                    wr(oc['signing_person'] + ", " + oc['title'])))
            if oc.get('email'):
                right_parts.append(wp('Addressees', wr(oc['email'])))
        right_paras = ''.join(right_parts)
    else:
        right_paras = wp('Addressees')

    table = (
        '<w:tbl>'
        '<w:tblPr><w:tblW w:w="0" w:type="auto"/>'
        '<w:tblLook w:val="04A0" w:firstRow="1" w:lastRow="0" '
        'w:firstColumn="1" w:lastColumn="0" w:noHBand="0" w:noVBand="1"/>'
        '</w:tblPr>'
        '<w:tblGrid><w:gridCol w:w="4608"/><w:gridCol w:w="4608"/></w:tblGrid>'
        '<w:tr><w:trPr><w:trHeight w:val="899"/></w:trPr>'
        '<w:tc><w:tcPr><w:tcW w:w="4608" w:type="dxa"/>'
        '<w:shd w:val="clear" w:color="auto" w:fill="auto"/></w:tcPr>'
        '<w:bookmarkStart w:id="2" w:name="Name"/>'
        + left_paras +
        '<w:bookmarkEnd w:id="2"/>'
        '</w:tc>'
        '<w:tc><w:tcPr><w:tcW w:w="4608" w:type="dxa"/>'
        '<w:shd w:val="clear" w:color="auto" w:fill="auto"/></w:tcPr>'
        + right_paras +
        '</w:tc>'
        '</w:tr></w:tbl>'
    )
    parts.append(table)

    # 7. Subject line with Subject bookmark
    subj_runs = build_subject_runs(config)
    subj_para = (
        '<w:p><w:pPr><w:pStyle w:val="Subject"/></w:pPr>'
        + wr("Re:") +
        '<w:r><w:tab/></w:r>'
        '<w:bookmarkStart w:id="3" w:name="Subject"/>'
        + subj_runs +
        '<w:bookmarkEnd w:id="3"/>'
        '</w:p>'
    )
    parts.append(subj_para)

    # 8. Salutation
    parts.append(wp('BodyTextContinued', wr(f"Dear {sal_name}:")))

    # 9. Body paragraphs
    parts.append(build_body(config))

    return '\n'.join(parts)


def main():
    if len(sys.argv) < 5:
        print("Usage: python generate_conflict_waiver.py config.json unpacked_dir/ output.docx original.docx")
        sys.exit(1)

    config_path = sys.argv[1]
    unpacked_dir = sys.argv[2]
    output_path = sys.argv[3]
    original_path = sys.argv[4]

    with open(config_path, 'r') as f:
        config = json.load(f)

    doc_path = os.path.join(unpacked_dir, 'word', 'document.xml')

    # Read original XML (preserves declaration and all namespace attrs)
    with open(doc_path, 'r', encoding='utf-8') as f:
        xml_content = f.read()

    # Find body boundaries
    body_start_tag_end = xml_content.index('<w:body>') + len('<w:body>')
    body_close_start = xml_content.index('</w:body>')

    # Extract sectPr (must be preserved as last child of body)
    sect_start = xml_content.rindex('<w:sectPr', 0, body_close_start)
    sect_end = xml_content.index('</w:sectPr>', sect_start) + len('</w:sectPr>')
    sect_pr = xml_content[sect_start:sect_end]

    # Generate new body content
    print("Generating conflict waiver letter...")
    new_body_content = generate_document_body(config)

    # Rebuild the document: original shell + new body + original sectPr
    new_xml = (
        xml_content[:body_start_tag_end] + '\n' +
        new_body_content + '\n' +
        sect_pr + '\n' +
        xml_content[body_close_start:]
    )

    with open(doc_path, 'w', encoding='utf-8') as f:
        f.write(new_xml)
    print("Document XML updated.")

    # Clean up pre-existing template issues
    # 1. Fix broken attached template reference
    settings_rels = os.path.join(unpacked_dir, 'word', '_rels', 'settings.xml.rels')
    if os.path.exists(settings_rels):
        with open(settings_rels, 'r') as f:
            sr = f.read()
        if 'TVA' in sr or 'file:///' in sr:
            # Remove the broken external template reference
            import re as _re
            sr = _re.sub(r'<Relationship[^>]*TargetMode="External"[^>]*/>', '', sr)
            with open(settings_rels, 'w') as f:
                f.write(sr)
            # Also remove the attachedTemplate element from settings.xml
            settings_xml = os.path.join(unpacked_dir, 'word', 'settings.xml')
            if os.path.exists(settings_xml):
                with open(settings_xml, 'r') as f:
                    sx = f.read()
                sx = _re.sub(r'<w:attachedTemplate[^/]*/>', '', sx)
                with open(settings_xml, 'w') as f:
                    f.write(sx)
            print("Cleaned broken template reference.")

    # 2. Remove [trash] directory
    trash_dir = os.path.join(unpacked_dir, '[trash]')
    if os.path.isdir(trash_dir):
        import shutil
        shutil.rmtree(trash_dir)
        print("Removed [trash] directory.")

    # Pack
    pack_script = "/mnt/skills/public/docx/scripts/office/pack.py"
    print("Packing document...")
    result = subprocess.run(
        ["python", pack_script, unpacked_dir, output_path, "--original", original_path],
        capture_output=True, text=True
    )
    if result.stdout:
        print(result.stdout)
    if result.returncode != 0:
        print(f"Pack issue (trying without validation): {result.stderr}")
        result2 = subprocess.run(
            ["python", pack_script, unpacked_dir, output_path,
             "--original", original_path, "--validate", "false"],
            capture_output=True, text=True
        )
        if result2.stdout:
            print(result2.stdout)
        if result2.returncode != 0:
            print(f"Pack failed: {result2.stderr}")
            sys.exit(1)

    # Fix standalone
    fix_script = "/mnt/skills/user/klg-shared-scripts/fix_docx_standalone.py"
    if os.path.exists(fix_script):
        print("Fixing standalone attribute...")
        subprocess.run(["python", fix_script, output_path], capture_output=True)

    print(f"Done. Output: {output_path}")


if __name__ == '__main__':
    main()
