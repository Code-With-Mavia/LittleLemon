# 🍋 LittleLemon - Restaurant Web App

![Stars](https://img.shields.io/github/stars/Code-With-Mavia/LittleLemon?color=gold&style=flat-square)
![Forks](https://img.shields.io/github/forks/Code-With-Mavia/LittleLemon?color=teal&style=flat-square)
![Issues](https://img.shields.io/github/issues/Code-With-Mavia/LittleLemon?color=red&style=flat-square)
![Repo Size](https://img.shields.io/github/repo-size/Code-With-Mavia/LittleLemon?color=blueviolet&style=flat-square)
![Last Commit](https://img.shields.io/github/last-commit/Code-With-Mavia/LittleLemon?color=brightgreen&style=flat-square)
![Contributors](https://img.shields.io/github/contributors/Code-With-Mavia/LittleLemon?color=orange&style=flat-square)
![Languages](https://img.shields.io/github/languages/count/Code-With-Mavia/LittleLemon?color=blue&style=flat-square)
![License](https://img.shields.io/github/license/Code-With-Mavia/LittleLemon?color=yellow&style=flat-square)
[![Live Demo](https://img.shields.io/badge/Live%20Demo-%F0%9F%9A%80-blueviolet?style=flat-square)](https://portfolio-taupe-one-51.vercel.app/)
![CI/CD](https://img.shields.io/badge/CI%2FCD-pending-lightgrey?style=flat-square)

> A **full-stack Django restaurant web app** featuring menu management, booking system, and a REST API. Developed as part of the **Meta Backend Development Specialization**.

---

## 📋 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [API Endpoints](#-api-endpoints)
- [Screenshots](#-screenshots)
- [Future Enhancements](#-future-enhancements)
- [License](#-license)
- [Social & Contact](#-social--contact)
- [Portfolio](#-portfolio)
- [Author](#-author)

---

## 🚀 Features

- 🍽️ Browse restaurant menu with detailed items  
- 🧾 Customer booking system  
- 🔌 REST API for menu and ratings (`littlelemonAPI`)  
- 🛠️ Admin panel for restaurant management  
- 📱 Responsive design with HTML, CSS  
- 💾 SQLite database  
- 🏗️ Modular Django project structure  

---

## 🛠️ Tech Stack

**Backend & API**  
- ![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white) Python 3.13  
- ![Django](https://img.shields.io/badge/Django-5.2-green?logo=django&logoColor=white) Django 5.2  
- Django REST Framework  

**Frontend**  
- ![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white) HTML5  
- ![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white) CSS3  
- Django Templates  

**Database & Tools**  
- ![SQLite](https://img.shields.io/badge/SQLite-3-yellow?logo=sqlite&logoColor=white) SQLite  
- Git & GitHub  
- VS Code  
- Pipenv  

---

## 📂 Project Structure

```

littlelemon/
│
├── littlelemon/          # Django project configuration
├── littlelemonAPI/       # API app with serializers, views, and urls
├── restaurant/           # Main app with models, views, templates, static files
├── db.sqlite3            # Database
├── Pipfile / Pipfile.lock
├── manage.py

````

---

## ⚡ Installation

1. Clone the repository:

```bash
git clone https://github.com/Code-With-Mavia/LittleLemon.git
cd LittleLemon
````

2. Install dependencies:

```bash
pipenv install
pipenv shell
```

3. Apply migrations:

```bash
python manage.py migrate
```

4. Create superuser:

```bash
python manage.py createsuperuser
```

5. Run the development server:

```bash
python manage.py runserver
```

6. Open your browser at `http://127.0.0.1:8000/`

---

## 🔗 API Endpoints

| Endpoint             | Method | Description               | Example Request                             |
| -------------------- | ------ | ------------------------- | ------------------------------------------- |
| `/api/menu/`         | GET    | List all menu items       | `curl http://127.0.0.1:8000/api/menu/`      |
| `/api/menu/<id>/`    | GET    | Retrieve single menu item | `curl http://127.0.0.1:8000/api/menu/1/`    |
| `/api/ratings/`      | GET    | List all ratings          | `curl http://127.0.0.1:8000/api/ratings/`   |
| `/api/ratings/<id>/` | GET    | Retrieve rating by ID     | `curl http://127.0.0.1:8000/api/ratings/1/` |

> Use the Django REST Framework browsable API for interactive exploration.

---

## 🖼️ Screenshots / Preview

![Home Page](https://via.placeholder.com/800x400.png?text=LittleLemon+Home+Page)
![Menu Page](https://via.placeholder.com/800x400.png?text=Menu+Page)
![Booking Page](https://via.placeholder.com/800x400.png?text=Booking+Page)

> Replace placeholders with actual screenshots of your app.

---

## 💡 Future Enhancements

* 🔐 User authentication & profiles
* 🗄️ Switch to PostgreSQL or MySQL
* 📸 Image uploads for menu items
* 🐳 Dockerize the project
* 🧪 Automated API tests
* 🌐 Deploy live demo

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🌐 Social & Contact

[![GitHub](https://img.shields.io/badge/GitHub-Code-With-Mavia-181717?logo=github\&logoColor=white)](https://github.com/Code-With-Mavia)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Mavia-blue?logo=linkedin\&logoColor=white)](https://www.linkedin.com/in/maawiah-qaiser-10793722b/)
[![Email](https://img.shields.io/badge/Email-Contact-red?logo=gmail\&logoColor=white)](mailto:maviaqaiser09@gmail.com)

---

## 🌐 Portfolio

[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-blue?style=for-the-badge)](https://portfolio-taupe-one-51.vercel.app/)

---

## 🎯 Author

**Mavia Qaiseriqbal**

* GitHub: [Code-With-Mavia](https://github.com/Code-With-Mavia)
* LinkedIn: [maawiah-qaiser](https://www.linkedin.com/in/maawiah-qaiser-10793722b/)
* Email: `maviaqaiser09@gmail.com`

---

## ⭐ Contributors & Acknowledgments

* Thanks to **Meta Backend Dev Specialization** course
* Inspired by modern restaurant web apps
* Contributions are welcome — submit PRs or open issues!
