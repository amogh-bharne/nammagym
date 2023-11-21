from flask import Flask, render_template
from member_management import member_management_routes
from trainer_management import trainer_management_routes
from db_config import execute_query
# Import other modules for different features

app = Flask(__name__)

# Register routes from other modules
app.register_blueprint(member_management_routes)
app.register_blueprint(trainer_management_routes)

# Register other blueprints for different features


@app.route('/dashboard', methods=['GET'])
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


if __name__ == '__main__':
    app.run(debug=True)
