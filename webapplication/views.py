from flask import Blueprint, render_template, request, url_for
from flask_login import current_user
from werkzeug.utils import redirect
from .models import Student
from . import db

views = Blueprint('views', __name__)

@views.route('/homepage', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        record = request.form.get('newRecord')
        if record == "Enter new student record":
            return redirect(url_for('views.create_record'))

    return render_template("homePage.html", name="homePage", students = Student.query.all())


@views.route('/create_record', methods=['GET', 'POST'])
def create_record(): 
    if request.method == 'POST':
        first_name = request.form.get('fname')
        last_name = request.form.get('lname')
        mobile_number = request.form.get('mobileNo')
        email = request.form.get('email')
        sex = request.form.get('sex')
        date = request.form.get('date')
        qualification = request.form.get('qualification')
        tech = request.args.get('tech')
        image = request.form.get('img')
        description = request.form.get('desc')

        new_student = Student(first_name=str(first_name), last_name=str(last_name),  mobile_num=int(mobile_number), email_id=str(email),
        gender=str(sex), d_o_b=date, qualification=str(qualification), techStacks=str(tech), img=image, desc=str(description))
        print(tech)
        print(first_name)
        print(sex)
        db.session.add(new_student)
        db.session.commit()
        return redirect(url_for('views.homepage'))

    return render_template('student_creation_tab.html', name='creation_tab')


@views.route('/update_record/<int:id>', methods=['GET', 'POST'])
def update_record(id):
    record_to_update = Student.query.get_or_404(id)
    
    if request.method == 'POST':
        if record_to_update:
            db.session.delete(record_to_update)
            db.session.commit()

        first_name = request.form.get('fname')
        last_name = request.form.get('lname')
        mobile_number = request.form.get('mobileNo')
        email = request.form.get('email')
        sex = request.form.get('sex')
        date = request.form.get('date')
        qualification = request.form.get('qualification')
        tech = request.args.get('tech')
        image = request.form.get('img')
        description = request.form.get('desc')

        record_to_update = Student(first_name=str(first_name), last_name=str(last_name),  mobile_num=int(mobile_number), email_id=str(email),
        gender=str(sex), d_o_b=date, qualification=str(qualification), techStacks=str(tech), img=image, desc=str(description))
        db.session.add(record_to_update)
        db.session.commit()
        return redirect(url_for('views.create_record'))

    return render_template('student_creation_tab.html', name='update_tab')


@views.route('/delete_record/<int:id>', methods=['GET', 'POST'])
def delete_record(id):
    record_to_delete = Student.query.get_or_404(id)
    if record_to_delete:
        db.session.delete(record_to_delete)
        db.session.commit()
        return redirect(url_for('views.homepage'))

    return render_template('homePage.html', name='delete_record')            