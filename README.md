# 🍋 LittleLemon — Restaurant Web App

![Stars](https://img.shields.io/github/stars/Code-With-Mavia/LittleLemon?color=gold&style=flat-square)
![Forks](https://img.shields.io/github/forks/Code-With-Mavia/LittleLemon?color=teal&style=flat-square)
![Issues](https://img.shields.io/github/issues/Code-With-Mavia/LittleLemon?color=red&style=flat-square)
![Repo Size](https://img.shields.io/github/repo-size/Code-With-Mavia/LittleLemon?color=blueviolet&style=flat-square)
![Last Commit](https://img.shields.io/github/last-commit/Code-With-Mavia/LittleLemon?color=brightgreen&style=flat-square)
![Contributors](https://img.shields.io/github/contributors/Code-With-Mavia/LittleLemon?color=orange&style=flat-square)
![Languages](https://img.shields.io/github/languages/count/Code-With-Mavia/LittleLemon?color=blue&style=flat-square)
![License](https://img.shields.io/github/license/Code-With-Mavia/LittleLemon?color=yellow&style=flat-square)
[![Live Demo](https://img.shields.io/badge/🚀-Live%20Demo-blueviolet?style=flat-square)](https://portfolio-taupe-one-51.vercel.app/)
![CI/CD](https://img.shields.io/badge/CI%2FCD-Pending-lightgrey?style=flat-square)

> A **full-stack Django web application** for a modern restaurant — featuring menu management, booking system, and REST API endpoints.  
> Built as part of the **Meta Backend Development Specialization**.

---

## 📚 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [API Endpoints](#-api-endpoints)
- [Screenshots](#-screenshots)
- [Future Enhancements](#-future-enhancements)
- [License](#-license)
- [Contact](#-contact)
- [Author](#-author)
- [Acknowledgments](#-acknowledgments)

---

## 🚀 Features

- 🍽️ **Menu Management** — Browse and manage restaurant items.  
- 📅 **Customer Bookings** — Integrated table reservation system.  
- 🔌 **REST API** — Full-featured API for menu and ratings (`littlelemonAPI`).  
- 🛠️ **Admin Dashboard** — Manage dishes, bookings, and user data.  
- 📱 **Responsive Design** — Clean UI optimized for all screens.  
- 💾 **SQLite Database** — Lightweight and reliable data storage.  
- 🧩 **Modular Django Structure** — Scalable, maintainable project setup.

---

## 🛠️ Tech Stack

**Backend & API**
- ![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white)  
- ![Django](https://img.shields.io/badge/Django-5.2-green?logo=django&logoColor=white)  
- Django REST Framework  

**Frontend**
- ![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)  
- ![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)  
- Django Templates  

**Database & Tools**
- ![SQLite](https://img.shields.io/badge/SQLite-3-yellow?logo=sqlite&logoColor=white)  
- Git & GitHub  
- VS Code  
- Pipenv  

---

## 📁 Project Structure

```

littlelemon/
│
├── littlelemon/          # Django project configuration
├── littlelemonAPI/       # API app (serializers, views, urls)
├── restaurant/           # Main app (models, templates, static)
├── db.sqlite3            # Database
├── Pipfile / Pipfile.lock
└── manage.py

````

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Code-With-Mavia/LittleLemon.git
   cd LittleLemon
````

2. **Install dependencies**

   ```bash
   pipenv install
   pipenv shell
   ```

3. **Apply migrations**

   ```bash
   python manage.py migrate
   ```

4. **Create superuser**

   ```bash
   python manage.py createsuperuser
   ```

5. **Run the server**

   ```bash
   python manage.py runserver
   ```

6. **Visit**

   ```
   http://127.0.0.1:8000/
   ```
``````
---

## 🔗 API Endpoints

| Endpoint             | Method | Description                 | Example                                     |
| -------------------- | ------ | --------------------------- | ------------------------------------------- |
| `/api/menu/`         | GET    | List all menu items         | `curl http://127.0.0.1:8000/api/menu/`      |
| `/api/menu/<id>/`    | GET    | Retrieve a single menu item | `curl http://127.0.0.1:8000/api/menu/1/`    |
| `/api/ratings/`      | GET    | List all ratings            | `curl http://127.0.0.1:8000/api/ratings/`   |
| `/api/ratings/<id>/` | GET    | Retrieve a rating by ID     | `curl http://127.0.0.1:8000/api/ratings/1/` |

> 💡 Explore endpoints via Django REST Framework’s browsable API.

---

## 🖼️ Screenshots

![Home Page](https://via.placeholder.com/800x400.png?text=LittleLemon+Home+Page)
![Menu Page](https://via.placeholder.com/800x400.png?text=Menu+Page)
![Booking Page](https://via.placeholder.com/800x400.png?text=Booking+Page)

---

## 🔮 Future Enhancements

* 🔐 Add user authentication & profiles
* 🗄️ Move to PostgreSQL / MySQL
* 📸 Enable image uploads for menu items
* 🧪 Implement automated API tests
* 🐳 Add Docker setup
* 🌍 Deploy a production-ready live demo

---

## 📄 License

This project is licensed under the **MIT License**.
See the [LICENSE](LICENSE) file for details.

---

## 📬 Contact

[![GitHub](https://img.shields.io/badge/GitHub-Code--With--Mavia-181717?logo=github\&logoColor=white)](https://github.com/Code-With-Mavia)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Maawiah%20Qaiser-blue?logo=linkedin\&logoColor=white)](https://www.linkedin.com/in/maawiah-qaiser-10793722b/)
[![Email](https://img.shields.io/badge/Email-maviaqaiser09%40gmail.com-red?logo=gmail\&logoColor=white)](mailto:maviaqaiser09@gmail.com)

---

## 💼 Portfolio

[![Portfolio](https://img.shields.io/badge/Visit-My%20Portfolio-blueviolet?style=flat-square)](https://portfolio-taupe-one-51.vercel.app/)

---

## 👨‍💻 Author

**Maawiah Qaiser**
*Aspiring Backend Engineer*

* GitHub: [Code-With-Mavia](https://github.com/Code-With-Mavia)
* LinkedIn: [maawiah-qaiser](https://www.linkedin.com/in/maawiah-qaiser-10793722b/)
* Email: `maviaqaiser09@gmail.com`

---

## 🙌 Acknowledgments

* Meta Backend Development Specialization (Coursera)
* Inspired by modern restaurant web apps
* Contributions & suggestions are always welcome! 💡

---

```

---
