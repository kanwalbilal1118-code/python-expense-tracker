# 💰 Python Expense Tracker

A Python-based expense tracking and budget management application with a command-line interface, CSV data storage, automated expense analysis, unit testing, and an interactive Streamlit dashboard.

---

## 📌 Project Overview

The Python Expense Tracker is a practical expense management application that allows users to record, analyze, and manage their expenses.

The application can:

- Manage a monthly budget
- Add multiple expenses
- Store expense information using CSV files
- Calculate spending statistics
- Analyze spending by category
- Identify the highest spending category
- Identify the highest individual expense
- Calculate remaining budget
- Detect when the budget is exceeded
- Provide budget alerts
- Generate spending insights
- Maintain expense data between program runs
- Start a new month with a new budget
- Clear previous month's expenses when starting a new month
- Display financial information through a Streamlit dashboard
- Run automated unit tests

The project is organized into separate Python modules to keep the application maintainable and easy to understand.

---

## 🚀 Features

### Expense Management

- Add multiple expenses
- Store expense amount, category, and description
- Validate expense amounts
- Prevent empty categories
- Prevent empty descriptions
- Load previously saved expenses
- Save expenses to CSV

### Monthly Budget Management

- Set a monthly budget
- Automatically load the existing monthly budget
- Continue using the current month's budget
- Start a new month
- Set a new monthly budget
- Clear previous month's expenses when starting a new month
- Calculate remaining budget
- Detect budget overuse

### Expense Analysis

- Calculate total expenses
- Calculate average expense
- Count the number of expenses
- Calculate category totals
- Calculate spending percentages
- Identify the highest spending category
- Identify the highest individual expense
- Generate spending insights

### Budget Alerts

The application provides feedback based on budget usage.

Examples include:

- Spending under control
- Warning when spending approaches the budget
- Alert when the budget is exceeded

### Dashboard

The Streamlit dashboard provides:

- Monthly budget
- Total expenses
- Remaining budget
- Number of expenses
- Budget status
- Budget usage progress
- Category spending
- Spending percentages
- Spending charts
- Spending insights
- Highest spending category
- Highest individual expense
- Expense history
- Add Expense functionality
- Start New Month functionality
- Dashboard refresh functionality

---

## 🛠️ Technologies Used

- Python
- CSV
- File Handling
- Streamlit
- Pandas
- unittest
- Git
- GitHub

---

## 🧠 Python Concepts Applied

This project applies the following Python concepts:

- Variables
- Data types
- User input and output
- Conditional statements
- `if`, `elif`, and `else`
- `for` loops
- `while` loops
- Lists
- Dictionaries
- Functions
- String methods
- String formatting
- Arithmetic operations
- File handling
- CSV reading and writing
- Exception handling
- Data processing
- Modular programming
- Unit testing
- Importing modules

---

## 📊 Dashboard

The project includes an interactive Streamlit dashboard designed to make expense information easier to understand.

The dashboard provides:

### Financial Overview

- Monthly budget
- Total expenses
- Remaining budget
- Number of expenses

### Budget Monitoring

- Budget status
- Budget usage percentage
- Visual budget progress
- Budget exceeded warnings

### Spending Analysis

- Category totals
- Spending percentages
- Spending chart
- Highest spending category
- Highest individual expense
- Spending insights

### Expense Management

The dashboard also allows users to:

- Add new expenses
- Start a new month
- Set a new monthly budget
- Clear the previous month's expenses
- Refresh dashboard data

---

## 📂 Project Structure

