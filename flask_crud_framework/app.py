from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = "crud_secret"

# Connect to MySQL database
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",      # keep empty unless you set one in XAMPP
        database="flask_crud_db"
    )

# Home route – list all employees
@app.route('/')
def index():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employee")
    data = cursor.fetchall()
    conn.close()
    return render_template("index.html", employees=data)

# Add employee route
@app.route('/add', methods=['POST', 'GET'])
def add_employee():
    if request.method == 'POST':
        name = request.form['name']
        role = request.form['role']
        salary = request.form['salary']

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO employee (name, role, salary) VALUES (%s, %s, %s)", (name, role, salary))
        conn.commit()
        conn.close()
        flash("Employee added successfully!")
        return redirect(url_for('index'))

    return render_template('add.html')

# Edit employee route
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_employee(id):
    conn = get_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        name = request.form['name']
        role = request.form['role']
        salary = request.form['salary']

        cursor.execute("UPDATE employee SET name=%s, role=%s, salary=%s WHERE id=%s", (name, role, salary, id))
        conn.commit()
        conn.close()
        flash("Employee updated successfully!")
        return redirect(url_for('index'))

    cursor.execute("SELECT * FROM employee WHERE id=%s", (id,))
    employee = cursor.fetchone()
    conn.close()
    return render_template('edit.html', employee=employee)

# Delete employee route
@app.route('/delete/<int:id>', methods=['GET'])
def delete_employee(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employee WHERE id=%s", (id,))
    conn.commit()
    conn.close()
    flash("Employee deleted successfully!")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
