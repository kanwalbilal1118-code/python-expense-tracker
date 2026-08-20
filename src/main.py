from datetime import datetime

from file_manager import (
    load_expenses,
    save_expenses,
    save_summary,
    load_budget,
    save_budget,
    clear_expenses
)

from expense_manager import (
    add_expenses,
    get_valid_budget,
    get_new_budget
)

from analyzer import (
    calculate_summary,
    budget_alert,
    calculate_category_totals,
    generate_insights,
    find_highest_category,
    find_highest_expense
)


# ========================================
# GET MONTHLY BUDGET
# ========================================

def get_budget():

    saved_budget = load_budget()

    # ------------------------------------
    # NO PREVIOUS BUDGET
    # ------------------------------------

    if saved_budget is None:

        current_month = datetime.now().strftime("%Y-%m")

        budget = get_valid_budget()

        save_budget(
            current_month,
            budget
        )

        return budget

    # ------------------------------------
    # PREVIOUS BUDGET EXISTS
    # ------------------------------------

    print()
    print("========================================")
    print("             MONTHLY BUDGET")
    print("========================================")

    print(
        f"Current month: {saved_budget['month']}"
    )

    print(
        f"Current budget: {saved_budget['budget']:.2f}"
    )

    print()
    print("1. Continue current month")
    print("2. Start a new month")

    while True:

        choice = input(
            "Choose an option (1/2): "
        ).strip()

        if choice in ["1", "2"]:
            break

        print("Please enter 1 or 2.")

    # ------------------------------------
    # CONTINUE CURRENT MONTH
    # ------------------------------------

    if choice == "1":

        print(
            f"Monthly budget loaded: "
            f"{saved_budget['budget']:.2f}"
        )

        return saved_budget["budget"]

    # ------------------------------------
    # START NEW MONTH
    # ------------------------------------

    new_month = datetime.now().strftime("%Y-%m")

    print()
    print("Starting a new month...")

    new_budget = get_new_budget()

    save_budget(
        new_month,
        new_budget
    )

    # Remove previous month's expenses
    clear_expenses()

    print()
    print(
        f"New monthly budget saved: "
        f"{new_budget:.2f}"
    )

    print(
        "Previous month's expenses have been cleared."
    )

    return new_budget


# ========================================
# DISPLAY DASHBOARD
# ========================================

