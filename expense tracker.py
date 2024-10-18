from datetime import datetime, timedelta
from collections import defaultdict

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category, date):
        self.expenses.append({
            'amount': amount,
            'category': category,
            'date': datetime.strptime(date, '%Y-%m-%d')
        })
        print(f"Added expense: ₹{amount:.2f} in category '{category}' on {date}.")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return
        
        print("\nExpenses:")
        for index, expense in enumerate(self.expenses, start=1):
            print(f"{index}. ₹{expense['amount']:.2f} | Category: {expense['category']} | Date: {expense['date'].strftime('%Y-%m-%d')}")
        print(f"Total expenses: ₹{self.get_total_expenses():.2f}\n")

    def view_summary(self):
        print("\nSummary of Expenses:")
        total = self.get_total_expenses()
        print(f"Total Overall Spending: ₹{total:.2f}")

        category = input("Enter category for spending summary: ")
        total_category = self.get_total_spending_by_category(category)
        print(f"Total Spending in '{category}': ₹{total_category:.2f}")

        time_unit = input("Enter time unit for spending over time (daily, weekly, monthly): ").lower()
        self.summary_by_time(time_unit)

    def summary_by_time(self, time_unit):
        if not self.expenses:
            print("No expenses recorded.")
            return
        
        summary = defaultdict(float)

        for expense in self.expenses:
            if time_unit == 'daily':
                key = expense['date'].date()
            elif time_unit == 'weekly':
                key = expense['date'] - timedelta(days=expense['date'].weekday())  # Start of the week
            elif time_unit == 'monthly':
                key = expense['date'].replace(day=1)
            else:
                print("Invalid time unit. Choose 'daily', 'weekly', or 'monthly'.")
                return

            summary[key] += expense['amount']

        print(f"\nSpending Summary by {time_unit.capitalize()}:")
        for key, total in sorted(summary.items()):
            print(f"{key}: ₹{total:.2f}")
        print(f"Total spending over {time_unit}: ₹{sum(summary.values()):.2f}\n")

    def get_total_spending_by_category(self, category):
        return sum(expense['amount'] for expense in self.expenses if expense['category'].lower() == category.lower())

    def delete_expense(self, index):
        if 0 <= index < len(self.expenses):
            removed = self.expenses.pop(index)
            print(f"Removed expense of ₹{removed['amount']:.2f} in category '{removed['category']}'")
        else:
            print("Invalid expense number.")

    def get_total_expenses(self):
        return sum(expense['amount'] for expense in self.expenses)

def main():
    tracker = ExpenseTracker()

    while True:
        print("Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Summary of Expenses")
        print("4. Delete Expense")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            amount = float(input("Enter expense amount (in ₹): "))
            category = input("Enter expense category: ")
            date_input = input("Enter expense date (YYYY-MM-DD, or press Enter for today): ")
            date = date_input if date_input else datetime.now().strftime('%Y-%m-%d')
            tracker.add_expense(amount, category, date)
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            tracker.view_summary()
        elif choice == '4':
            tracker.view_expenses()
            try:
                index = int(input("Enter the expense number to delete: ")) - 1
                tracker.delete_expense(index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
