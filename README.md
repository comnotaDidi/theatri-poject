# 🎭 Theatre Project

A Django-based web application for managing a theatre's performances, ticket reservations, and related data. Includes a fully functional REST API with JWT authentication and Swagger documentation.

---

## 🌐 Live Preview

> This project runs locally. To test the API and frontend, start the Django server and navigate to:

- **Frontend**: `http://127.0.0.1:8000/`
- **API Docs (Swagger)**: `http://127.0.0.1:8000/api/doc/swagger/`

---

## 🚀 Features

- 🔐 JWT Authentication
- 🛠️ Admin panel at `/admin/`
- 📄 API Documentation via Swagger at `/api/doc/swagger/`
- 🎭 Manage genres, actors, and plays
- 🎫 Manage theatre halls and performances
- 🧾 Create and manage reservations and tickets
- 🔍 Filter performances by date or other criteria
- 🌐 Multi-language interface supported

---

## 📦 API Endpoints

All main API endpoints are available under `/api/`:

- `/api/genres/` – Genres CRUD
- `/api/actors/` – Actors CRUD
- `/api/plays/` – Plays CRUD
- `/api/halls/` – Theatre Halls
- `/api/performances/` – Performances and scheduling
- `/api/reservations/` – Ticket reservations
- `/api/tickets/` – Issued tickets

---

## 🔐 Authentication

Use the following endpoints to get a JWT token:

- `POST /api/token/` – Get access and refresh tokens
- `POST /api/token/refresh/` – Refresh your access token

---

## 🧑‍💻 Technologies

- Python 3.11+
- Django 4+
- Django REST Framework
- SimpleJWT (JWT Authentication)
- drf-yasg (Swagger docs)
- Bootstrap (for UI)

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/comnotaDidi/theatri-poject.git
   cd theatri-poject
