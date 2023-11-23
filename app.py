from flask import Flask, render_template
from member_management import member_management_routes
from trainer_management import trainer_management_routes
from db_config import execute_query
from class_management import class_management_routes
from attendance_management import attendance_maintenance_routes
from dashboard import dashboard_routes
# Import other modules for different features

app = Flask(__name__)

# Register routes from other modules
app.register_blueprint(dashboard_routes)

app.register_blueprint(member_management_routes)

app.register_blueprint(trainer_management_routes)

app.register_blueprint(class_management_routes)

app.register_blueprint(attendance_maintenance_routes)




if __name__ == '__main__':
    app.run(debug=True)
