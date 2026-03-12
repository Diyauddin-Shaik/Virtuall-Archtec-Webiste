# 🏠 AI Interior Design Web App (Django)

A full-stack **Interior Design Web Application** built with **Django, HTML, CSS, and JavaScript** that allows users to design different rooms, upload room images, receive design suggestions, and interact through a support chat system.

This project demonstrates **user authentication, database integration, image upload handling, dynamic templates, and admin monitoring**.

---

# 🚀 Features

✔ User Registration & Login
✔ Room Selection Dashboard
✔ Interior Design Input Form
✔ Upload Room Images
✔ Smart Design Suggestions
✔ Chat Support System
✔ User Design History
✔ Admin Panel Monitoring

---

# 🖼 Project Workflow

User Flow:

Login/Register
↓
Choose Room
↓
Fill Design Preferences
↓
Upload Room Image
↓
Get Interior Design Suggestion
↓
View Design Result
↓
Save Design History
↓
Chat With Interior Support

---

# 🧰 Technologies Used

Backend

* Python
* Django

Frontend

* HTML
* CSS
* JavaScript

Database

* SQLite

Other Tools

* Git
* GitHub
* VS Code

---

# 📂 Project Structure

```
Interior_Project
│
├── interior_project
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── mainapp
│   ├── migrations
│   ├── static
│   │   ├── css
│   │   ├── images
│   │   └── js
│   │
│   ├── templates
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── room_select.html
│   │   ├── room_design.html
│   │   ├── design_result.html
│   │   ├── chat.html
│   │   └── my_designs.html
│   │
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── media
├── manage.py
└── requirements.txt
```

---

# ⚙️ Installation Guide

Follow these steps to run the project locally.

---

## 1️⃣ Clone Repository

```
git clone https://github.com/yourusername/interior-design-project.git
```

```
cd interior-design-project
```

---

## 2️⃣ Create Virtual Environment

```
python -m venv venv
```

---

## 3️⃣ Activate Virtual Environment

Windows:

```
venv\Scripts\activate
```

Mac/Linux:

```
source venv/bin/activate
```

---

## 4️⃣ Install Dependencies

```
pip install -r requirements.txt
```

If requirements file is not available:

```
pip install django
pip install pillow
```

---

## 5️⃣ Run Migrations

```
python manage.py makemigrations
```

```
python manage.py migrate
```

---

## 6️⃣ Create Admin User

```
python manage.py createsuperuser
```

---

## 7️⃣ Run Server

```
python manage.py runserver
```

---

# 🌐 Open Application

User Interface

```
http://127.0.0.1:8000
```

Admin Panel

```
http://127.0.0.1:8000/admin
```

---

# 🧑‍💻 Admin Capabilities

The Django Admin Panel allows administrators to:

✔ View user accounts
✔ Monitor interior designs created by users
✔ View chat messages sent by users

---

# 🔒 Privacy & Security

✔ User-specific design history
✔ Chat messages visible only to the user
✔ Admin monitoring through Django admin panel

---

# 📸 Screenshots

Add screenshots of:

* Login Page
* Room Selection Page
* Design Result Page
* Chat Support Page

---

# 📈 Future Improvements

* AI generated interior design previews
* Real-time chat system
* Download design report (PDF)
* Modern UI framework (React / Tailwind)

---

# 👨‍💻 Author

**SK Diyauddin**

Python Developer | Cloud & DevOps Engineer

---

# ⭐ Support

If you found this project useful, please ⭐ the repository.

    
