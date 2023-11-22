# class_management.py
from flask import Blueprint, render_template, redirect, url_for, request
from db_config import execute_query

class_management_routes = Blueprint('class_management', __name__)

@class_management_routes.route('/classes', methods=['GET'])
def classes():
    query = "SELECT * FROM Classes"
    classes = execute_query(query)
    return render_template('classes.html', classes=classes)

@class_management_routes.route('/classes/add', methods=['GET', 'POST'])
def add_class():
    if request.method == 'POST':
        class_name = request.form.get('class_name')
        description = request.form.get('description')
        schedule_date = request.form.get('schedule_date')
        schedule_time = request.form.get('schedule_time')
        max_capacity = request.form.get('max_capacity')
        instructor_id = request.form.get('instructor_id')  # TrainerID

        query = """
            INSERT INTO Classes (ClassName, Description, ScheduleDate, ScheduleTime, MaxCapacity, InstructorID)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (class_name, description, schedule_date, schedule_time, max_capacity, instructor_id)
        execute_query(query, values)

        return redirect(url_for('class_management.classes'))

    # Fetch instructors (trainers) to populate the dropdown
    instructors_query = "SELECT TrainerID, CONCAT(FirstName, ' ', LastName) AS InstructorName FROM Trainers"
    instructors = execute_query(instructors_query)

    return render_template('add_class.html', instructors=instructors)

@class_management_routes.route('/classes/<int:class_id>/edit', methods=['GET', 'POST'])
def edit_class(class_id):
    if request.method == 'POST':
        class_name = request.form.get('class_name')
        description = request.form.get('description')
        schedule_date = request.form.get('schedule_date')
        schedule_time = request.form.get('schedule_time')
        max_capacity = request.form.get('max_capacity')
        instructor_id = request.form.get('instructor_id')  # TrainerID

        query = """
            UPDATE Classes
            SET ClassName = %s, Description = %s, ScheduleDate = %s, ScheduleTime = %s,
                MaxCapacity = %s, InstructorID = %s
            WHERE ClassID = %s
        """
        values = (class_name, description, schedule_date, schedule_time, max_capacity, instructor_id, class_id)
        execute_query(query, values)

        return redirect(url_for('class_management.classes'))

    query = "SELECT * FROM Classes WHERE ClassID = %s"
    class_info = execute_query(query, (class_id,), fetch_one=True)

    # Fetch instructors (trainers) to populate the dropdown
    instructors_query = "SELECT TrainerID, CONCAT(FirstName, ' ', LastName) AS InstructorName FROM Trainers"
    instructors = execute_query(instructors_query)

    return render_template('edit_class.html', class_info=class_info, instructors=instructors)

@class_management_routes.route('/classes/<int:class_id>/delete', methods=['POST'])
def delete_class(class_id):
    if request.method == 'POST':
        query = "DELETE FROM Classes WHERE ClassID = %s"
        execute_query(query, (class_id,))

        return redirect(url_for('class_management.classes'))

# Add more routes for editing and deleting classes if needed
# You can follow a similar structure to the existing trainer and member management routes.
