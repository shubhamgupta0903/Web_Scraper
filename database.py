import mysql.connector
from mysql.connector import Error

def create_connection():
    """
    Create a connection to the MySQL database.
    
    Returns:
        connection (mysql.connector.connection.MySQLConnection): The MySQL database connection object.
    """
    try:
        # Replace the placeholder values with your actual database credentials
        connection = mysql.connector.connect(
        host='your_host',              # Change 'your_host' to your database host, e.g., '127.0.0.1'
        port='your_port',              # Change 'your_port' to your database port, e.g., 3306
        user='your_username',          # Change 'your_username' to your database username
        password='your_password',      # Change 'your_password' to your database password
        database='internship_project'  # Don't change database name
    )
        if connection.is_connected():
            print("Connection to MySQL DB successful")
        return connection
    except Error as e:
        print(f"The error '{e}' occurred")
        return None

def execute_query(connection, query, data=None):
    """
    Execute a SQL query on the MySQL database.
    
    Args:
        connection (mysql.connector.connection.MySQLConnection): The MySQL database connection object.
        query (str): The SQL query to be executed.
        data (tuple, optional): The data to be used with the query (for parameterized queries).
    """
    cursor = connection.cursor()
    try:
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

