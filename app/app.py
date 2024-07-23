from flask import Flask, render_template, request, redirect
import MySQLdb

app = Flask(__name__)

# MySQL configurations
db = MySQLdb.connect(
    host="db",  # This is the service name in docker-compose
    user="root",
    passwd="password",
    db="user_data"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    db.commit()
    cursor.close()
    
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

