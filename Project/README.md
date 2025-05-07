# 📝 FastAPI Todo API

A simple FastAPI-based Todo application with SQLite + Docker support.

---

## 🚀 Features

- ✅ REST API with FastAPI
- 🗃️ SQLite database using SQLModel
- 🐳 Dockerized for easy deployment
- 🔄 GitHub Actions CI for linting and build test

---

## 📦 Tech Stack

- FastAPI
- SQLModel
- SQLite
- Docker
- GitHub Actions

---

## 🛠️ Setup Locally

```bash
git clone https://github.com/YOUR_USERNAME/fastapi-todo.git
cd fastapi-todo
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
