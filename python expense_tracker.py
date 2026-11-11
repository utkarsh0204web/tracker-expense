"""Simple Expense Tracker - Python + SQLite (console app)."""
import sqlite3
from datetime import date

DB_NAME = "expenses.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.execute(
        """CREATE TABLE IF NOT EXISTS expenses (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               date TEXT NOT NULL,
               category TEXT NOT NULL,
               amount REAL NOT NULL,
               note TEXT
           )"""
    )
    return conn


def add_expense(conn):
    category = input("Category (food, travel, books...): ").strip().lower()
    try:
        amount = float(input("Amount (Rs): "))
    except ValueError:
        print("Please enter a valid number.")
        return
    note = input("Note (optional): ").strip()
    conn.execute(
        "INSERT INTO expenses (date, category, amount, note) VALUES (?, ?, ?, ?)",
        (date.today().isoformat(), category, amount, note),
    )
    conn.commit()
    print("Expense saved.")


def view_expenses(conn):
    rows = conn.execute(
        "SELECT id, date, category, amount, note FROM expenses ORDER BY date DESC"
    ).fetchall()
    if not rows:
        print("No expenses yet.")
        return
    print(f"\n{'ID':<4}{'Date':<12}{'Category':<12}{'Amount':>10}  Note")
    for r in rows:
        print(f"{r[0]:<4}{r[1]:<12}{r[2]:<12}{r[3]:>10.2f}  {r[4] or ''}")


def delete_expense(conn):
    try:
        expense_id = int(input("Enter the ID to delete: "))
    except ValueError:
        print("Please enter a valid ID.")
        return
    cur = conn.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    print("Deleted." if cur.rowcount else "No expense with that ID.")


def summary(conn):
    total = conn.execute("SELECT COALESCE(SUM(amount), 0) FROM expenses").fetchone()[0]
    print(f"\nTotal spent: Rs {total:.2f}")
    rows = conn.execute(
        "SELECT category, SUM(amount) FROM expenses GROUP BY category ORDER BY 2 DESC"
    ).fetchall()
    for category, amount in rows:
        print(f"  {category:<12} Rs {amount:.2f}")


def main():
    conn = get_connection()
    actions = {
        "1": add_expense,
        "2": view_expenses,
        "3": delete_expense,
        "4": summary,
    }
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Delete expense")
        print("4. Summary by category")
        print("5. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "5":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action:
            action(conn)
        else:
            print("Invalid choice, try again.")
    conn.close()


if __name__ == "__main__":
    main()