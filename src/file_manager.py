import csv


# ========================================
# LOAD EXPENSES FROM CSV
# ========================================

def load_expenses():

    expenses = []

    try:

        with open(
            "data/expenses.csv",
            mode="r",
            newline=""
        ) as file:

            reader = csv.reader(file)

            next(reader, None)

            for row in reader:

                if not row:
                    continue

                if len(row) < 3:
                    continue

                expense = {
                    "amount": float(row[0]),
                    "category": row[1].strip(),
                    "description": row[2].strip()
                }

                expenses.append(expense)

    except FileNotFoundError:

        pass

    return expenses


# ========================================
# SAVE EXPENSES TO CSV
# ========================================

def save_expenses(expenses):

    with open(
        "data/expenses.csv",
        mode="w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Amount",
            "Category",
            "Description"
        ])

        for expense in expenses:

            writer.writerow([
                expense["amount"],
                expense["category"],
                expense["description"]
            ])


# ========================================
# SAVE SUMMARY REPORT
# ========================================

def save_summary(
    total_budget,
    total_expense,
    number_of_expenses,
    average_expense,
    remaining_budget,
    highest_category,
    highest_category_amount,
    highest_expense
):

    with open(
        "data/summary.csv",
        mode="w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Metric",
            "Value"
        ])

        writer.writerow([
            "Total Budget",
            f"{total_budget:.2f}"
        ])

        writer.writerow([
            "Total Expense",
            f"{total_expense:.2f}"
        ])

        writer.writerow([
            "Number of Expenses",
            number_of_expenses
        ])

        writer.writerow([
            "Average Expense",
            f"{average_expense:.2f}"
        ])

        writer.writerow([
            "Remaining Budget",
            f"{remaining_budget:.2f}"
        ])

        writer.writerow([
            "Highest Spending Category",
            highest_category
        ])

        writer.writerow([
            "Highest Category Amount",
            f"{highest_category_amount:.2f}"
        ])

        if highest_expense is not None:

            writer.writerow([
                "Highest Individual Expense",
                f"{highest_expense['amount']:.2f}"
            ])

            writer.writerow([
                "Highest Expense Category",
                highest_expense["category"]
            ])

            writer.writerow([
                "Highest Expense Description",
                highest_expense["description"]
            ])


# ========================================
# LOAD MONTHLY BUDGET
# ========================================

def load_budget():

    try:

        with open(
            "data/budget.csv",
            mode="r",
            newline=""
        ) as file:

            reader = csv.DictReader(file)

            row = next(reader, None)

            if row is None:
                return None

            return {
                "month": row["Month"],
                "budget": float(row["Budget"])
            }

    except FileNotFoundError:

        return None

    except (ValueError, KeyError):

        return None


# ========================================
# SAVE MONTHLY BUDGET
# ========================================

def save_budget(month, budget):

    with open(
        "data/budget.csv",
        mode="w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Month",
            "Budget"
        ])

        writer.writerow([
            month,
            f"{budget:.2f}"
        ])


# ========================================
# CLEAR EXPENSES
# ========================================

def clear_expenses():

    with open(
        "data/expenses.csv",
        mode="w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Amount",
            "Category",
            "Description"
        ])