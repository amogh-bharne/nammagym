# equipment_management.py
from flask import Blueprint, render_template, redirect, url_for, request
from db_config import execute_query

equipment_management_routes = Blueprint('equipment_management', __name__)


@equipment_management_routes.route('/equipment', methods=['GET'])
def equipment():
    query = "SELECT * FROM Equipment"
    equipment_list = execute_query(query)
    return render_template('equipment.html', equipment_list=equipment_list)


@equipment_management_routes.route('/equipment/add', methods=['GET', 'POST'])
def add_equipment():
    if request.method == 'POST':
        equipment_name = request.form['equipment_name']
        quantity_available = request.form['quantity_available']
        equipment_condition = request.form['equipment_condition']
        last_maintenance_date = request.form['last_maintenance_date']

        query = """
            INSERT INTO Equipment (EquipmentName, QuantityAvailable, EquipmentCondition, LastMaintenanceDate)
            VALUES (%s, %s, %s, %s)
        """
        values = (equipment_name, quantity_available, equipment_condition, last_maintenance_date)
        execute_query(query, values)

        return redirect(url_for('equipment_management.equipment'))

    return render_template('add_equipment.html')


@equipment_management_routes.route('/equipment/edit/<int:equipment_id>', methods=['GET', 'POST'])
def edit_equipment(equipment_id):
    if request.method == 'POST':
        equipment_name = request.form['equipment_name']
        quantity_available = request.form['quantity_available']
        equipment_condition = request.form['equipment_condition']
        last_maintenance_date = request.form['last_maintenance_date']

        query = """
            UPDATE Equipment
            SET EquipmentName = %s, QuantityAvailable = %s, EquipmentCondition = %s, LastMaintenanceDate = %s
            WHERE EquipmentID = %s
        """
        values = (equipment_name, quantity_available, equipment_condition, last_maintenance_date, equipment_id)
        execute_query(query, values)

        return redirect(url_for('equipment_management.equipment'))

    query = "SELECT * FROM Equipment WHERE EquipmentID = %s"
    equipment = execute_query(query, (equipment_id,), fetch_one=True)
    return render_template('edit_equipment.html', equipment=equipment)
