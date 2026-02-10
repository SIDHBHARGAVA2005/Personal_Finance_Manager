class Expense:
    def __init__(self, amount, category, date, description):
        self.amount=float(amount)
        self.category=category
        self.date=date
        self.description=description

    def to_dict(self):

        return{
            'amount': self.amount,
            'category': self.category,
            'date': self.date,
            'description': self.description
        }
    
    def __str__(self):
        return f"{self.date} | {self.category.ljust(15)} | ${self.amount:.2f} | {self.description}"
    