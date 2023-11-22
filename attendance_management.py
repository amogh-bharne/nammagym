# Import necessary modules and classes
from flask import Blueprint, render_template, redirect, url_for, request
from db_config import execute_query

attendance_maintenance_routes = Blueprint('attendance_maintenance', __name__)


@attendance_maintenance_routes.route('/attendance', methods=['GET'])
def view_attendance():
    query = """
    SELECT Attendance.AttendanceID, Members.FirstName, Members.LastName, Classes.ClassName, Attendance.AttendanceDate, Attendance.AttendanceStatus
    FROM Attendance
    JOIN Members ON Attendance.MemberID = Members.MemberID
    JOIN Classes ON Attendance.ClassID = Classes.ClassID
    """
    attendance_records = execute_query(query)
    return render_template('attendance.html', attendance_records=attendance_records)


@attendance_maintenance_routes.route('/attendance/add', methods=['GET', 'POST'])
def add_attendance():
    if request.method == 'POST':
        member_id = request.form.get('member_id')
        class_id = request.form.get('class_id')
        attendance_date = request.form.get('attendance_date')
        attendance_status = request.form.get('attendance_status')

        query = """
        INSERT INTO Attendance (MemberID, ClassID, AttendanceDate, AttendanceStatus)
        VALUES (%s, %s, %s, %s)
        """
        values = (member_id, class_id, attendance_date, attendance_status)
        execute_query(query, values)

        return redirect(url_for('attendance_maintenance.view_attendance'))

    # Fetch members and classes data for dropdowns
    members_query = "SELECT MemberID, CONCAT(FirstName, ' ', LastName) AS FullName FROM Members"
    classes_query = "SELECT ClassID, ClassName FROM Classes"
    members = execute_query(members_query)
    classes = execute_query(classes_query)

    return render_template('add_attendance.html', members=members, classes=classes)


@attendance_maintenance_routes.route('/attendance/edit/<int:attendance_id>', methods=['GET', 'POST'])
def edit_attendance(attendance_id):
    if request.method == 'POST':
        attendance_status = request.form.get('attendance_status')

        query = "UPDATE Attendance SET AttendanceStatus = %s WHERE AttendanceID = %s"
        values = (attendance_status, attendance_id)
        execute_query(query, values)

        return redirect(url_for('attendance_maintenance.view_attendance'))

    query = """
    SELECT Attendance.AttendanceID, Members.FirstName, Members.LastName, Classes.ClassName, Attendance.AttendanceDate, Attendance.AttendanceStatus
    FROM Attendance
    JOIN Members ON Attendance.MemberID = Members.MemberID
    JOIN Classes ON Attendance.ClassID = Classes.ClassID
    WHERE Attendance.AttendanceID = %s
    """
    attendance_record = execute_query(query, (attendance_id,), fetch_one=True)

    return render_template('edit_attendance.html', attendance_record=attendance_record)


@attendance_maintenance_routes.route('/attendance/delete/<int:attendance_id>', methods=['POST'])
def delete_attendance(attendance_id):
    if request.method == 'POST':
        query = "DELETE FROM Attendance WHERE AttendanceID = %s"
        execute_query(query, (attendance_id,))
        
        return redirect(url_for('attendance_maintenance.view_attendance'))
