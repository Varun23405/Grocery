import mysql.connector

__cnx = None  # Global connection variable

def get_sql_connection():
    global __cnx

    if __cnx is None or not __cnx.is_connected():
        try:
            print("Opening MySQL connection...")
            __cnx = mysql.connector.connect(
                host='localhost',         # Specify the host
                user='root',              # Your MySQL username
                password='Kjnv1506@',     # Your MySQL password
                database='grocery'        # Your database name
            )
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None

    return __cnx  # Return the global connection
