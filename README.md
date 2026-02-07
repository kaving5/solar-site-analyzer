# Solar Panel Site Analyzer

# Full-Stack Spatial Analysis Application

# Overview

−The Solar Panel Site Analyzer is a full-stack web application designed to identify and evaluate potential locations for solar panel installations using spatial and infrastructure data.

−The system analyzes multiple geographic and environmental factors and computes a Suitability Score (0–100) for each site, helping decision-makers prioritize optimal locations for solar development.

# Core Objectives

* Analyze land locations using spatial attributes
* Calculate a weighted Suitability Score
* Allow dynamic re-analysis based on changing priorities
* Visualize results on an interactive map
* Present statistics and rankings through a clean UI
* Maintain clear separation of concerns across backend and frontend

# What is a Suitability Score?
    The Suitability Score represents how ideal a land parcel is for solar panel installation.
It combines multiple normalized factors into a single score.
Each factor is scored from 0–100, then combined using weights that represent business or policy priorities.

# formula(Calculation of Suitability Score)
# Suitability Score Formula
Suitability Score =
  (Solar Score × 0.35) +
  (Area Score × 0.25) +
  (Grid Score × 0.20) +
  (Slope Score × 0.15) +
  (Infrastructure Score × 0.05)

# System Architecture

System Architecture
Frontend (Angular)
│
├── Dashboard (Statistics)
├── Site List
├── Site Detail
├── Analyze (Weight Adjustment)
├── Interactive Map (Leaflet)
│
Backend (Django REST Framework)
│
├── Models (Site)
├── Services (Suitability Calculator)
├── Serializers (Validation + Formatting)
├── APIs (CBV + FBV)
├── Management Command (CSV Loader)
│
Database (MySQL)

# Technology Stack

Backend

- Django REST Framework
- MySQL
- Custom Service Layer
- Function-Based & Class-Based Views
- Custom Management Commands


Frontend
- Angular (Standalone Components)
- SCSS (Responsive Design)
- Leaflet.js (Interactive Maps)
- REST API Integration


# Project Structure

solar-site-analyzer/
│
├── backend/
│   ├── sites/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── services/
│   │   │   └── suitability_calculator.py
│   │   ├── management/
│   │   │   └── commands/
│   │   │       └── load_sites_csv.py
│   ├── settings.py
│   └── urls.py
│
├── frontend/
│   ├── core/services/
│   ├── pages/
│   │   ├── dashboard/
│   │   ├── site-list/
│   │   ├── site-detail/
│   │   ├── analyze/
│   │   └── map/
│   ├── app.routes.ts
│   └── styles.scss
│
└── README.md


# Backend Design Highlights

* MySQL Schema:

1>Designed for spatial attributes
2>Indexed for performance
3>Extensible for future GIS integrations

* Custom Management Command

 load_sites_csv.py

1.Loads initial spatial dataset
2.Validates required columns
3.Ensures clean bootstrap without admin input


* Service-Oriented Scoring Logic
1> All calculation logic isolated in:
     services/suitability_calculator.py
2>Enables:
    Easy testing
    Weight adjustments
    Reuse across APIs

# Endpoints (Api Design)

1> GET /api/sites    ---   List all sites with scores
2> POST /api/get_sites_by_id  ---- Fetch detailed site info
3> POST /api/analyze   ---   Recalculate using custom weights
4> GET /api/statistics      ----  Aggregate analytics


* Input validation handled at serializer level
* Strict payload enforcement
* Consistent response structure for UI handling

# Frontend Design Highlights

✔ Dashboard

1.Total sites
2.Average / Min / Max scores
3.Entry point for navigation

✔ Interactive Map (Leaflet.js)

1.Marker-based visualization
2.Color-coded scoring:
🟢 High suitability
🟡 Medium suitability
🔴 Low suitability
Click markers to view site details

✔ Analyze Screen

1.Adjustable weights (must sum to 1.0)
2.Real-time re-analysis
3.Sorted results by suitability

✔ Site Detail Page

1.Score breakdown per factor
2.Category badges (Excellent / Good / Poor)
3.Clean, readable layout



# End-to-End Flow

- Load spatial data via CSV
- Store sites in MySQL
- Calculate scores using default weights
- Display results in UI
-Visualize sites on map
- Adjust weights dynamically
- Recalculate & re-rank
-View statistics & insights



# Run Locally
* Backend

python -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py load_sites_csv path/to/data.csv  (management command)
pip install django djangorestframework mysqlclient
python manage.py runserver

* Frontend

npm install
npm install leaflet
ng serve


# Access:

Frontend → http://localhost:4200
Backend → http://127.0.0.1:8000


# Conclusion

- This project demonstrates:
* Clean full-stack architecture
- Real-world spatial analysis logic
* Scalable backend design
- Modern frontend practices
* Clear separation of concerns
- Practical decision-support modeling.

It reflects how geospatial data can be transformed into actionable insights for renewable energy planning.
