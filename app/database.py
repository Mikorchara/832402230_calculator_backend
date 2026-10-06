import sqlite3


DATABASE_PATH = "calculator.db"


def init_database():
    connection = sqlite3.connect(DATABASE_PATH)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            expression TEXT NOT NULL,
            result REAL NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()

def add_history(expression: str, result: float):
    connection = sqlite3.connect(DATABASE_PATH)

    connection.execute(
        "INSERT INTO history (expression, result) VALUES (?, ?)",
        (expression, result)
    )

    connection.commit()
    connection.close()

def get_history():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row

    rows = connection.execute(
        "SELECT * FROM history ORDER BY id DESC"
    ).fetchall()

    connection.close()

    return [dict(row) for row in rows]

def delete_history(history_id: int):
    connection = sqlite3.connect(DATABASE_PATH)

    cursor = connection.execute(
        "DELETE FROM history WHERE id = ?",
        (history_id,)
    )

    connection.commit()

    deleted = cursor.rowcount > 0

    connection.close()

    return deleted