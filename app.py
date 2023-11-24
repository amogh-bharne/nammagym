from flask import Flask, render_template, request
from member_management import member_management_routes
from trainer_management import trainer_management_routes
from db_config import execute_query
from class_management import class_management_routes
from attendance_management import attendance_maintenance_routes
from dashboard import dashboard_routes
from payments_management import payments_management_routes
from invoices_management import invoices_management_routes
from equipment_management import equipment_management_routes

# Import other modules for different features

app = Flask(__name__)

# Register routes from other modules
app.register_blueprint(dashboard_routes)

app.register_blueprint(member_management_routes)

app.register_blueprint(trainer_management_routes)

app.register_blueprint(class_management_routes)

app.register_blueprint(attendance_maintenance_routes)

app.register_blueprint(payments_management_routes)

app.register_blueprint(invoices_management_routes)

app.register_blueprint(equipment_management_routes)


@app.route('/custom_query', methods=['GET', 'POST'])
def custom_query():
    if request.method == 'POST':
        # Get the user-entered query from the form
        user_query = request.form.get('user_query')

        # Execute the query
        result = execute_query(user_query)

        # Render the template with the query result
        return render_template('custom_query_result.html', user_query=user_query, result=result)

    # Render the custom query form
    return render_template('custom_query.html')


if __name__ == '__main__':
    app.run(debug=True)
