from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText
import os


class CoffeePage:
    def __init__(self):
        self.app = Flask(__name__)
        self.email_sender = EmailSender(os.getenv("EMAIL_ADDRESS"), os.getenv("PASSWORD"))
        self.setup_routes()
        
    
    def setup_routes(self):
        self.app.add_url_rule('/', 'home', self.home)
        self.app.add_url_rule('/contact','contact', self.contact ,methods=['GET', 'POST'])
    
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
    
    def run(self):
        self.app.run(debug=True)


class EmailSender:
    def __init__(self, email_sender, sender_password):
        self.email_sender = email_sender
        self.sender_password = sender_password

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
        msg['From'] = self.email_sender
        msg['To'] = self.email_sender
        msg['Reply-To'] = email

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.set_debuglevel(1)
            server.starttls()
            server.login(self.email_sender, self.sender_password)
            server.send_message(msg)
        
        print("Email Sent")
    
coffee = CoffeePage()      # create CoffeePage object
app = coffee.app           # expose Flask app as "app"

if __name__ == "__main__":
    app.run()
