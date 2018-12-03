
import imaplib
import email
import os

user = 'yahir@mail.redes.com'
password = ''
imap_url = 'mail.redes.com'

# Where you want your attachments to be saved (ensure this directory exists)
attachment_dir = '/var/mail/yahir'


def auth(us, psw, url):
    conn = imaplib.IMAP4_SSL(url)
    conn.login(us, psw)
    return conn


def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None, True)
# allows you to download attachments


def get_attachments(msg):
    for part in msg.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue
        file_name = part.get_filename()

        if bool(file_name):
            file_path = os.path.join(attachment_dir, file_name)
            with open(file_path, 'wb') as f:
                f.write(part.get_payload(decode=True))


# search for a particular email
def search(key, value, conn):
    res, d = conn.search(None, key, '"{}"'.format(value))
    return d


# extracts emails from byte array
def get_emails(result_bytes):
    msgs = []
    for num in result_bytes[0].split():
        typ, d = con.fetch(num, '(RFC822)')
        msgs.append(d)
    return msgs


con = auth(user, password, imap_url)
con.select('INBOX')

result, data = con.fetch(b'10', '(RFC822)')
raw = email.message_from_bytes(data[0][1])
get_attachments(raw)
