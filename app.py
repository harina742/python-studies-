#app.py
from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/admission', methods=['POST'])
def admission():

    name = request.form['name']
    department = request.form['department']

    maths = int(request.form['maths'])
    physics = int(request.form['physics'])
    chemistry = int(request.form['chemistry'])

    total = maths + physics + chemistry
    percentage = total / 3

    student_id = "STU" + str(random.randint(1000,9999))

    if percentage >= 85:
        status = "Admission Approved"
    elif percentage >= 60:
        status = "Waiting List"
    else:
        status = "Admission Rejected"

    return render_template(
        'result.html',
        student_id=student_id,
        name=name,
        department=department,
        mark1=maths,
        mark2=physics,
        mark3=chemistry,
        total=total,
        percentage=round(percentage,2),
        status=status
    )

if __name__ == '__main__':
    app.run(debug=True)

