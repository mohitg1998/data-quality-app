import pyodbc
import os

server = os.getenv("SQL_SERVER_HOST", "localhost")
port = os.getenv("SQL_SERVER_PORT", "1433")
username = os.getenv("SQL_SERVER_USER", "sa")
password = os.getenv("SQL_SERVER_PASSWORD", "YourStrong!Passw0rd")


def get_sqlserver_connection(database=None):
    """
    Returns a connection to the local SQL Server instance.
    Uses Windows Authentication.
    
    Parameters:
    - database_name (str): Optional. If provided, connects to that specific database.
    """
    # server = "MOHIT\SQLEXPRESS"  # Adjust if your instance name is different
    driver = "ODBC Driver 17 for SQL Server"  # Make sure this is installed

    if database:
        conn_str = (
            f"DRIVER={{{driver}}};"
            f"SERVER={server};"
            f"DATABASE={database};"
            f"UID={username};"
            f"PWD={password}"
            # "Trusted_Connection=yes;"
        )
    else:
        # Default to master if no DB specified
        conn_str = (
            f"DRIVER={{{driver}}};"
            f"SERVER={server};"
            "DATABASE=master;"
            f"UID={username};"
            f"PWD={password}"
            # "Trusted_Connection=yes;"
        )

    return pyodbc.connect(conn_str)
