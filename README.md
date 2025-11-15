# 🍋 LittleLemon — Restaurant Web App

![Stars](https://img.shields.io/github/stars/Code-With-Mavia/LittleLemon?style=plastic&logo=github&logoColor=white&color=FFD700)
![Forks](https://img.shields.io/github/forks/Code-With-Mavia/LittleLemon?style=plastic&logo=github&logoColor=white&color=00C9A7)
![Issues](https://img.shields.io/github/issues/Code-With-Mavia/LittleLemon?style=plastic&logo=gitbook&logoColor=white&color=FF4B4B)
![Repo Size](https://img.shields.io/github/repo-size/Code-With-Mavia/LittleLemon?style=plastic&logo=dropbox&logoColor=white&color=9D4EDD)
![Last Commit](https://img.shields.io/github/last-commit/Code-With-Mavia/LittleLemon?style=plastic&logo=git&logoColor=white&color=00C851)
![Contributors](https://img.shields.io/github/contributors/Code-With-Mavia/LittleLemon?style=plastic&logo=users&logoColor=white&color=FFB300)
![Languages](https://img.shields.io/github/languages/count/Code-With-Mavia/LittleLemon?style=plastic&logo=codefactor&logoColor=white&color=4285F4)
![License](https://img.shields.io/github/license/Code-With-Mavia/LittleLemon?style=plastic&logo=open-source-initiative&logoColor=white&color=FFD43B)
[![Live Demo](https://img.shields.io/badge/Live%20Demo-🚀-8A2BE2?style=plastic)](https://portfolio-taupe-one-51.vercel.app/)
![CI/CD](https://img.shields.io/badge/CI%2FCD-Active-808080?style=plastic&logo=githubactions&logoColor=white)

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

- 🍽️ **Menu Management** — Browse, filter, and view restaurant items.  
- 📅 **Customer Bookings** — Table reservation system with date and slot selection.  
- 🔌 **REST API** — Full-featured API for menu items and ratings (`littlelemonAPI`).  
- 🛠️ **Admin Dashboard** — Manage dishes, bookings, and user accounts.  
- 📱 **Responsive Design** — Optimized layout for mobile, tablet, and desktop.  
- 💾 **MySQL Database** — Stores user, menu, and booking data across multiple databases.  
- 🧩 **Modular Django Structure** — Scalable and maintainable architecture for future enhancements.

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
- ![MySQL](https://img.shields.io/badge/MySQL-4479A1?logo=mysql&logoColor=white)  
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
├── users/                # User authentication app
├── db.sqlite3            # Default database (or MySQL configured)
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

3. **Configure databases**

   * Update `settings.py` with your MySQL credentials for `default` and `reservations`.

4. **Apply migrations**

   ```bash
   python manage.py migrate
   ```

5. **Create superuser**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**

   ```bash
   python manage.py runserver
   ```

7. **Access the app**

   ```
   http://127.0.0.1:8000/
   ```

---

## 🔗 API Endpoints

| Endpoint                | Method | Description                 | Example                                                                                            |
| ----------------------- | ------ | --------------------------- | -------------------------------------------------------------------------------------------------- |
| `/api/menu/`            | GET    | List all menu items         | `curl http://127.0.0.1:8000/api/menu/`                                                             |
| `/api/menu/<id>/`       | GET    | Retrieve a single menu item | `curl http://127.0.0.1:8000/api/menu/1/`                                                           |
| `/api/ratings/`         | GET    | List all ratings            | `curl http://127.0.0.1:8000/api/ratings/`                                                          |
| `/api/ratings/<id>/`    | GET    | Retrieve a rating by ID     | `curl http://127.0.0.1:8000/api/ratings/1/`                                                        |
| `/restaurant/bookings/` | POST   | Create a new booking        | JSON payload: `{"first_name":"John", "reservation_date":"2025-11-15", "reservation_slot":"18:00"}` |

> 💡 Use the Django REST Framework browsable API or Insomnia/Postman to interact with endpoints.

---

## 🖼️ Screenshots

![Home Page](https://via.placeholder.com/800x400.png?text=LittleLemon+Home+Page)
![Menu Page](https://via.placeholder.com/800x400.png?text=Menu+Page)
![Booking Page](https://via.placeholder.com/800x400.png?text=Booking+Page)

---

## 🔮 Future Enhancements

* 🔐 Add user profiles and roles
* 🗄️ Support full MySQL deployment across multiple environments
* 📸 Enable image uploads for menu items
* 🧪 Implement automated API and unit tests
* 🐳 Dockerize the application
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

**Maawiah Qaiser** — *Aspiring Backend Engineer*

* GitHub: [Code-With-Mavia](https://github.com/Code-With-Mavia)
* LinkedIn: [maawiah-qaiser](https://www.linkedin.com/in/maawiah-qaiser-10793722b/)
* Email: `maviaqaiser09@gmail.com`

---

## 🙌 Acknowledgments

* Meta Backend Development Specialization (Coursera)
* Inspired by modern restaurant web applications
* Contributions, suggestions, and feedback are welcome 💡

```
```
