from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText
import os


class CoffeePage:
    def __init__(self):
        self.app = Flask(__name__)
        self.email_sender = EmailSender()   # no args needed anymore
        self.setup_routes()
        
    def setup_routes(self):
        self.app.add_url_rule('/', 'home', self.home)
        self.app.add_url_rule('/contact', 'contact', self.contact, methods=['GET', 'POST'])
    
    def home(self):
        return render_template('index.html')
    
    def contact(self):
        if request.method == 'POST':
            name = request.form.get('name')
            email = request.form.get('email')
            phone = request.form.get('phone')
            message = request.form.get('message')

            self.email_sender.send(name, email, phone, message)

            print(f"Name: {name} email: {email} phone: {phone} message: {message}")
            return '', 200

        return 'Method not allowed', 405


class EmailSender:
    def __init__(self):
        # Read all values from Render environment variables
        self.host = os.getenv("MAIL_HOST")
        self.port = int(os.getenv("MAIL_PORT"))
        self.username = os.getenv("MAIL_USERNAME")
        self.password = os.getenv("MAIL_PASSWORD")
        self.to_email = os.getenv("MAIL_TO")

    def send(self, name, email, phone, message):
        body = f"""
        You received a new contact form submission:

        Name: {name}
        Email: {email}
        Phone: {phone}

        Message:
        {message}
        """
        
        msg = MIMEText(body)
        msg['Subject'] = f"New Message from {name}"
        msg['From'] = self.username
        msg['To'] = self.to_email
        msg['Reply-To'] = email

        with smtplib.SMTP(self.host, self.port) as server:
            server.starttls()
            server.login(self.username, self.password)
            server.send_message(msg)

        print("Email Sent")


# Expose Flask app to Render
coffee = CoffeePage()
app = coffee.app

# Do NOT run app.run() in production
