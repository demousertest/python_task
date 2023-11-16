from flask import Flask, render_template, request, url_for, redirect, flash, session

import mysql.connector
 
app = Flask(__name__)
app.secret_key = "Welcome"
conn = mysql.connector.connect(host='localhost', user='root', password='', database='employeedb')
cursor = conn.cursor()


@app.route("/")
def home():
    return render_template("home.html")

@app.route('/SignUp', methods = ['GET', 'POST'])
def SignUP():
    return render_template("signup.html")

@app.route("/login")
def login():
    conn.query_attrs_clear()
    return  render_template("login.html")

@app.route('/logout')
def logout():
    conn.query_attrs_clear()
    return redirect('/')

@app.route('/employees')
def display_data():
    cursor.execute("SELECT * FROM employee_data")
    data = cursor.fetchall()
    return render_template('empTBL.html', data=data)


@app.route('/adduser', methods=['POST'])
def adduser():
    first_name = request.form.get('firstname')
    last_name = request.form.get('lastname')
    email = request.form.get('email')
    password = request.form.get('password')
    user_name = request.form.get('username')

    try:
        cursor = conn.cursor(buffered=True)

        # Check if the user with the given email already exists
        select_query = "SELECT * FROM emp_t1 WHERE email = %s"
        cursor.execute(select_query, (email,))
        existing_user = cursor.fetchone()

        if existing_user:
            flash('User with this email already exists. Please try with a different email.', 'error')
            return render_template('signup.html')
        else:
            VAL = (first_name, last_name, email, password, user_name)
            query = "INSERT INTO emp_t1 (first_name, last_name, email, password, user_name) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, VAL)
            conn.commit()
            flash('User added successfully!', 'success')
            return render_template('login.html')

    except Exception as e:
        print(f"An error occurred: {e}")
        flash('An error occurred while adding the user. Please try again later.', 'error')
        return render_template('login.html')



@app.route('/loginValidation', methods= ['POST'])
def login_validation():
    email = request.form.get('email')
    password = request.form.get('password')
    try:
            
        cursor.execute('SELECT * FROM emp_t1 WHERE email=%s AND password=%s', (email, password))
        users = cursor.fetchall()
        print(users)

        if len(users) > 0:
            return render_template('employee_details.html')
        else:
            flash('Invalid email or password. Please try again.', 'error')
            return render_template('login.html')

    except Exception as e:
       
        print(f"An error occurred: {e}")
        flash('An error occurred. Please try again later.', 'error')
        return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)