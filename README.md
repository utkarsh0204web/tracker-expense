# Expense Tracker

A simple expense tracker built with Python and SQLite. It lets you record daily expenses, view them in a table, delete entries and see how much you have spent in each category.

## Features

- Add an expense with category, amount and note (today's date is saved automatically)
- View all expenses, newest first
- Delete an expense by its ID
- Summary of total spending and spending per category
- Data is stored in a local SQLite database (`expenses.db`), so it is saved between runs

## Tech Stack

- Python 3
- SQLite (`sqlite3` module)

## How to Run

1. Install [Python 3](https://www.python.org/downloads/)
2. Clone this repository:
   ```
   git clone https://github.com/utkarsh0204web/tracker-expense.git
   cd tracker-expense
   ```
3. Run the program:
   ```
   python expense_tracker.py
   ```
4. Choose an option from the menu by typing its number.

No extra libraries are needed.

## Project Structure

```
tracker-expense/
├── expense_tracker.py   # main program
├── .gitignore           # keeps the local database out of Git
└── README.md
```

## Future Improvements

- Web interface using Streamlit
- Monthly reports and budget alerts
- Export expenses to CSV
- Edit existing expenses

## Author

Utkarsh Gupta, B.Tech CSE student, Sharda University
GitHub: [utkarsh0204web](https://github.com/utkarsh0204web)
