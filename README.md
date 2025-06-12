# ⛽ Petrol Bunk Finder (Nearest FuelFinder)

This is an AI-powered web application that helps users quickly locate nearby petrol bunks (fuel stations) based on their current location. It's built using Django, integrated with AI features and Google Maps to provide real-time search results.

---

## 🚀 Features

- 🔍 Find nearby petrol bunks instantly
- 🧠 AI-assisted filtering (e.g., by rating or distance)
- 📍 Google Maps integration for precise navigation
- 🗺️ User-friendly UI and map-based display
- 🔐 Secure and lightweight backend using Django
- 🧪 REST API ready (extensible for mobile or frontend frameworks)

---

## 🛠️ Tech Stack

| Area           | Technologies Used                           |
|----------------|----------------------------------------------|
| Frontend       | HTML, CSS, JavaScript, Bootstrap             |
| Backend        | Python, Django                               |
| AI Integration | Custom logic (e.g., scoring or ranking bunk data) |
| Map API        | Google Maps Places API                       |
| Database       | SQLite (default Django DB)                   |
| Hosting        | Localhost / Can be deployed on Heroku/Vercel |
| Virtual Env    | `venv` (Python virtual environment)          |

---

## 🧠 How AI is Implemented

- **Filtering Algorithm**: Ranks petrol bunks based on distance and user ratings using a custom logic.
- **Future Improvements**: Scope for integrating ML models for predicting fuel availability, dynamic pricing suggestions, etc.

---

## 📂 Project Structure

```bash
petrol_bunk_finder/
│
├── petrolapp/            # Main Django app
├── petrol_bunk_finder/   # Project settings
├── ai_model/             # AI/algorithm scripts
├── templates/            # HTML templates
├── static/               # Static files (CSS, JS, images)
├── db.sqlite3            # Database
├── requirements.txt      # Python dependencies
├── manage.py             # Django manager
└── venv/                 # Virtual environment

---

## 🧪 Setup Instructions

1. **Clone the repo**  
   ```bash
   git clone https://github.com/Harinisenthilkumar/Nearest_FuelFinder.git
   cd Nearest_FuelFinder
Set up virtual environment

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the app

bash
Copy
Edit
python manage.py runserver
Visit http://127.0.0.1:8000/ in your browser.

