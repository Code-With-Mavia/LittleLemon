# 🍋 LittleLemon - Restaurant Web App

![GitHub repo size](https://img.shields.io/github/repo-size/Code-With-Mavia/LittleLemon)
![GitHub last commit](https://img.shields.io/github/last-commit/Code-With-Mavia/LittleLemon)
![GitHub contributors](https://img.shields.io/github/contributors/Code-With-Mavia/LittleLemon)
![GitHub language count](https://img.shields.io/github/languages/count/Code-With-Mavia/LittleLemon)
![License](https://img.shields.io/github/license/Code-With-Mavia/LittleLemon)
![CI/CD](https://img.shields.io/badge/CI/CD-pending-lightgrey)
![Live Demo](https://img.shields.io/badge/Live-Demo-orange)

A **full-stack Django web application** for a restaurant, featuring menu management, booking system, and a REST API. Developed as part of the **Meta Backend Development Specialization**.

---

## 🚀 Features

- Menu browsing and detailed menu items
- Customer booking system
- REST API for menu and ratings (`littlelemonAPI`)
- Admin panel for restaurant management
- Responsive design with HTML, CSS
- Database powered by SQLite
- Fully modular Django project structure

---

## 🛠️ Tech Stack

**Backend & API**  
- Python 3.13  
- Django 5.2  
- Django REST Framework  

**Frontend**  
- HTML5  
- CSS3  
- Django Templates  

**Database**  
- SQLite  

**Tools & Environment**  
- Git & GitHub  
- VS Code  
- Pipenv (dependency management)  

---

## 📂 Project Structure

```

littlelemon/
│
├── littlelemon/          # Django project config
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

2. Install dependencies (using pipenv):

```bash
pipenv install
pipenv shell
```

3. Apply migrations:

```bash
python manage.py migrate
```

4. Create superuser (for admin panel):

```bash
python manage.py createsuperuser
```

5. Run the development server:

```bash
python manage.py runserver
```

6. Visit `http://127.0.0.1:8000/` in your browser.

---

## 🔗 API Endpoints

| Endpoint             | Method | Description               |
| -------------------- | ------ | ------------------------- |
| `/api/menu/`         | GET    | List all menu items       |
| `/api/menu/<id>/`    | GET    | Retrieve single menu item |
| `/api/ratings/`      | GET    | List all ratings          |
| `/api/ratings/<id>/` | GET    | Retrieve rating by ID     |

> Use Django REST Framework browsable API to explore endpoints.

---

## 🏷️ Badges (Tech Stack)

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python\&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.2-green?logo=django\&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-3-yellow?logo=sqlite\&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5\&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3\&logoColor=white)

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 💡 Future Enhancements

* Add user authentication and profiles
* Integrate with PostgreSQL or MySQL
* Add image uploads for menu items
* Dockerize the project
* Add automated tests for API endpoints
* Deploy live demo

---

## 🌐 Social & Contact

[![GitHub](https://img.shields.io/badge/GitHub-Code-With-Mavia-181717?logo=github\&logoColor=white)]([https://github.com/Code-With-Mavia](https://github.com/Code-With-Mavia))
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Mavia-blue?logo=linkedin\&logoColor=white)]([https://www.linkedin.com/in/your-profile](https://www.linkedin.com/in/maawiah-qaiser-10793722b/))
[![Email](https://img.shields.io/badge/Email-Contact-red?logo=gmail\&logoColor=white)](mailto:maviaqaiser09@gmail.com)

---

## 🎯 Author

**Mavia Qaiseriqbal**

* GitHub: [Code-With-Mavia](https://github.com/Code-With-Mavia)
* Email: `maviaqaiser09@gmail.com`

