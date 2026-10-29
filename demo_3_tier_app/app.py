from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from pathlib import Path

app = Flask(__name__)
app.secret_key = "demo-secret-key-change-for-real-projects"

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "students.db"


# Tier 3: Database layer
def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL
            )
        """)


# Tier 2: Application / business logic
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()

        if not name or not email:
            flash("Please enter both name and email.")
            return redirect(url_for("index"))

        # Parameterized SQL helps avoid SQL injection.
        with get_connection() as connection:
            connection.execute(
                "INSERT INTO students (name, email) VALUES (?, ?)",
                (name, email)
            )
        flash("Student added successfully!")
        return redirect(url_for("index"))

    with get_connection() as connection:
        students = connection.execute(
            "SELECT id, name, email FROM students ORDER BY id DESC"
        ).fetchall()

    # Tier 1: Presentation layer is rendered by the HTML template.
    return render_template("index.html", students=students)


if __name__ == "__main__":
    init_db()
    # Demo server only. For a production deployment, use a production WSGI server.
    app.run(host="0.0.0.0", port=5000, debug=False)
