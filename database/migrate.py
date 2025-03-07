import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.constants import DATABASE_PORT, DATABASE_HOST, DATABASE_NAME, DATABASE_PASSWORD, DATABASE_USERNAME
from database.connection import connect_to_redshift

def run_migrations():
    conn = connect_to_redshift(DATABASE_HOST, DATABASE_PORT, DATABASE_NAME, DATABASE_USERNAME, DATABASE_PASSWORD)
    cur = conn.cursor()
    
    MIGRATION_FILE = [
    "../database/migrations/create_dim_table.sql",
    "../database/migrations/create_fact_salesOrder.sql"
    ]
    
    for file in MIGRATION_FILE:
        with open(file, "r") as f:
            cur.execute(f.read())
        conn.commit()
    cur.close()
    conn.close()
    
if __name__ == "__main__":
    run_migrations()