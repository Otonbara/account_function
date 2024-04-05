import csv

class Transaction:
    def __init__(self, action, amount):
        self.action = action # 'deposit' or 'withdrawal'
        self.amount = amount

class Account:
    """A class representing account info."""
    def __init__(self, account_number, initial_amount=0):
        self.account_number = account_number
        self.transactions = []
        self.make_transaction('Initial Deposit', initial_amount)

    def make_transaction(self, action, amount):
        if action not in ['Deposit', 'Withdrawal', 'Initial Deposit']:
            print("Invalid action. Transaction not recorded.")
            return
        if amount <= 0:
            print("Transaction amount must be greater than zero.")
            return
        if action == 'Withdrawal' and amount > self.get_balance():
            print("Insufficient funds for withdrawal.")
            return
        self.transactions.append(Transaction(action, amount))

    def get_balance(self):
        balance = 0
        for transaction in self.transactions:
            if transaction.action in ['Deposit', 'Initial Deposit']:
                balance += transaction.amount
            elif transaction.action == 'Withdrawal':
                balance -= transaction.amount
        return balance
    
    def write_transactions_to_csv(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['Transaction Type', 'Amount'])
            for transaction in self.transactions:
                csv_writer.writerow([transaction.action, transaction.amount])

print('Starting')
my_account = Account('1234567890', initial_amount=500000)
my_account.make_transaction('Deposit', 500000)
my_account.make_transaction('Withdrawal', 300000)

print("Current balance", my_account.get_balance())

# Write transactions to CSV
my_account.write_transactions_to_csv('account_transactions.csv')