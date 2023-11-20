import mysql.connector

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '123450',
    'database': 'nammagym'
}


def execute_query(query, values=None, fetch_one=False):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute(query, values)
        result = cursor.fetchone() if fetch_one else cursor.fetchall()
        connection.commit()
        return result
    finally:
        cursor.close()
        connection.close()
