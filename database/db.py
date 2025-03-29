import sqlite3

def connect_db(db_file="budgetmanager.db"):
    conn = sqlite3.connect(db_file)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def execute_query(query, params=(), commit=False, fetch_one=False, fetch_all=False):
    with connect_db() as conn:
        cursor = conn.execute(query, params)
        result = None
        if fetch_one:
            result = cursor.fetchone()
        elif fetch_all:
            result = cursor.fetchall()
        if commit:
            conn.commit()
            result = cursor.rowcount
        return result

def create_tables():
    # Create users table
    users_table_query = """--sql
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        firstname TEXT,
        lastname TEXT
    )
    """
    execute_query(users_table_query, commit=True)
    
    # Create budget table
    budget_table_query = """--sql
    CREATE TABLE IF NOT EXISTS budgets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        month TEXT NOT NULL,
        income REAL NOT NULL,
        savings_percent REAL NOT NULL,
        rent_percent REAL NOT NULL,
        electricity_percent REAL NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
        UNIQUE(user_id, month)
    )
    """

    execute_query(budget_table_query, commit=True)

# Initialize the database when the module is imported
create_tables()