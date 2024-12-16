from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

db_config = {
    'host': 'localhost',
    'user': 'root',       
    'password': 'root',   
    'database': 'school'
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/top-student', methods=['GET'])
def get_top_student():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        
        query = "SELECT name, marks FROM students ORDER BY marks DESC LIMIT 1"
        cursor.execute(query)
        result = cursor.fetchone()

        cursor.close()
        connection.close()

        if result:
            name, marks = result
            return render_template('result.html', name=name, marks=marks)
        else:
            return "No student records found."

    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    app.run(debug=True)
