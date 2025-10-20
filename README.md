# 🍋 Little Lemon Restaurant Website  

![Django](https://img.shields.io/badge/Framework-Django-092E20?style=flat&logo=django&logoColor=white)
![HTML](https://img.shields.io/badge/Frontend-HTML5-E34F26?style=flat&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/Styling-CSS3-1572B6?style=flat&logo=css3&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## 🌐 Overview  

**Little Lemon Restaurant Website** is a full-stack web application built with **Django**, **HTML**, and **CSS**.  
It provides an elegant and responsive interface for customers to:  
- Explore the restaurant’s menu  
- Make table reservations  
- Contact the restaurant directly  

This project represents a professional restaurant site setup using Django’s core features — ideal for showcasing full-stack development and web design skills.  

---

## 🚀 Features  

### 🧾 Menu Page  
- Displays all menu items in a **table-based layout** for easy viewing.  
- Organized by categories like *Appetizers*, *Main Courses*, *Desserts*, and *Drinks*.  
- Styled for readability and presentation.  

### 📅 Booking System  
- Customers can book a table through a reservation form.  
- Django handles form validation and stores booking details.  
- Confirmation or success message displayed upon submission.  

### 📞 Contact Page  
- A simple and functional contact form for messages or feedback.  
- Submissions can be processed and viewed via Django admin.  

### 🏠 Home Page  
- Clean landing page with restaurant highlights, featured dishes, and navigation links.  

---

## 🛠️ Tech Stack  

| Layer | Technology |
|-------|-------------|
| **Backend** | Django |
| **Frontend** | HTML5, CSS3 |
| **Database** | SQLite (default for development) |
| **Server** | Django Development Server |
| **Version Control** | Git & GitHub |

---

## 📂 Project Structure  

```

LittleLemon/
├── manage.py
├── littlelemon/                # Project configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── restaurant/                 # Main app
│   ├── models.py               # Menu & booking models
│   ├── views.py                # Core view logic
│   ├── forms.py                # Booking and contact forms
│   ├── templates/restaurant/   # HTML templates
│   └── static/restaurant/css/  # CSS styling
└── db.sqlite3

````

---

## ⚙️ Installation & Setup  

### 1. Clone the Repository  
```bash
git clone https://github.com/yourusername/littlelemon.git
cd littlelemon
````

### 2. Create & Activate Virtual Environment

```bash
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Run the Server

```bash
python manage.py runserver
```

### 6. Open in Browser

Visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🧠 Key Django Concepts Used

* **Models:** For menu items and reservations.
* **Forms:** For booking and contact handling.
* **Templates:** For rendering HTML with Django template language.
* **Static Files:** Custom CSS styling integrated via Django’s static file setup.
* **URL Routing:** Organized and clean navigation.

---

## 💡 Future Improvements

* 🔐 Add user login & profile management.
* 📧 Email notifications for reservations.
* 📊 Admin dashboard enhancements.
* 🎨 Add JavaScript for interactivity and animations.

---

## 👨‍💻 Author

Developed with 💛 by **[Maawiah Qaiserl](https://github.com/code-with-mavia)**

> A Django-based web project inspired by the *Meta Back-End Developer* "Little Lemon" case study.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).
You’re free to use, modify, and share with attribution.

---
