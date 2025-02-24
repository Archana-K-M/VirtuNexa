import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# SMTP Configuration
SMTP_SERVER = "smtp.gmail.com" #smtp server email
SMTP_PORT = 587
EMAIL_SENDER = "23d106@psgitech.ac.in"
EMAIL_PASSWORD = "agEklB67Woph2WcV"  # Use an App Password for security

# Email Subject and Attachment
EMAIL_SUBJECT = "Personalized Email with Attachment"
ATTACHMENT_PATH = "E:\K M Archana\Project\VirtuNexa\Week2\VNJournal.pdf" 

# Read recipient details from CSV
csv_file = "recipients.csv" 
df = pd.read_csv(csv_file)

def send_email(to_email, name):
    try:
        # Message container
        msg = MIMEMultipart()
        msg["From"] = EMAIL_SENDER
        msg["To"] = to_email
        msg["Subject"] = EMAIL_SUBJECT

        # Email body (personalized)
        body = f"Hello {name},\n\nThis is an automated email with an attachment.\n\nBest regards,\nArchana K M"
        msg.attach(MIMEText(body, "plain"))

        # Attach file
        with open(ATTACHMENT_PATH, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename={ATTACHMENT_PATH.split('/')[-1]}")
        msg.attach(part)

        # Send email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, to_email, msg.as_string())
        server.quit()
        
        print(f"Email sent to {name} ({to_email})")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

# Loop through CSV and send emails
for _, row in df.iterrows():
    send_email(row["email"], row["name"])
