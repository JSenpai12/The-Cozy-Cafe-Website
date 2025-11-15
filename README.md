# ☕ Cozy Café — Landing Page

A simple and cozy landing page for a fictional café. Built with HTML, CSS, and JavaScript (or Flask if you used Flask). The site includes **Home**, **About Us**, and **Contact** sections, designed with a warm aesthetic.

---

## 🌟 Features

* 🏠 **Home Section** — Hero image + welcoming café introduction
* 📖 **About Us** — Short description of the café’s story and vibe
* ✉️ **Contact Form** — Users can message the café (optional backend)
* 📱 **Responsive Design** — Works on desktop, tablet, and mobile
* 🎨 **Warm, cozy theme** using soft colors and elegant typography

---

## 🔐 Email Setup (Gmail)

If you want the contact form to send emails, you must configure Gmail properly.

### **1. Enable 2-Step Verification**

1. Go to your Google Account.
2. Open **Security** → **2-Step Verification**.
3. Turn it on.

### **2. Create an App Password**

1. After enabling 2-Step Verification, go to **Security** → **App Passwords**.
2. Choose **Mail** as the app.
3. Choose your device (or select “Other”).
4. Google will generate a **16-character App Password**.
5. Copy it — this will replace your normal Gmail password in the code.

### **3. Create Environment Variables**

Create two environment variables on your PC:

* `EMAIL_ADDRESS` — your Gmail address
* `EMAIL_PASSWORD` — the **app password** (not your real Gmail password)

#### **Windows (PowerShell)**

```bash
setx EMAIL_ADDRESS "your_email@gmail.com"
setx EMAIL_PASSWORD "your_app_password"
```

#### **Mac / Linux**

```bash
export EMAIL_ADDRESS="your_email@gmail.com"
export EMAIL_PASSWORD="your_app_password"
```

Your Flask code will securely access them using:

```python
os.getenv("EMAIL_ADDRESS")
os.getenv("EMAIL_PASSWORD")
```

---


## 🛠️ Tech Stack

If this is a static site:

* **HTML5**
* **CSS3** 
* **JavaScript** 
* **Flask**
* **Python 3.x**
* **Bootstrap / Custom CSS** 

---

## 📦 Installation & Setup

### 🔹 Static Version

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/cozy-cafe.git
   ```
2. Open `index.html` in your browser.
3. Done!

### 🔹 Flask Version

1. Clone the repo
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Run the server:

   ```bash
   flask run
   ```
4. Visit `http://127.0.0.1:5000`

---


## 📂 Project Structure (Example)

```
/cozy-cafe
│── static/
│   ├── css/
│   ├── js/
│   └── images/
│── templates/
│   ├── index.html
│   ├── about.html
│   └── contact.html
│── app.py
│── README.md
```

---

## 🎯 Purpose

This project was created for
✔ learning front-end development
✔ practicing UI/UX design
✔ experimenting with Flask (optional)

It can be used as a **real business landing page**, a **portfolio project**, or a **template for other small cafés**.

---

## 📸 Screenshots

<img width="1908" height="896" alt="image" src="https://github.com/user-attachments/assets/4a313e35-0e76-4b9a-bfea-c90973e4c023" />
<img width="1879" height="888" alt="image" src="https://github.com/user-attachments/assets/b7f50410-b3c0-4e0c-9cba-af8a4561dfd1" />
<img width="1887" height="887" alt="image" src="https://github.com/user-attachments/assets/a86b88e2-6505-425f-9ef4-070566a3fdbb" />
<img width="1880" height="791" alt="image" src="https://github.com/user-attachments/assets/e208e2d6-86ef-4b6b-bf9f-f56c27867a94" />
<img width="1873" height="892" alt="image" src="https://github.com/user-attachments/assets/157a125b-60d7-413d-a2d8-7182c0ac8ca6" />
<img width="1883" height="895" alt="image" src="https://github.com/user-attachments/assets/ad6e7598-b7a8-4472-9ec7-2481adf96bdb" />




---


