# trainer_management.py
from flask import Blueprint, render_template, redirect, url_for, request
from db_config import execute_query

trainer_management_routes = Blueprint('trainer_management', __name__)


@trainer_management_routes.route('/trainers', methods=['GET'])
def trainers():
    query = "SELECT * FROM Trainers"
    trainers = execute_query(query)
    return render_template('trainers.html', trainers=trainers)


@trainer_management_routes.route('/trainers/add', methods=['GET', 'POST'])
def add_trainer():
    if request.method == 'POST':
        # Handle form submission to add a new trainer
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        specialization = request.form.get('specialization')
        contact_info = request.form.get('contact_info')

        # Execute SQL query to add the new trainer to the database
        query = "INSERT INTO Trainers (FirstName, LastName, Specialization, ContactInfo) VALUES (%s, %s, %s, %s)"
        values = (first_name, last_name, specialization, contact_info)
        execute_query(query, values)

        # Redirect to the trainers page after adding the trainer
        return redirect(url_for('trainer_management.trainers'))

    return render_template('add_trainer.html')


@trainer_management_routes.route('/trainers/<int:trainer_id>', methods=['GET'])
def view_trainer(trainer_id):
    query = "SELECT * FROM Trainers WHERE TrainerID = %s"
    trainer = execute_query(query, (trainer_id,), fetch_one=True)
    return render_template('view_trainer.html', trainer=trainer)


@trainer_management_routes.route('/trainers/<int:trainer_id>/edit', methods=['GET', 'POST'])
def edit_trainer(trainer_id):
    if request.method == 'POST':
        # Handle form submission to update trainer details
        specialization = request.form.get('specialization')
        contact_info = request.form.get('contact_info')

        # Execute SQL query to update the trainer's information
        query = "UPDATE Trainers SET Specialization = %s, ContactInfo = %s WHERE TrainerID = %s"
        values = (specialization, contact_info, trainer_id)
        execute_query(query, values)

        # Redirect to the trainer details page after updating
        return redirect(url_for('trainer_management.view_trainer', trainer_id=trainer_id))

    query = "SELECT * FROM Trainers WHERE TrainerID = %s"
    trainer = execute_query(query, (trainer_id,), fetch_one=True)
    return render_template('edit_trainer.html', trainer=trainer)


@trainer_management_routes.route('/trainers/<int:trainer_id>/delete', methods=['GET'])
def delete_trainer(trainer_id):
    # Execute SQL query to delete the trainer from the database
    query = "DELETE FROM Trainers WHERE TrainerID = %s"
    execute_query(query, (trainer_id,))

    # Redirect to the trainers page after deleting the trainer
    return redirect(url_for('trainer_management.trainers'))


@trainer_management_routes.route('/trainers/<int:trainer_id>/personal_training', methods=['GET'])
def view_personal_training(trainer_id):
    # Query personal training sessions for the specified trainer with member details
    query = """
        SELECT pt.MemberID, m.FirstName, m.LastName
        FROM PersonalTraining pt
        JOIN Members m ON pt.MemberID = m.MemberID
        WHERE pt.TrainerID = %s
    """
    personal_training_sessions = execute_query(query, (trainer_id,))

    return render_template('view_personal_training.html', trainer_id=trainer_id, personal_training_sessions=personal_training_sessions)


# trainer_management.py
# Existing routes...

@trainer_management_routes.route('/trainers/<int:trainer_id>/personal_training/add', methods=['GET', 'POST'])
def add_personal_training(trainer_id):
    if request.method == 'POST':
        # Handle form submission to add a new personal training session
        member_id = request.form.get('member_id')

        # Execute SQL query to add the new personal training session to the database
        query = "INSERT INTO PersonalTraining (MemberID, TrainerID) VALUES (%s, %s)"
        values = (member_id, trainer_id)
        execute_query(query, values)

        # Redirect to the personal training sessions page after adding the session
        return redirect(url_for('trainer_management.view_personal_training', trainer_id=trainer_id))

    # Fetch the list of members to populate the dropdown
    members_query = "SELECT MemberID, CONCAT(FirstName, ' ', LastName) AS MemberName FROM Members"
    members = execute_query(members_query)

    return render_template('add_personal_training.html', trainer_id=trainer_id, members=members)