```text
expense-tracker/
│
├── data/
│   ├── expenses.csv
│   ├── budget.csv
│   └── summary.csv
│
├── src/
│   ├── main.py
│   ├── expense_manager.py
│   ├── analyzer.py
│   └── file_manager.py
│
├── dashboard/
│   └── app.py
│
├── tests/
│   └── test_expense_manager.py
│
├── README.md
├── requirements.txt
└── .gitignore

Folder and File Description
File / Folder	Purpose
data/	Stores application data and reports
expenses.csv	Stores recorded expenses
budget.csv	Stores the current monthly budget
summary.csv	Stores expense summary information
src/main.py	Runs the command-line application
src/expense_manager.py	Handles expense input and management
src/analyzer.py	Performs expense calculations and analysis
src/file_manager.py	Handles CSV file operations and budget storage
dashboard/app.py	Provides the interactive Streamlit dashboard
tests/	Contains automated unit tests
test_expense_manager.py	Tests important expense analysis functionality
requirements.txt	Lists required external Python packages
.gitignore	Specifies files Git should ignore
README.md	Project documentation
💾 Data Storage

The application uses CSV files for persistent data storage.

Expense Data

Expense information is stored in:

data/expenses.csv

The file contains:

Amount,Category,Description

Example:

250.00,food,lunch
100.00,transport,bus fare
500.00,shopping,shoes
Budget Data

The current monthly budget is stored in:

data/budget.csv

Example:

Month,Budget
2026-08,50000.00
Summary Data

A summary report is stored in:

data/summary.csv

The summary can contain information such as:

Total budget
Total expenses
Number of expenses
Average expense
Remaining budget
Highest spending category
Highest category amount
Highest individual expense
Highest expense category
Highest expense description

Using CSV files allows the application to preserve data between program runs.

📅 Monthly Budget Management

The application supports multiple monthly budget cycles.

When the application is started, the user can choose whether to:

1. Continue current month
2. Start a new month
Continue Current Month

The existing monthly budget and expenses are loaded.

The user can continue adding expenses without entering the budget again.

Start New Month

The user can enter a new monthly budget.

The previous month's expenses are cleared and the new month starts with an empty expense list.

Example:

Starting a new month...
Enter your new monthly budget: 40000


New monthly budget saved: 40000.00
Previous month's expenses have been cleared.

This allows the application to be reused month after month.

▶️ How to Run
1. Open the Project

Open the expense-tracker folder in Visual Studio Code.

2. Install Dependencies

Open the terminal and run:

pip install -r requirements.txt
3. Run the Command-Line Application

Run:

python src/main.py

The application allows you to manage your monthly budget and add expenses.

4. Run the Dashboard

Launch the Streamlit dashboard using:

streamlit run dashboard/app.py

The dashboard will open in your web browser.

📦 Requirements

The main external packages used by the dashboard are:

Streamlit
Pandas

They are listed in:

requirements.txt

Install them with:

pip install -r requirements.txt
🧪 Testing

The project includes automated unit tests for important expense analysis functionality.

The tests verify functionality such as:

Total expense calculation
Average expense calculation
Number of expenses
Empty expense handling
Category totals
Highest spending category
Highest individual expense
Budget exceeded status
Budget within limit status

Run the complete test suite using:

python -m unittest discover -s tests -v

Example successful output:

Ran 9 tests


OK
🛡️ Input Validation

The application validates user input to prevent common errors.

Examples include:

Preventing invalid expense amounts
Preventing negative expense amounts
Preventing invalid budgets
Preventing empty categories
Preventing empty descriptions
Validating yes/no responses
Handling missing CSV files

For example:

Enter the expense amount: abc

The application handles invalid input instead of allowing the program to crash.

📈 Expense Analysis

The application analyzes recorded expenses and calculates several useful metrics.

Total Expense

The total amount spent across all recorded expenses.

Average Expense

The average amount spent per expense.

Category Totals

The total amount spent within each category.

Spending Breakdown

The percentage of total spending represented by each category.

Highest Spending Category

The category with the highest total spending.

Highest Individual Expense

The single expense with the highest amount.

Budget Status

The application compares total spending with the monthly budget and reports whether spending is:

Within budget
Approaching the budget limit
Over budget
🚨 Budget Alerts

The application provides different messages depending on budget usage.

For example:

Budget Usage: 50%
Your spending is under control.

When spending approaches the budget:

WARNING: You have used 90% of your budget!
Remaining Budget: 100.00

When spending exceeds the budget:

ALERT: Your budget has been exceeded!


Budget Usage: 110%
Amount Over Budget: 100.00
💡 Spending Insights

The application generates simple insights based on spending patterns.

For example:

food is your largest spending area, using 75.3% of your total spending.

These insights help users quickly understand where most of their money is being spent.

🔮 Future Improvements

Possible future improvements include:

Monthly historical reports
Expense search and filtering
Expense editing
Expense deletion
Date-based expense tracking
More advanced dashboard visualizations
Exporting reports in additional formats
Automated scheduled reports
More advanced financial insights
Linux-based automation
Database integration
User authentication
🎯 Learning Purpose

This project was created to apply Python programming concepts to a practical automation problem.

Instead of learning Python concepts individually, the project combines them into a complete application:

User Input
     ↓
Data Processing
     ↓
Expense Storage
     ↓
Calculations
     ↓
Analysis
     ↓
Budget Monitoring
     ↓
Reports
     ↓
Dashboard

The project demonstrates how Python programming, file handling, modular design, testing, and a web dashboard can be combined to build a practical real-world application.

👩‍💻 Author

Developed as a Python learning and automation project.

📄 License

This project is created for educational and portfolio purposes.