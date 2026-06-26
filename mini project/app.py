from flask import Flask, render_template, request, redirect
import sqlite3
import random

app = Flask(__name__)

# ---------------- DATABASE ---------------- #

def create_table():

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(

        student_id TEXT PRIMARY KEY,

        name TEXT,
        gender TEXT,
        dob TEXT,

        mobile TEXT,
        email TEXT,

        address TEXT,
        state TEXT,
        district TEXT,
        city TEXT,
        pincode TEXT,

        board TEXT,
        group_name TEXT,
        subjects TEXT,

        tenth_mark REAL,
        twelfth_mark REAL,

        father_name TEXT,
        mother_name TEXT,

        department TEXT,

        percentage REAL,
        grade TEXT,

        scholarship TEXT,
        merit_rank INTEGER,

        status TEXT
    )
    """)

    conn.commit()
    conn.close()

create_table()

# ---------------- HOME ---------------- #

@app.route('/')
def home():
    return render_template('home.html')


# ---------------- REGISTER ---------------- #

@app.route('/register')
def register():
    return render_template('register.html')


# ---------------- ADMISSION ---------------- #

@app.route('/admission', methods=['POST'])
def admission():

    name = request.form['name']
    gender = request.form['gender']
    dob = request.form['dob']

    mobile = request.form['mobile']
    email = request.form['email']

    address = request.form['address']
    state = request.form['state']
    district = request.form['district']
    city = request.form['city']
    pincode = request.form['pincode']

    board = request.form['board']
    group_name = request.form['group_name']
    subjects = request.form['subjects']

    tenth_mark = float(request.form['tenth_mark'])
    twelfth_mark = float(request.form['twelfth_mark'])

    father_name = request.form['father_name']
    mother_name = request.form['mother_name']

    department = request.form['department']

    percentage = (tenth_mark + twelfth_mark) / 2

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    else:
        grade = "D"

    if percentage >= 95:
        scholarship = "100%"
    elif percentage >= 90:
        scholarship = "75%"
    elif percentage >= 85:
        scholarship = "50%"
    else:
        scholarship = "No Scholarship"

    merit_rank = random.randint(1, 1000)

    if percentage >= 75:
        status = "Admission Approved"
    elif percentage >= 60:
        status = "Waiting List"
    else:
        status = "Admission Rejected"

    student_id = "KITS" + str(random.randint(10000,99999))

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO students
    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    """,

    (
        student_id,
        name,
        gender,
        dob,
        mobile,
        email,
        address,
        state,
        district,
        city,
        pincode,
        board,
        group_name,
        subjects,
        tenth_mark,
        twelfth_mark,
        father_name,
        mother_name,
        department,
        percentage,
        grade,
        scholarship,
        merit_rank,
        status
    ))

    conn.commit()
    conn.close()

    return render_template(
        "result.html",

        student_id=student_id,
        name=name,
        department=department,
        percentage=percentage,
        grade=grade,
        scholarship=scholarship,
        merit_rank=merit_rank,
        status=status
    )


# ---------------- VIEW STUDENTS ---------------- #

@app.route('/students')
def students():

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()

    conn.close()

    return render_template(
        "students.html",
        students=data
    )


# ---------------- SEARCH ---------------- #

@app.route('/search', methods=['GET','POST'])
def search():

    student = None

    if request.method == 'POST':

        sid = request.form['student_id']

        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM students WHERE student_id=?",
            (sid,)
        )

        student = cursor.fetchone()

        conn.close()

    return render_template(
        "search.html",
        student=student
    )


# ---------------- DELETE ---------------- #

@app.route('/delete/<student_id>')
def delete(student_id):

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE student_id=?",
        (student_id,)
    )

    conn.commit()
    conn.close()

    return redirect('/students')


# ---------------- DASHBOARD ---------------- #

@app.route('/dashboard')
def dashboard():

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM students")
    total = cursor.fetchone()[0]

    cursor.execute("""
    SELECT COUNT(*)
    FROM students
    WHERE status='Admission Approved'
    """)
    approved = cursor.fetchone()[0]

    cursor.execute("""
    SELECT COUNT(*)
    FROM students
    WHERE status='Admission Rejected'
    """)
    rejected = cursor.fetchone()[0]

    cursor.execute("""
    SELECT COUNT(*)
    FROM students
    WHERE status='Waiting List'
    """)
    waiting = cursor.fetchone()[0]

    conn.close()

    return render_template(
    "dashboard.html",
    total=total,
    approved=approved,
    waiting=waiting,
    rejected=rejected
)


if __name__ == "__main__":
    app.run(debug=True)
