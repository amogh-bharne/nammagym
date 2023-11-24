# invoices_management.py
from flask import make_response, send_file
from flask import Blueprint, render_template, redirect, url_for, request, make_response
from db_config import execute_query
from flask import send_file
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

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
    invoice_query = """
        SELECT Invoices.InvoiceID, Members.MemberID, CONCAT(Members.FirstName, ' ', Members.LastName) AS MemberName, 
            Invoices.IssueDate, Invoices.DueDate, Invoices.TotalAmount
        FROM Invoices
        JOIN Members ON Invoices.MemberID = Members.MemberID
        WHERE Invoices.InvoiceID = %s
    """
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
    




@invoices_management_routes.route('/invoices/download/<int:invoice_id>', methods=['GET'])
def download_invoice(invoice_id):
    # Fetch the invoice details
    invoice_query = """
        SELECT Invoices.InvoiceID, Members.MemberID, CONCAT(Members.FirstName, ' ', Members.LastName) AS MemberName, 
            Members.Address, Members.ContactInfo,
            Invoices.IssueDate, Invoices.DueDate, Invoices.TotalAmount
        FROM Invoices
        JOIN Members ON Invoices.MemberID = Members.MemberID
        WHERE Invoices.InvoiceID = %s
    """
    invoice = execute_query(invoice_query, (invoice_id,), fetch_one=True)

    # Create PDF buffer
    pdf_buffer = BytesIO()

    # Create PDF document
    pdf = SimpleDocTemplate(pdf_buffer, pagesize=letter)

    # Define data for the table
    table_data = [
        ['Invoice for', invoice['MemberName']],
        ['Member Address', invoice['Address']],
        ['Member Contact Info', invoice['ContactInfo']],
        ['Issue Date', str(invoice['IssueDate'])],
        ['Due Date', str(invoice['DueDate'])],
        ['Total Amount', str(invoice['TotalAmount'])],
    ]

    # Create table and set style
    table = Table(table_data, colWidths=[200, 200], rowHeights=30)
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ])

    table.setStyle(style)

    # Build the PDF document
    pdf.build([table])

    # Move the buffer's position to the beginning
    pdf_buffer.seek(0)

    # Create a response and set the appropriate headers for a PDF file
    response = make_response(send_file(
        pdf_buffer, as_attachment=True, download_name=f"Invoice_{invoice_id}.pdf"))
    response.headers['Content-Type'] = 'application/pdf'

    return response
