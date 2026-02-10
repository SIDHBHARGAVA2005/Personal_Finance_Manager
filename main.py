import sys
from models import Expense
import storage
import utils 
import analytics

def add_expense(expenses):
    print("\n--- Add New Expense ---")
    amount=utils.get_valid_amount()
    category = utils.get_non_empty_string("Enter category (Food/Transport/Bills/etc): ")
    date = utils.get_valid_date()
    description = utils.get_non_empty_string("Enter description: ")
    
    new_expense = Expense(amount, category, date, description)
    expenses.append(new_expense)
    storage.save_expenses(expenses)
    print("✅ Expense added successfully!")

def view_expenses(expenses):
    print("\n--- Expense History ---")
    if not expenses:
        print("No records found.")
        return
    
    print(f"{'Date':<12} | {'Category':<15} | {'Amount':<10} | {'Description'}")
    print("-" * 60)
    for e in expenses:
        print(e)
    print("-" * 60)

def main():
    print("🚀 Initializing Personal Finance Manager...")
    expenses = storage.load_expenses()
    
    while True:
        print("\n=== MAIN MENU ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Generate Report")
        print("4. Backup Data")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ").strip()
        
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            analytics.print_report(expenses)
        elif choice == '4':
            storage.backup_data()
        elif choice == '5':
            print("Saving data and exiting... Goodbye! 👋")
            storage.save_expenses(expenses)
            sys.exit()
        else:
            print("❌ Invalid option. Please try again.")

if __name__=="__main__":
    main()