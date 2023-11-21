# member_management.py
from flask import Blueprint, render_template, redirect, url_for, request
from db_config import execute_query

member_management_routes = Blueprint('member_management', __name__)


@member_management_routes.route('/members', methods=['GET'])
def member_management():
    query = "SELECT * FROM Members"
    members = execute_query(query)
    return render_template('member_management.html', members=members)


@member_management_routes.route('/members/add', methods=['POST'])
def add_member():
    # Handle form submission to add a new member
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        date_of_birth = request.form.get('dob')
        contact_info = request.form.get('contact_info')
        address = request.form.get('address')
        membership_start = request.form.get('membership_start')
        membership_expiry = request.form.get('membership_expiry')

        # Insert the new member into the database
        query = """
            INSERT INTO Members (FirstName, LastName, DateOfBirth, ContactInfo, Address, MembershipStart, MembershipExpiry)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = (first_name, last_name, date_of_birth, contact_info,
                  address, membership_start, membership_expiry)
        execute_query(query, values)

    # Redirect to the members page after adding the member
    return redirect(url_for('member_management.member_management'))


# member_management.py

# ... (existing code)
# member_management.py

# ... (existing code)

@member_management_routes.route('/members/<int:member_id>', methods=['GET', 'POST'])
def view_member(member_id):
    if request.method == 'POST':
        # Handle form submission for member details update
        updated_first_name = request.form.get('updated_first_name')
        updated_last_name = request.form.get('updated_last_name')
        updated_dob = request.form.get('updated_dob')
        updated_contact_info = request.form.get('updated_contact_info')
        updated_address = request.form.get('updated_address')
        updated_membership_start = request.form.get('updated_membership_start')
        updated_membership_expiry = request.form.get(
            'updated_membership_expiry')

        # Extract and update other member details based on the form inputs
        query = """
            UPDATE Members
            SET FirstName = %s, LastName = %s, DateOfBirth = %s, ContactInfo = %s, Address = %s,
                MembershipStart = %s, MembershipExpiry = %s
            WHERE MemberID = %s
        """
        values = (
            updated_first_name, updated_last_name, updated_dob, updated_contact_info, updated_address,
            updated_membership_start, updated_membership_expiry, member_id
        )
        execute_query(query, values)

        # Redirect to the members page after updating the member
        return redirect(url_for('member_management.member_management'))

    # Fetch member details
    member_query = "SELECT * FROM Members WHERE MemberID = %s"
    member = execute_query(member_query, (member_id,), fetch_one=True)

    # Fetch personal trainer details for the member
    pt_query = """
    SELECT PersonalTraining.MemberID, Trainers.TrainerID, Trainers.FirstName AS TrainerFirstName, Trainers.LastName AS TrainerLastName
    FROM PersonalTraining
    JOIN Trainers ON PersonalTraining.TrainerID = Trainers.TrainerID
    WHERE PersonalTraining.MemberID = %s
    """
    personal_trainer = execute_query(pt_query, (member_id,), fetch_one=True)

    # Render the member details template
    return render_template('member_details.html', member=member, personal_trainer=personal_trainer)




# Delete route for members
@member_management_routes.route('/members/delete/<int:member_id>', methods=['POST'])
def delete_member(member_id):
    if request.method == 'POST':
        # Execute SQL DELETE query to remove member by MemberID
        delete_query = "DELETE FROM Members WHERE MemberID = %s"
        execute_query(delete_query, (member_id,))
        
        # Redirect to the members page after deletion
        return redirect(url_for('member_management.member_management'))


