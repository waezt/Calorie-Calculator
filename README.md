# Calorie & Fitness Calculator

A simple Flask web app that calculates your **daily calories (TDEE)**, **protein goal**, and **BMI** based on user inputs such as weight, height, age, activity level, gender, and fitness goal.  

All UI elements were taken from [uiverse.io](https://uiverse.io).

## Live Demo

Try the app live here: [Calorie Calculator](https://calorie-calculator-m13y.onrender.com)

---

## Features

### Calorie Calculator (TDEE)
- Calculates **Basal Metabolic Rate (BMR)**
- Applies an **activity multiplier**
- Adjusts calories based on the user’s goal:
  - **Cut** → -15% calories  
  - **Maintain** → no change  
  - **Bulk** → +15% calories  

### Protein Goal
- Automatically calculates recommended protein intake based on weight.

### BMI Calculator
Uses the standard formula: BMI = weight / (height²) * 10,000



---

## Tech Used
- **Python (Flask)**
- **HTML / CSS**
- **Jinja2 Templates**

---

## Project Structure
project/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   ├── index.html
│   └── base.html
└── static/
    └── style.css
