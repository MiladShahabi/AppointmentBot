import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailService:
    def __init__(self) -> None:
        pass

    def send_email(self, sender_email, sender_password, receiver_email, subject=None):
        msg = f'subject:{subject}\n\n This is body of mey email '
        smtp = 'smtp.gmail.com'
        smtp_port = 587
        session = smtplib.SMTP(smtp, smtp_port)
        session.starttls()
        session.login(sender_email, sender_password)
        session.sendmail(
            from_addr=sender_email,
            to_addrs=receiver_email,
            msg=msg

        )

    def advanced_send_mail(self, sender_email, sender_password, receiver_email, subject):
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = subject

        website = 'youtube.com'
        mail_content = f'''3
        
        this is the email body \n

        please make sure you check other videos\n

        website : {website}\n
        
        With Regards \n
        Me myself \n\n
        '''

        message.attach(MIMEText(mail_content, 'plain'))
        smtp = 'smtp.gmail.com'
        smtp_port = 587
        session = smtplib.SMTP(smtp, smtp_port)
        session.starttls()
        session.login(sender_email, sender_password)
        session.sendmail(
            from_addr=sender_email,
            to_addrs=receiver_email,
            msg=message.as_string()

        )


def main() -> None:
    email = EmailService()

    try:
        email.advanced_send_mail(
            sender_email='milad.shahabifard.20@gmail.com',
            sender_password='pphfyglrpruzvpkg',
            receiver_email='milad.shahabi.20@gmail.com',
            subject='Your appointment has been booked'
        )
        print("Email Sent Successfully")
    except Exception as e:
        print(f"Email sending failed with error {e}")


if __name__ == '__main__':
    main()
