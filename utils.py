from datetime import datetime

def get_valid_amount():

    while True:
        try:
            amount=float(input("Enter amount: "))
            if amount<=0:
                print("Amount must be positive")
                continue
            return amount
        except ValueError:
            print("Invalid input. Please enter a numeric value (e.g., 10.50)")


def get_valid_date():
    while True:
        date_str=input("Enter date (YYYY-MM-DD) or press Enter for Today: ").strip()
        if not date_str:
            return datetime.today().strftime('%Y-%m-%d')
        
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return date_str
        except ValueError:
            print("Invalid Format. Please use YYYY-MM-DD")


def get_non_empty_string(prompt):
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("This field cannot be empty.")