# 🛡️ API Security Monitoring System

A real-time API attack detection and monitoring system built with **FastAPI** and **Streamlit**, designed to detect malicious activity (like XSS or SQL injection), log it, and visualize it live.

---

## Features

- 🔐 JWT-based API authentication
- 🧼 Middleware to detect XSS and SQL Injection attacks
- 📁 CSV logging of attack details (IP, type, user-agent, timestamp)
- 📊 Streamlit dashboard for real-time visualization
- 💻 Swagger UI for easy API testing

---

## Project Goals

- Understand how API-based attacks like XSS and SQLi are structured
- Build basic real-time detection logic using request inspection
- Log and visualize attack data for analysis and awareness
  
---

## Set Up Virtual Environment
cd path\to\application

# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate

---

## Tech Stack

| Component | Tech Used            |
|----------|----------------------|
| API      | FastAPI              |
| Auth     | JWT (JSON Web Token) |
| Frontend | Streamlit Dashboard  |
| Logging  | CSV File             |

---

## Install Dependencies


pip install -r requirements.txt

---

## Run the API Server

uvicorn main:app --reload

Access Swagger UI at: http://localhost:8000/docs

---

## Run the Dashboard

streamlit run dashboard.py

---







