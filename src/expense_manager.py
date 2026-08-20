from file_manager import save_budget, save_expenses


# ========================================
# ADD NEW EXPENSES
# ========================================

def add_expenses(expenses):

    while True:

        # --------------------------------
        # EXPENSE AMOUNT
        # --------------------------------

        while True:

            try:
                amount = float(
                    input("Enter the expense amount: ")
                )

                if amount > 0:
                    break

                print("Amount must be greater than 0.")

            except ValueError:
                print("Please enter a valid number.")

        # --------------------------------
        # CATEGORY
        # --------------------------------

        while True:

            category = input(
                "Enter the expense category: "
            ).strip()

            if category:
                break

            print("Category cannot be empty.")

        # --------------------------------
        # DESCRIPTION
        # --------------------------------

        while True:

            description = input(
                "Enter a description for the expense: "
            ).strip()

            if description:
                break

            print("Description cannot be empty.")

        # --------------------------------
        # CREATE EXPENSE
        # --------------------------------

        expense = {
            "amount": amount,
            "category": category,
            "description": description
        }

        expenses.append(expense)

        # --------------------------------
        # ADD ANOTHER?
        # --------------------------------

        while True:

            user_input = input(
                "Do you want to add another expense? (yes/no): "
            ).lower().strip()

            if user_input in ["yes", "no"]:
                break

            print("Please enter yes or no.")

        if user_input == "no":
            break

    return expenses


# ========================================
# GET VALID BUDGET
# ========================================

def get_valid_budget():

    while True:

        try:

            budget = float(
                input("Enter your monthly budget: ")
            )

            if budget > 0:
                return budget

            print("Budget must be greater than 0.")

        except ValueError:

            print("Please enter a valid number.")


# ========================================
# GET NEW MONTHLY BUDGET
# ========================================

def get_new_budget():

    while True:

        try:

            budget = float(
                input("Enter your new monthly budget: ")
            )

            if budget > 0:
                return budget

            print("Budget must be greater than 0.")

        except ValueError:

            print("Please enter a valid number.")

# ========================================
# CLEAR CURRENT MONTH EXPENSES
# ========================================

def clear_expenses():
    save_expenses([])