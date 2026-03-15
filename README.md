# ConstraCRM

ConstraCRM is a **Contractor Lead Marketplace SaaS Starter Platform** designed for lead sellers, contractor networks, and service marketplaces.

It provides a simple system for capturing contractor buyer inquiries, organizing demand by market and service category, and managing requests through a lightweight CRM intake workflow.

This project serves as a **minimum viable SaaS prototype** that can be expanded into a full lead marketplace platform.

---

## Platform Preview

### Buyer Intake Form
![Buyer Intake](screenshots/index.png)

### CRM Dashboard
![Dashboard](screenshots/dashboard.png)

---

# Product Overview

ConstraCRM is designed as a **Contractor Lead Marketplace Starter Kit**.

This project can be used by:

- Lead generation agencies
- Contractor networks
- Marketing firms selling contractor leads
- Service marketplaces
- Growth agencies building CRM workflows

ConstraCRM captures buyer demand, organizes contractor lead requests, and routes inquiries into a lightweight CRM intake pipeline.

The platform is intentionally simple so it can be easily customized, expanded, or integrated into larger SaaS systems.

---

# Core Features

### Contractor Buyer Intake Portal
A clean web interface where contractors submit requests for lead access.

### FastAPI Backend API
Handles lead submissions, validation, and storage through REST endpoints.

### CRM Inquiry Pipeline
All submissions are stored and organized into a structured inquiry record.

### Admin Dashboard
A simple dashboard for viewing incoming contractor buyer inquiries.

### Market & Trade Filtering
Submissions capture service type, geographic market, and service radius.

---

# Technology Stack

- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** FastAPI (Python)  
- **Data Storage:** JSON file (prototype storage)  
- **API Layer:** REST endpoints  
- **Dashboard:** Client-side rendering via API  

---

# Project Structure


ConstraCRM
│
├── backend
│ ├── main.py
│ └── buyer_inquiries.json
│
├── frontend
│ ├── index.html
│ └── dashboard.html
│
├── screenshots
│ ├── dashboard.png
│ └── index.png
│
└── README.md


---

# Running the Application

## 1. Start the backend server

Navigate to the backend directory and run:


cd backend
python -m uvicorn main:app --reload


The API will start at:


http://127.0.0.1:8000


---

## 2. Open the frontend

Open the intake form:


frontend/index.html


Open the dashboard:


frontend/dashboard.html


---

# Quick Setup Guide

1. Clone the repository


git clone https://github.com/lillisoto9902/constracrm


2. Navigate to the backend folder


cd constracrm/backend


3. Install dependencies


pip install fastapi uvicorn


4. Start the API server


python -m uvicorn main:app --reload


5. Open the frontend


frontend/index.html


The intake form will submit contractor inquiries into the FastAPI backend and store them in the CRM pipeline.

---

# API Endpoints

### Submit Buyer Inquiry


POST /api/buyer-inquiry


Stores contractor lead requests.

### Retrieve Inquiries


GET /api/inquiries


Returns all stored buyer inquiries.

---

# Commercial Use

ConstraCRM can be used as the foundation for:

- Contractor lead marketplaces
- CRM intake systems
- Lead broker platforms
- Marketing agency dashboards

The system is intentionally lightweight so it can be extended with:

- user authentication
- email notifications
- Stripe billing
- lead routing automation
- database storage
- multi-tenant SaaS architecture

---

# License

This project is provided as a **SaaS prototype starter platform** and may be extended or customize
