import mailbox
import os
from dateutil.parser import parse
from email.header import decode_header
import re

def extract_attachments_from_mbox(mbox_file, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    def clean_filename(filename):
        return re.sub(r'[\\/*?:"<>|/\r\n]+', '_', filename)

    mbox = mailbox.mbox(mbox_file)

    for msg in mbox:
        date_str = msg['date']
        date_dt = parse(date_str)
        date_formatted = date_dt.strftime('%Y-%m-%d')   
        
        subject = msg['subject']
        decoded_subject, encoding = decode_header(subject)[0]
        if isinstance(decoded_subject, bytes):
            subject = decoded_subject.decode(encoding or 'utf-8')

        subject = subject.replace(' ', '_').replace('/', '_').replace('\\', '_').replace(':', '_')

        for part in msg.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue

            filename_header = part.get_filename()
            if filename_header:
                decoded_filename, encoding = decode_header(filename_header)[0]
                if isinstance(decoded_filename, bytes):
                    filename = decoded_filename.decode(encoding or 'utf-8')
                else:
                    filename = decoded_filename
                
                filename = clean_filename(os.path.basename(filename))
                
                output_path = os.path.join(output_folder, f"{date_formatted}_{filename}")
                
                payload = part.get_payload(decode=True)
                if payload is not None:
                    with open(output_path, 'wb') as f:
                        f.write(payload)
                    print(f"Attachment saved: {output_path}")

mbox_file = '<mbox file path>'
output_folder = '<output_folder_path>'
extract_attachments_from_mbox(mbox_file, output_folder)
