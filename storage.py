import csv
import shutil
import os
from models import Expense

FILENAME="expenses.xlsx"
BACKUP_DIR="backups"

def save_expenses(expenses):

    try:
        with open(FILENAME, mode='w', newline='', encoding='utf-8') as file:
            fieldnames=['amount', 'category', 'date', 'description']
            writer=csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            for expense in expenses:
                writer.writerow(expense.to_dict())
        print("Data saved successfully")
    except IOError as e:
        print(f"Error Saving data: {e}")

    return expenses

def load_expenses():
    """Reads CSV and returns a list of Expense objects."""
    expenses = []
    if not os.path.exists(FILENAME):
        return expenses

    try:
        with open(FILENAME, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append(Expense(
                    amount=row['amount'],
                    category=row['category'],
                    date=row['date'],
                    description=row['description']
                ))
    except (IOError, ValueError) as e:
        print(f"⚠️ Error loading data: {e}. Starting with empty list.")
    
    return expenses

def backup_data():

    if not os.path.exists(FILENAME):
        print("No data file to backup")
        return
    
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(BACKUP_DIR, f"expenses_backup_{timestamp}.csv")
    
    try:
        shutil.copy2(FILENAME, backup_file)
        print(f"✅ Backup created: {backup_file}")
    except IOError as e:
        print(f"❌ Backup failed: {e}")
        
from datetime import datetime