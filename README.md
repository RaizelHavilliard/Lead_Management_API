# Lead Management API

## Overview

This project is a **simple and practical Lead Management REST API** built with **FastAPI**.
It is designed to help small businesses manage incoming leads, track their status, and trigger follow-up actions in a structured way.

The focus of this project is on **clean backend architecture**, **data validation**, and **real-world use cases**, rather than UI or frontend features.

---

## Problem It Solves

Many small businesses collect leads through forms, emails, or calls, but:

* Leads are stored in spreadsheets
* Follow-ups are forgotten
* There is no clear tracking of lead status

This API provides a backend solution to:

* Store leads safely
* Prevent duplicate entries
* Track lead status (new, contacted, converted)
* Prepare the system for automated follow-ups

---

## Features

* Create and store leads with validation
* Prevent duplicate leads using unique email checks
* Retrieve all stored leads
* Update lead status
* Trigger a follow-up action (logged for now)
* Simple API key authentication
* SQLite database for lightweight persistence

---

## Tech Stack

* **Python**
* **FastAPI**
* **SQLite**
* **SQLAlchemy**
* **Pydantic**
* **Uvicorn**

---

## Project Structure

```
lead_manager/
├─ app.py          # Main FastAPI application
├─ database.py     # Database connection and session
├─ models.py       # Database models
├─ schemas.py      # Request/response validation
├─ crud.py         # Database operations
├─ auth.py         # API key authentication
├─ requirements.txt
└─ README.md
```

---

## How to Run the Project

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the server

```bash
uvicorn app:app --reload
```

### 3. Access API documentation

Open your browser and go to:

```
http://127.0.0.1:8000/docs
```

---

## Authentication

All endpoints require an API key passed in the request header:

```
x-api-key: SECRET_API_KEY
```

---

## API Endpoints

### Create a new lead

```
POST /leads
```

Example body:

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "+49123456789"
}
```

---

### Get all leads

```
GET /leads
```

---

### Update lead status

```
PATCH /leads/{lead_id}
```

Example body:

```json
{
  "status": "contacted"
}
```

---

### Trigger follow-up

```
POST /leads/{lead_id}/follow-up
```

This endpoint simulates a follow-up action by logging the event.
It is designed to be easily extended to send emails or messages in the future.

---

## Design Decisions

* **FastAPI** was chosen for its speed, simplicity, and automatic documentation
* **SQLite** keeps the project lightweight and easy to run
* **API Key authentication** adds a basic but realistic security layer
* Business logic is separated from API routes for clarity and maintainability

---

## Possible Improvements

* Email or SMS integration for real follow-ups
* Pagination and filtering for leads
* Role-based authentication
* Docker support
* Migration to PostgreSQL for production use

---

## What This Project Demonstrates

* Ability to design and build a real backend API
* Understanding of REST principles
* Proper data validation and persistence
* Clean and maintainable project structure
* Practical problem-solving for real business needs

---
