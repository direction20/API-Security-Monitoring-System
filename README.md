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

steps :
1. get JWT token from /token 
1.1.On the docs page, scroll down to the /token endpoint.
1.2.Click the POST /token box to expand it.
1.3.Click "Try it out".
1.4.Fill in:
    username: admin
    password: admin
1.5.Click "Execute"
1.6.if successful will get access token string.

2.Authorize using JWT
2.1.Click the Authorize 🔐 button at the top right of the docs page.
2.2.In the popup box, paste the token like this:
(Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...)
2.3.Click "Authorize", then close the popup.

3.Test Attack Detection
3.1.Go to the POST /test-comment endpoint
3.2.Click Try it out
3.3.Paste this in the body:
{
  "comment": "<script>alert('xss')</script>"
}
OR
{
  "comment": "' OR 1=1--"
}
3.4.Click Execute
You’ll get a 400 error if an attack is detected.
logs/attacks.csv is automatically updated.

---

## Run the Dashboard

streamlit run dashboard.py

---







