from flask import Flask, render_template, request, redirect, url_for, flash
from firebase_config import firebase_config
import pyrebase

app = Flask(__name__)
app.secret_key = 'supersecretkey'

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

@app.route('/')
def dashboard():
    return render_template('dashboard.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('dashboard'))
        except:
            flash("Login failed. Check your credentials")
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.create_user_with_email_and_password(email, password)
            flash("Account created successfully")
            return redirect(url_for('login'))
        except:
            flash("Registration failed. Try again")
            return redirect(url_for('register'))
    return render_template('register.html')



if __name__ == '__main__':
    app.run(debug=True)
