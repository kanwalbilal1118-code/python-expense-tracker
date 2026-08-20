import sys
import os

import streamlit as st
import pandas as pd
from datetime import datetime

# ========================================
# ALLOW IMPORTS FROM SRC
# ========================================

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

SRC_PATH = os.path.join(PROJECT_ROOT, "src")

if SRC_PATH not in sys.path:
    sys.path.append(SRC_PATH)


# ========================================
# IMPORT PROJECT FUNCTIONS
# ========================================

from file_manager import (
    load_expenses,
    save_expenses,
    load_budget,
    save_budget,
    clear_expenses,
)

from analyzer import (
    calculate_summary,
    budget_alert,
    calculate_category_totals,
    generate_insights,
    find_highest_category,
    find_highest_expense,
)


# ========================================
# PAGE CONFIGURATION
# ========================================

st.set_page_config(
    page_title="Expense Tracker Dashboard",
    page_icon="💰",
    layout="wide",
)


# ========================================
# TITLE
# ========================================

st.title("💰 Expense Tracker Dashboard")

st.caption(
    "Track your monthly budget, expenses, spending patterns, "
    "and financial insights."
)


# ========================================
# LOAD DATA
# ========================================

expenses = load_expenses()

budget_data = load_budget()

if budget_data is not None:
    budget = budget_data["budget"]
    current_month = budget_data["month"]
else:
    budget = None
    current_month = None


# ========================================
# SIDEBAR
# ========================================

st.sidebar.title("📌 Expense Tracker")

st.sidebar.markdown("### Navigation")

page = st.sidebar.radio(
    "Choose an option:",
    [
        "📊 Dashboard",
        "➕ Add Expense",
        "📅 Start New Month",
    ],
)


# ========================================
# REFRESH BUTTON
# ========================================

if st.sidebar.button("🔄 Refresh Dashboard"):
    st.rerun()


# ========================================
# DASHBOARD PAGE
# ========================================

if page == "📊 Dashboard":

    st.header("📊 Monthly Dashboard")
    if current_month:
     st.caption(f"📅 Current Month: {current_month}")

    # ------------------------------------
    # CHECK BUDGET
    # ------------------------------------

    if budget is None:

        st.warning(
            "No monthly budget has been set yet."
        )

        st.info(
            "Go to 'Start New Month' from the sidebar "
            "to create your monthly budget."
        )

        st.stop()

    # ------------------------------------
    # CALCULATE SUMMARY
    # ------------------------------------

    (
        total_expense,
        number_of_expenses,
        average_expense,
    ) = calculate_summary(expenses)

    remaining_budget = budget - total_expense

    expenses_by_category = calculate_category_totals(
        expenses
    )

    highest_category = find_highest_category(
        expenses_by_category
    )

    highest_expense = find_highest_expense(
        expenses
    )

    budget_message = budget_alert(
        budget,
        total_expense
    )

    # ------------------------------------
    # TOP METRICS
    # ------------------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "💰 Monthly Budget",
            f"{budget:,.2f}"
        )

    with col2:

        st.metric(
            "💸 Total Expenses",
            f"{total_expense:,.2f}"
        )

    with col3:

        st.metric(
            "💵 Remaining Budget",
            f"{remaining_budget:,.2f}"
        )

    with col4:

        st.metric(
            "🧾 Number of Expenses",
            number_of_expenses
        )

    st.divider()

    # ------------------------------------
    # BUDGET STATUS
    # ------------------------------------

    st.subheader("🚦 Budget Status")

    if total_expense > budget:

        st.error(
            f"🚨 Budget exceeded by "
            f"{total_expense - budget:,.2f}"
        )

    elif total_expense >= budget * 0.8:

        st.warning(
            f"⚠️ You have used "
            f"{(total_expense / budget) * 100:.1f}% "
            f"of your budget."
        )

    else:

        st.success(
            f"✅ You have used "
            f"{(total_expense / budget) * 100:.1f}% "
            f"of your budget."
        )

    # ------------------------------------
    # BUDGET PROGRESS
    # ------------------------------------

    usage = total_expense / budget

    if usage > 1:
        usage = 1

    st.progress(usage)

    st.caption(
        f"Budget usage: "
        f"{(total_expense / budget) * 100:.1f}%"
    )

    # ------------------------------------
    # SUMMARY
    # ------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("📈 Expense Summary")

        st.write(
            f"**Average Expense:** "
            f"{average_expense:,.2f}"
        )

        st.write(
            f"**Remaining Budget:** "
            f"{remaining_budget:,.2f}"
        )

        if remaining_budget >= 0:

            st.write(
                "Status: **Within Budget**"
            )

        else:

            st.write(
                "Status: **Budget Exceeded**"
            )

    with col2:

        st.subheader("💡 Spending Insights")

        insights = generate_insights(
            expenses_by_category,
            total_expense
        )

        if insights:

            for insight in insights:

                st.info(
                    f"💡 {insight}"
                )

        else:

            st.info(
                "No spending insights available yet."
            )

    st.divider()

    # ------------------------------------
    # CATEGORY SPENDING
    # ------------------------------------

    st.subheader("📂 Category Spending")

    if expenses_by_category and total_expense > 0:

        category_data = pd.DataFrame(
            {
                "Category": list(
                    expenses_by_category.keys()
                ),
                "Amount": list(
                    expenses_by_category.values()
                ),
            }
        )

        category_data["Percentage"] = (
            category_data["Amount"]
            / total_expense
            * 100
        )

        st.dataframe(
            category_data,
            use_container_width=True,
            hide_index=True,
        )

        # --------------------------------
        # CATEGORY CHART
        # --------------------------------

        st.subheader("📊 Spending by Category")

        chart_data = category_data.set_index(
            "Category"
        )["Amount"]

        st.bar_chart(chart_data)

    else:

        st.info(
            "No expenses recorded for this month."
        )

    st.divider()

    # ------------------------------------
    # HIGHEST CATEGORY
    # ------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.subheader(
            "🏆 Highest Spending Category"
        )

        if highest_category is not None:

            highest_amount = (
                expenses_by_category[
                    highest_category
                ]
            )

            st.write(
                f"**Category:** "
                f"{highest_category}"
            )

            st.write(
                f"**Amount:** "
                f"{highest_amount:,.2f}"
            )

        else:

            st.info(
                "No category data available."
            )

    # ------------------------------------
    # HIGHEST EXPENSE
    # ------------------------------------

    with col2:

        st.subheader(
            "💳 Highest Individual Expense"
        )

        if highest_expense is not None:

            st.write(
                f"**Amount:** "
                f"{highest_expense['amount']:,.2f}"
            )

            st.write(
                f"**Category:** "
                f"{highest_expense['category']}"
            )

            st.write(
                f"**Description:** "
                f"{highest_expense['description']}"
            )

        else:

            st.info(
                "No expenses available."
            )

    st.divider()

    # ------------------------------------
    # EXPENSE HISTORY
    # ------------------------------------

    st.subheader("📜 Expense History")

    if expenses:

        history_data = pd.DataFrame(expenses)

        history_data.index = range(
            1,
            len(history_data) + 1
        )

        history_data.index.name = "No."

        st.dataframe(
            history_data,
            use_container_width=True,
        )

    else:

        st.info(
            "No expenses recorded yet."
        )


