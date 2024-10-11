import mysql.connector as mysql
from mysql.connector import Error
from pathlib import Path
import sys
from Connect import create_database_connection

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the path to the folder containing SQL files.")
        sys.exit(1)

    folder_path = Path(sys.argv[1])
    queries = list(folder_path.glob('*.sql')) 

    if not queries:
        print("No SQL files found")
        sys.exit(1)

    connection = create_database_connection()
    cursor = connection.cursor()

    for query_file in queries:
        print(f"Running {query_file}")
        try:
            query = query_file.read_text()
            
            for result in cursor.execute(query, multi=True):
                if result.with_rows:
                    print(result.statement)
                    print(result.fetchall())
        except Error as e:
            print(f"Error executing query in {query_file}: {e}")

    cursor.close()
    connection.close()