# invoices_management.py
from flask import Blueprint, render_template, redirect, url_for, request, make_response
from db_config import execute_query
import pdfkit
from flask import send_file

invoices_management_routes = Blueprint('invoices_management', __name__)

# Route to display invoices
@invoices_management_routes.route('/invoices', methods=['GET'])
def display_invoices():
    query = "SELECT * FROM Invoices"
    invoices = execute_query(query)
    return render_template('invoices.html', invoices=invoices)

# Route to add an invoice
@invoices_management_routes.route('/invoices/add', methods=['GET', 'POST'])
def add_invoice():
    if request.method == 'POST':
        member_id = request.form.get('member_id')
        issue_date = request.form.get('issue_date')
        due_date = request.form.get('due_date')
        total_amount = request.form.get('total_amount')

        query = """
            INSERT INTO Invoices (MemberID, IssueDate, DueDate, TotalAmount)
            VALUES (%s, %s, %s, %s)
        """
        values = (member_id, issue_date, due_date, total_amount)
        execute_query(query, values)

        return redirect(url_for('invoices_management.display_invoices'))

    # Fetch members to populate the dropdown
    members_query = "SELECT MemberID, CONCAT(FirstName, ' ', LastName) AS MemberName FROM Members"
    members = execute_query(members_query)
    
    return render_template('add_invoice.html', members=members)

# Route to edit an invoice
@invoices_management_routes.route('/invoices/edit/<int:invoice_id>', methods=['GET', 'POST'])
def edit_invoice(invoice_id):
    if request.method == 'POST':
        # Handle form submission to update invoice details
        member_id = request.form.get('member_id')
        issue_date = request.form.get('issue_date')
        due_date = request.form.get('due_date')
        total_amount = request.form.get('total_amount')

        query = """
            UPDATE Invoices
            SET MemberID = %s, IssueDate = %s, DueDate = %s, TotalAmount = %s
            WHERE InvoiceID = %s
        """
        values = (member_id, issue_date, due_date, total_amount, invoice_id)
        execute_query(query, values)

        return redirect(url_for('invoices_management.display_invoices'))

    # Fetch the invoice details
    invoice_query = "SELECT * FROM Invoices WHERE InvoiceID = %s"
    invoice = execute_query(invoice_query, (invoice_id,), fetch_one=True)

    # Fetch members to populate the dropdown
    members_query = "SELECT MemberID, CONCAT(FirstName, ' ', LastName) AS MemberName FROM Members"
    members = execute_query(members_query)

    return render_template('edit_invoice.html', invoice=invoice, members=members)

# Route to delete an invoice
@invoices_management_routes.route('/invoices/delete/<int:invoice_id>', methods=['POST'])
def delete_invoice(invoice_id):
    if request.method == 'POST':
        delete_query = "DELETE FROM Invoices WHERE InvoiceID = %s"
        execute_query(delete_query, (invoice_id,))

        return redirect(url_for('invoices_management.display_invoices'))
    


def get_invoice_data(invoice_id):
    query = f"SELECT * FROM Invoices WHERE InvoiceID = {invoice_id}"
    # Assuming your query returns a single row for the given invoice_id
    result = execute_query(query)

    # Adjust this according to your database columns
    invoice = {
        'InvoiceID': result[0]['InvoiceID'],
        'MemberID': result[0]['MemberID'],
        'IssueDate': str(result[0]['IssueDate']),
        'DueDate': str(result[0]['DueDate']),
        'TotalAmount': result[0]['TotalAmount'],
        # Add other relevant data for the invoice
    }
    return invoice