# ========================================
# ADD EXPENSE PAGE
# ========================================

elif page == "➕ Add Expense":

    st.header("➕ Add New Expense")

    if budget is None:

        st.warning(
            "Please start a month and set a budget first."
        )

        st.info(
            "Go to '📅 Start New Month' to create "
            "your first monthly budget."
        )

    else:

        st.write(
            f"Current monthly budget: "
            f"**{budget:,.2f}**"
        )

        st.divider()

        amount = st.number_input(
            "Expense Amount",
            min_value=0.01,
            step=1.00,
            format="%.2f",
        )

        category = st.text_input(
            "Expense Category",
            placeholder="e.g. food, transport, shopping"
        )

        description = st.text_input(
            "Description",
            placeholder="e.g. groceries, lunch, shoes"
        )

        if st.button(
            "➕ Add Expense",
            type="primary"
        ):

            if not category.strip():

                st.error(
                    "Please enter an expense category."
                )

            elif not description.strip():

                st.error(
                    "Please enter a description."
                )

            elif amount <= 0:

                st.error(
                    "Expense amount must be greater than 0."
                )

            else:

                new_expense = {
                    "amount": float(amount),
                    "category": category.strip(),
                    "description": description.strip(),
                }

                expenses.append(new_expense)

                save_expenses(expenses)

                st.success(
                    "✅ Expense added successfully!"
                )

                st.info(
                    f"Added {amount:,.2f} "
                    f"under '{category.strip()}'."
                )

                st.rerun()


# ========================================
# START NEW MONTH PAGE
# ========================================

elif page == "📅 Start New Month":

    st.header("📅 Start a New Month")

    st.warning(
        "Starting a new month will clear the "
        "current month's expenses."
    )

    st.write(
        "Your previous month's expenses will be "
        "removed from the current expense list."
    )

    st.divider()

    new_budget = st.number_input(
        "New Monthly Budget",
        min_value=0.01,
        step=100.00,
        format="%.2f",
    )

    confirm = st.checkbox(
        "I understand that the current month's "
        "expenses will be cleared."
    )

    if st.button(
        "📅 Start New Month",
        type="primary"
    ):

        if not confirm:

            st.error(
                "Please confirm that you want to "
                "clear the current month's expenses."
            )

        elif new_budget <= 0:

            st.error(
                "Budget must be greater than 0."
            )

        else:

            # --------------------------------
            # CLEAR OLD EXPENSES
            # --------------------------------

            clear_expenses()

            # --------------------------------
            # SAVE NEW BUDGET
            # --------------------------------

            # Save new budget
            new_month = datetime.now().strftime("%Y-%m")
            save_budget(
            new_month,
            float(new_budget)
            )  


            st.success(
                "✅ New month started successfully!"
            )

            st.info(
                f"New monthly budget: "
                f"{new_budget:,.2f}"
            )

            st.write(
                "Previous month's expenses "
                "have been cleared."
            )

            st.rerun()