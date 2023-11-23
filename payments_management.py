# Import necessary modules and classes
from flask import Blueprint, render_template, redirect, url_for, request
from db_config import execute_query

payments_management_routes = Blueprint('payments_management', __name__)

# Route for displaying payments
@payments_management_routes.route('/payments', methods=['GET'])
def payments():
    query = "SELECT * FROM Payments"
    payments = execute_query(query)
    return render_template('payments.html', payments=payments)

# Route for adding a payment
@payments_management_routes.route('/payments/add', methods=['GET', 'POST'])
def add_payment():
    if request.method == 'POST':
        member_id = request.form.get('member_id')
        payment_date = request.form.get('payment_date')
        amount = request.form.get('amount')
        payment_method = request.form.get('payment_method')

        query = "INSERT INTO Payments (MemberID, PaymentDate, Amount, PaymentMethod) VALUES (%s, %s, %s, %s)"
        values = (member_id, payment_date, amount, payment_method)
        execute_query(query, values)

        return redirect(url_for('payments_management.payments'))

    # Fetch members to populate dropdown
    members_query = "SELECT MemberID, CONCAT(FirstName, ' ', LastName) AS MemberName FROM Members"
    members = execute_query(members_query)

    return render_template('add_payment.html', members=members)

# Route for editing a payment
@payments_management_routes.route('/payments/edit/<int:payment_id>', methods=['GET', 'POST'])
def edit_payment(payment_id):
    if request.method == 'POST':
        member_id = request.form.get('member_id')
        payment_date = request.form.get('payment_date')
        amount = request.form.get('amount')
        payment_method = request.form.get('payment_method')

        query = "UPDATE Payments SET MemberID = %s, PaymentDate = %s, Amount = %s, PaymentMethod = %s WHERE PaymentID = %s"
        values = (member_id, payment_date, amount, payment_method, payment_id)
        execute_query(query, values)

        return redirect(url_for('payments_management.payments'))

    # Fetch payment details
    payment_query = "SELECT * FROM Payments WHERE PaymentID = %s"
    payment = execute_query(payment_query, (payment_id,), fetch_one=True)

    # Fetch members to populate dropdown
    members_query = "SELECT MemberID, CONCAT(FirstName, ' ', LastName) AS MemberName FROM Members"
    members = execute_query(members_query)

    return render_template('edit_payment.html', payment=payment, members=members)

# Route for deleting a payment
@payments_management_routes.route('/payments/delete/<int:payment_id>', methods=['POST'])
def delete_payment(payment_id):
    if request.method == 'POST':
        delete_query = "DELETE FROM Payments WHERE PaymentID = %s"
        execute_query(delete_query, (payment_id,))
    
    return redirect(url_for('payments_management.payments'))
