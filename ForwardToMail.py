import smtplib
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# Setările serverului SMTP
smtp_server = 'smtp.mail.yahoo.com'
smtp_port = 587
username = 'sebastian.stefan0@yahoo.com'
password = 'ufsi rwtp daua njud'

# Destinatar și expeditor
to_address = 'sebastian.stefan0@yahoo.com'
from_address = 'sebastian.stefan0@yahoo.com'

# Subiect și conținutul email-ului
subject = 'Prezență la cursul de astăzi'
message = 'Acesta este conținutul email-ului.'

# Calea către fișierul atașat
attachment_path = 'prezenta.txt'

# Construirea obiectului MIMEMultipart
msg = MIMEMultipart()
msg['To'] = email.utils.formataddr(('Profesor', to_address))
msg['From'] = email.utils.formataddr(('FaceRecognitionApp', from_address))
msg['Subject'] = subject

# Adăugarea conținutului text
msg.attach(MIMEText(message, 'plain'))

# Adăugarea fișierului atașat
with open('prezenta.txt', 'rb') as file:
    attachment = MIMEApplication(file.read(), _subtype='txt')
    attachment.add_header('Content-Disposition', 'attachment', filename=attachment_path)
    msg.attach(attachment)

# Trimiterea email-ului prin serverul SMTP
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(username, password)
    server.sendmail(from_address, to_address, msg.as_string())
    server.quit()
    print('Email trimis cu succes!')
    a = "Prezența trimisă pe email la adresa de logare"
    print(a)
except Exception as e:
    print('A apărut o eroare la trimiterea email-ului:', str(e))