def display_dashboard(
    expenses,
    total_budget,
    total_expense,
    number_of_expenses,
    average_expense,
    remaining_budget,
    expenses_by_category,
    highest_category,
    highest_expense,
    budget_message
):

    print()
    print("========================================")
    print("           EXPENSE SUMMARY")
    print("========================================")

    print(
        f"Total Budget:       "
        f"{total_budget:.2f}"
    )

    print(
        f"Total Expense:      "
        f"{total_expense:.2f}"
    )

    print(
        f"Number of Expenses: "
        f"{number_of_expenses}"
    )

    print(
        f"Average Expense:    "
        f"{average_expense:.2f}"
    )

    print(
        f"Remaining Budget:   "
        f"{remaining_budget:.2f}"
    )

    if total_expense > total_budget:

        print(
            "Status:             "
            "BUDGET EXCEEDED!"
        )

    else:

        print(
            "Status:             "
            "Within Budget"
        )

    # ========================================
    # BUDGET ALERT
    # ========================================

    print()
    print("========================================")
    print("              BUDGET ALERT")
    print("========================================")

    print(budget_message)

    # ========================================
    # CATEGORY TOTALS
    # ========================================

    print()
    print("========================================")
    print("           CATEGORY TOTALS")
    print("========================================")

    if expenses_by_category:

        for category, total in expenses_by_category.items():

            print(
                f"{category:<20} "
                f"{total:.2f}"
            )

    else:

        print("No categories recorded.")

    # ========================================
    # SPENDING BREAKDOWN
    # ========================================

    print()
    print("========================================")
    print("          SPENDING BREAKDOWN")
    print("========================================")

    if total_expense == 0:

        print("No expenses recorded.")

    else:

        for category, total in expenses_by_category.items():

            percentage = (
                total / total_expense
            ) * 100

            print(
                f"{category:<20}"
                f"{total:>8.2f}"
                f" ({percentage:.1f}%)"
            )

    # ========================================
    # SPENDING INSIGHTS
    # ========================================

    print()
    print("========================================")
    print("          SPENDING INSIGHTS")
    print("========================================")

    insights = generate_insights(
        expenses_by_category,
        total_expense
    )

    if insights:

        for insight in insights:

            print(f"💡 {insight}")

    else:

        print("No insights available.")

    # ========================================
    # HIGHEST SPENDING CATEGORY
    # ========================================

    print()
    print("========================================")
    print("       HIGHEST SPENDING CATEGORY")
    print("========================================")

    if highest_category is not None:

        print(
            f"Category: "
            f"{highest_category}"
        )

        print(
            f"Amount:   "
            f"{expenses_by_category[highest_category]:.2f}"
        )

    else:

        print("No category available.")

    # ========================================
    # HIGHEST INDIVIDUAL EXPENSE
    # ========================================

    print()
    print("========================================")
    print("        HIGHEST INDIVIDUAL EXPENSE")
    print("========================================")

    if highest_expense is not None:

        print(
            f"Amount:      "
            f"{highest_expense['amount']:.2f}"
        )

        print(
            f"Category:    "
            f"{highest_expense['category']}"
        )

        print(
            f"Description: "
            f"{highest_expense['description']}"
        )

    else:

        print("No expenses available.")

    # ========================================
    # ALL EXPENSES
    # ========================================

    print()
    print("========================================")
    print("              ALL EXPENSES")
    print("========================================")

    if not expenses:

        print("No expenses recorded.")

    else:

        for i, expense in enumerate(
            expenses,
            start=1
        ):

            print()
            print(
                f"Expense {i}"
            )

            print(
                f"  Amount:      "
                f"{expense['amount']:.2f}"
            )

            print(
                f"  Category:    "
                f"{expense['category']}"
            )

            print(
                f"  Description: "
                f"{expense['description']}"
            )


# ========================================
# MAIN PROGRAM
# ========================================

# Get existing budget or create a new one
total_budget = get_budget()

# Load expenses AFTER the monthly budget decision
expenses = load_expenses()

# Add new expenses
expenses = add_expenses(expenses)

# ========================================
# CALCULATE SUMMARY
# ========================================

(
    total_expense,
    number_of_expenses,
    average_expense
) = calculate_summary(expenses)

# ========================================
# CATEGORY TOTALS
# ========================================

expenses_by_category = calculate_category_totals(
    expenses
)

# ========================================
# HIGHEST CATEGORY
# ========================================

highest_category = find_highest_category(
    expenses_by_category
)

if highest_category is not None:

    highest_category_amount = (
        expenses_by_category[highest_category]
    )

else:

    highest_category_amount = 0

# ========================================
# HIGHEST EXPENSE
# ========================================

highest_expense = find_highest_expense(
    expenses
)

# ========================================
# REMAINING BUDGET
# ========================================

remaining_budget = (
    total_budget - total_expense
)

# ========================================
# BUDGET ALERT
# ========================================

budget_message = budget_alert(
    total_budget,
    total_expense
)

# ========================================
# SAVE DATA
# ========================================

save_expenses(expenses)

save_summary(
    total_budget,
    total_expense,
    number_of_expenses,
    average_expense,
    remaining_budget,
    highest_category,
    highest_category_amount,
    highest_expense
)

# ========================================
# DISPLAY DASHBOARD
# ========================================

display_dashboard(
    expenses,
    total_budget,
    total_expense,
    number_of_expenses,
    average_expense,
    remaining_budget,
    expenses_by_category,
    highest_category,
    highest_expense,
    budget_message
)