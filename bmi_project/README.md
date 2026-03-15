BMI AI Diet & Exercise Planner (Django + Gemini)
Project Overview

This project is a Django web application that calculates a user's Body Mass Index (BMI) and generates a one-month diet and exercise plan using the Google Gemini API (LLM).

The system collects user information including:

Height (cm)

Weight (kg)

Age

Gender

The application calculates BMI using Python and then sends the user data to the Gemini AI model, which generates a personalized health plan.

Technologies Used

Python

Django

HTML / CSS

Google Gemini API

SQLite Database

BMI Calculation Formula

The BMI value is calculated using the formula:

BMI = weight / (height²)

In Python:

bmi = round(weight / (height**2), 2)
BMI Categories
BMI Range	Category
BMI < 20	Underweight
20 ≤ BMI < 25	Normal
BMI ≥ 25	Overweight
How the System Works

The user enters height, weight, age, and gender.

Django processes the form using a POST request.

The backend calculates BMI.

The BMI category is determined.

The BMI information is sent to the Gemini API.

Gemini generates a one-month diet and exercise plan.

The generated plan is displayed on the webpage.

Example Scenario 1
Young Underweight Person

Input:

Height: 170 cm

Weight: 50 kg

Age: 22

Gender: Male

Calculation:

BMI = 50 / (1.70 × 1.70)
BMI = 17.3

Result:

BMI: 17.3

Category: Underweight

AI Generated Plan Includes:

High-calorie healthy meals

Protein-rich foods

Strength training exercises

Weekly fitness schedule

(Insert Screenshot Here)

Example Scenario 2
Older Overweight Person

Input:

Height: 160 cm

Weight: 85 kg

Age: 36

Gender: Female

Calculation:

BMI = 85 / (1.60 × 1.60)
BMI = 33.2

Result:

BMI: 33.2

Category: Overweight

AI Generated Plan Includes:

Balanced calorie-controlled diet

Cardio exercises

Weekly walking routine

Low-impact workouts

(Insert Screenshot Here)

Project Structure
bmi_project
│
├── bmi_app
│   ├── views.py
│   ├── gemini_service.py
│
├── templates
│   └── bmi.html
│
├── manage.py
└── README.md
Installation

Clone the repository:

git clone https://github.com/yourusername/bmi-ai-planner.git

Install dependencies:

pip install django google-genai
Setup Gemini API Key

Create an API key from:

https://aistudio.google.com/app/apikey

Set the environment variable.

Windows PowerShell
$env:GEMINI_API_KEY="your_api_key_here"
Run the Application

Start the Django server:

python manage.py runserver

Open the browser:

http://127.0.0.1:8000
Future Improvements

Save user history

Add meal tracking

Add calorie calculator

Add charts for BMI trends

Improve AI prompt engineering