from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, Patient, Appointment
from . import db

# Blueprint definition
main = Blueprint('main', __name__)

# Routes
@main.route('/')
def home():
    return render_template('home.html')

@main.route('/patients', methods=['GET', 'POST'])
@login_required
def patients():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        address = request.form.get('address')
        new_patient = Patient(name=name, age=age, address=address)
        db.session.add(new_patient)
        db.session.commit()
        flash('Patient added successfully!')
        return redirect(url_for('main.patients'))
    
    patients = Patient.query.all()
    return render_template('patients.html', patients=patients)

@main.route('/departments')
@login_required
def departments():
    return render_template('departments.html')

@main.route('/appointments')
@login_required
def appointments():
    return render_template('appointments.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            flash('Login successful')
            return redirect(url_for('main.home'))
        flash('Login failed. Check your username and/or password.')
    return render_template('login.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if password != confirm_password:
            flash('Passwords do not match.')
            return redirect(url_for('main.register'))

        hashed_password = generate_password_hash(password)
        user = User(username=username, email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful. You can now log in.')
        return redirect(url_for('main.login'))

    return render_template('register.html')

@main.route('/contact')
@login_required
def contact():
    return render_template('contact.html')

@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.login'))
