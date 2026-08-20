import sys
import os
import unittest


# ========================================
# ALLOW IMPORTS FROM SRC
# ========================================

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

SRC_PATH = os.path.join(
    PROJECT_ROOT,
    "src"
)

if SRC_PATH not in sys.path:
    sys.path.insert(0, SRC_PATH)


# ========================================
# IMPORT FUNCTIONS TO TEST
# ========================================

from analyzer import (
    calculate_summary,
    budget_alert,
    calculate_category_totals,
    find_highest_category,
    find_highest_expense,
)


# ========================================
# TEST EXPENSE DATA
# ========================================

class TestExpenseTracker(unittest.TestCase):

    def setUp(self):

        self.expenses = [
            {
                "amount": 500.00,
                "category": "food",
                "description": "fish"
            },
            {
                "amount": 200.00,
                "category": "food",
                "description": "meat"
            },
            {
                "amount": 100.00,
                "category": "shoe",
                "description": "sandal"
            },
            {
                "amount": 50.00,
                "category": "drink",
                "description": "juice"
            }
        ]


    # ========================================
    # TEST TOTAL EXPENSE
    # ========================================

    def test_total_expense(self):

        total, count, average = calculate_summary(
            self.expenses
        )

        self.assertEqual(
            total,
            850.00
        )


    # ========================================
    # TEST NUMBER OF EXPENSES
    # ========================================

    def test_number_of_expenses(self):

        total, count, average = calculate_summary(
            self.expenses
        )

        self.assertEqual(
            count,
            4
        )


    # ========================================
    # TEST AVERAGE EXPENSE
    # ========================================

    def test_average_expense(self):

        total, count, average = calculate_summary(
            self.expenses
        )

        self.assertEqual(
            average,
            212.50
        )


    # ========================================
    # TEST CATEGORY TOTALS
    # ========================================

    def test_category_totals(self):

        category_totals = calculate_category_totals(
            self.expenses
        )

        self.assertEqual(
            category_totals["food"],
            700.00
        )

        self.assertEqual(
            category_totals["shoe"],
            100.00
        )

        self.assertEqual(
            category_totals["drink"],
            50.00
        )


    # ========================================
    # TEST HIGHEST CATEGORY
    # ========================================

    def test_highest_category(self):

        category_totals = calculate_category_totals(
            self.expenses
        )

        highest_category = find_highest_category(
            category_totals
        )

        self.assertEqual(
            highest_category,
            "food"
        )


    # ========================================
    # TEST HIGHEST INDIVIDUAL EXPENSE
    # ========================================

    def test_highest_expense(self):

        highest_expense = find_highest_expense(
            self.expenses
        )

        self.assertEqual(
            highest_expense["amount"],
            500.00
        )

        self.assertEqual(
            highest_expense["category"],
            "food"
        )

        self.assertEqual(
            highest_expense["description"],
            "fish"
        )


    # ========================================
    # TEST BUDGET WITHIN LIMIT
    # ========================================

    def test_budget_within_limit(self):

        message = budget_alert(
         1000.00,
         500.00
        )
        
        self.assertIn(
         "under control",
         message
        )
    # ========================================
    # TEST BUDGET EXCEEDED
    # ========================================

    def test_budget_exceeded(self):

        message = budget_alert(
            800.00,
            850.00
        )

        self.assertIn(
            "exceeded",
            message
        )


    # ========================================
    # TEST EMPTY EXPENSE LIST
    # ========================================

    def test_empty_expenses(self):

        total, count, average = calculate_summary(
            []
        )

        self.assertEqual(
            total,
            0
        )

        self.assertEqual(
            count,
            0
        )

        self.assertEqual(
            average,
            0
        )


# ========================================
# RUN TESTS
# ========================================

if __name__ == "__main__":
    unittest.main()