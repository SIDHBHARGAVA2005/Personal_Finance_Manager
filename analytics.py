def calculate_total(expenses):
    return sum(e.amount for e in expenses)

def calculate_average(expenses):
    if not expenses:
        return 0.0
    return calculate_total(expenses)/len(expenses)

def get_category_breakdown(expenses):
    breakdown={}
    for e in expenses:
        breakdown[e.category]=breakdown.get(e.category, 0) + e.amount
    return breakdown

def print_report(expenses):
    if not expenses:
        print("\n No expenses to report.")
        return
    
    print("\n" + "="*40)
    print(f"{'FINANCIAL REPORT':^40}")
    print("="*40)

    total=calculate_total(expenses)
    avg=calculate_average(expenses)
    print(f"Total Expenses:  ${total:,.2f}")
    print(f"Average Expense: ${avg:,.2f}")


    print("\n--- Category Breakdown ---")
    breakdown=get_category_breakdown(expenses)
    for category, amount in breakdown.items():
        percentage=(amount/total) * 100
        print(f"{category<15}: ${amount:>8.2f} ({percentage:.1f}%)")

    print("="*40 + "\n")