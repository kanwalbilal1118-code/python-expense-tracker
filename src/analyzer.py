# ========================================
# CALCULATE EXPENSE SUMMARY
# ========================================

def calculate_summary(expenses):

    total_expense = 0.0
    number_of_expenses = 0

    for expense in expenses:

        total_expense += expense["amount"]
        number_of_expenses += 1

    average_expense = (
        total_expense / number_of_expenses
        if number_of_expenses > 0
        else 0
    )

    return total_expense, number_of_expenses, average_expense


# ========================================
# BUDGET ALERT
# ========================================

def budget_alert(total_budget, total_expense):

    if total_budget <= 0:
        return "Invalid budget."

    budget_usage = (total_expense / total_budget) * 100

    if total_expense > total_budget:

        exceeded_amount = total_expense - total_budget

        return (
            f"🚨 ALERT: Your budget has been exceeded!\n"
            f"Budget Usage: {budget_usage:.0f}%\n"
            f"Amount Over Budget: {exceeded_amount:.2f}"
        )

    elif budget_usage >= 80:

        remaining = total_budget - total_expense

        return (
            f"⚠️ WARNING: You have used {budget_usage:.0f}% "
            f"of your budget!\n"
            f"Remaining Budget: {remaining:.2f}"
        )

    else:

        return (
            f"Budget Usage: {budget_usage:.0f}%\n"
            f"Your spending is under control."
        )


# ========================================
# CALCULATE CATEGORY TOTALS
# ========================================

def calculate_category_totals(expenses):

    expenses_by_category = {}

    for expense in expenses:

        category = expense["category"]
        amount = expense["amount"]

        if category in expenses_by_category:
            expenses_by_category[category] += amount
        else:
            expenses_by_category[category] = amount

    return expenses_by_category


# ========================================
# GENERATE SPENDING INSIGHTS
# ========================================

def generate_insights(expenses_by_category, total_expense):

    insights = []

    if total_expense == 0:
        return insights

    for category, total in expenses_by_category.items():

        percentage = (total / total_expense) * 100

        if percentage >= 50:

            insights.append(
                f"{category} is your largest spending area, "
                f"using {percentage:.1f}% of your total spending."
            )

    if not insights:

        insights.append(
            "Your spending is distributed across multiple categories."
        )

    return insights


# ========================================
# FIND HIGHEST SPENDING CATEGORY
# ========================================

def find_highest_category(expenses_by_category):

    highest_category = None

    for category in expenses_by_category:

        if (
            highest_category is None
            or expenses_by_category[category]
            > expenses_by_category[highest_category]
        ):
            highest_category = category

    return highest_category


# ========================================
# FIND HIGHEST INDIVIDUAL EXPENSE
# ========================================

def find_highest_expense(expenses):

    highest_expense = None

    for expense in expenses:

        if (
            highest_expense is None
            or expense["amount"] > highest_expense["amount"]
        ):
            highest_expense = expense

    return highest_expense