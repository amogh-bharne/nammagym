

from flask import Blueprint, render_template, redirect, url_for, request
from db_config import execute_query

dashboard_routes = Blueprint('dashboard', __name__)

@dashboard_routes.route('/', methods=['GET'])
def dashboard():
    # Query database for metrics
    total_members_query = "SELECT COUNT(*) AS total_members FROM Members"
    active_memberships_query = "SELECT COUNT(*) AS active_memberships FROM Members WHERE MembershipExpiry >= CURDATE()"
    upcoming_classes_query = "SELECT COUNT(*) AS upcoming_classes FROM Classes WHERE ScheduleDate >= CURDATE()"
    total_revenue_query = "SELECT SUM(Amount) AS total_revenue FROM Payments"
    pending_payments_query = "SELECT COUNT(*) AS pending_payments FROM Payments WHERE PaymentDate IS NULL"

    total_members = execute_query(total_members_query)[0]['total_members']
    active_memberships = execute_query(active_memberships_query)[
        0]['active_memberships']
    upcoming_classes = execute_query(upcoming_classes_query)[
        0]['upcoming_classes']
    total_revenue = execute_query(total_revenue_query)[0]['total_revenue']
    pending_payments = execute_query(pending_payments_query)[
        0]['pending_payments']

    # Render the dashboard template with the obtained metrics
    return render_template('dashboard.html', total_members=total_members, active_memberships=active_memberships,
                           upcoming_classes=upcoming_classes, total_revenue=total_revenue, pending_payments=pending_payments)



