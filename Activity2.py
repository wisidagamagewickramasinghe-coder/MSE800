import sqlite3

DB_NAME = "w6_a1_students.db"

def create_table(conn: sqlite3.Connection):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS Student (
            student_id   INTEGER PRIMARY KEY,
            student_name TEXT NOT NULL,
            score        INTEGER NOT NULL,
            email        TEXT
        )
    """)
    conn.commit()

def seed_data(conn: sqlite3.Connection):
    # Example data (you can replace these with your W6-A1 inputs)
    keys  = [1, 2, 3, 4, 5]
    names = ["Alex", "Anne", "Andrew", "Adriel", "Hiruni"]
    marks = ["60", "70", "95", "80", "40"]  # strings -> will convert to int

    students = []
    for sid, name, mark in zip(keys, names, marks):
        students.append((sid, name, int(mark), f"{name.lower()}@example.com"))

    # Insert (or update if same student_id already exists)
    conn.executemany("""
        INSERT INTO Student(student_id, student_name, score, email)
        VALUES(?, ?, ?, ?)
        ON CONFLICT(student_id) DO UPDATE SET
            student_name = excluded.student_name,
            score        = excluded.score,
            email        = excluded.email
    """, students)
    conn.commit()

def get_top_3_students(conn: sqlite3.Connection):
    cursor = conn.execute("""
        SELECT student_id, student_name, score
        FROM Student
        ORDER BY score DESC
        LIMIT 3
    """)
    return cursor.fetchall()

def main():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row

    create_table(conn)
    seed_data(conn)

    top3 = get_top_3_students(conn)

  
    for row in top3:
        print(f"ID: {row['student_id']} | Name: {row['student_name']} | Score: {row['score']}")

    conn.close()

if __name__ == "__main__":
    main()
