from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/calculate/', methods=['POST', 'GET'])
def calc():
    if request.method == 'POST':
        weight = float(request.form['weight'])
        height = int(request.form['height'])
        age = int(request.form['age'])
        gender = request.form['gender']
        activity = float(request.form['activity'])
        goal = request.form['goal']
        if gender == 'male':
            BMR = (10 * weight) + (6.25 * height) - (5 * age) + 5
        else:
            BMR = (10 * weight) + (6.25 * height) - (5 * age) - 161

        TDEE = BMR * activity
        protein = weight * 2

        if goal == 'cut':
            TDEE = TDEE * 0.85
        elif goal == 'bulk':
            TDEE = TDEE * 1.15
        else:
            pass

        BMI = round(weight / (height * height) * 10000)
        if BMI < 18.5:
            bmi_category = "(Underweight)"
        elif 18.5 <= BMI < 25:
            bmi_category = "(Healthy)"
        elif 25 <= BMI < 30:
            bmi_category = "(Overweight)"
        else:
            bmi_category = "(Obese)"
        bmi_string = str(BMI) + ' ' + bmi_category

        minimun_water_intake = weight * 0.033


        return render_template('index.html', calories=round(TDEE),
                               protein=protein, bmi=bmi_string,
                               water=round(minimun_water_intake))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)