# ATM Project - Python Based

import datetime

# Class to represent a simple ATM system
class ATM:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        self.transactions = []  # Stores the transaction history

    # Method to check account balance
    def check_balance(self):
        print(f"Current Balance: ${self.balance}")
        return self.balance

    # Method to deposit funds
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append((datetime.datetime.now(), f"Deposited: ${amount}"))
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be greater than zero.")
    
    # Method to withdraw funds
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transactions.append((datetime.datetime.now(), f"Withdrew: ${amount}"))
            print(f"Withdrew: ${amount}")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            print("Withdrawal amount must be greater than zero.")
    
    # Method to print transaction history
    def print_statement(self):
        if not self.transactions:
            print("No transactions available.")
        else:
            print("\nTransaction History:")
            for date, action in self.transactions:
                print(f"{date} - {action}")
            print(f"Current Balance: ${self.balance}\n")

# Function to simulate ATM interface
def atm_interface():
    atm = ATM(initial_balance=1000)  # Create ATM object with an initial balance of $1000
    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Print Statement")
        print("5. Exit")
        choice = input("Select an option (1-5): ")
        
        if choice == '1':
            atm.check_balance()
        
        elif choice == '2':
            amount = float(input("Enter deposit amount: "))
            atm.deposit(amount)
        
        elif choice == '3':
            amount = float(input("Enter withdrawal amount: "))
            atm.withdraw(amount)
        
        elif choice == '4':
            atm.print_statement()
        
        elif choice == '5':
            print("Thank you for using the ATM. Goodbye!")
            break
        
        else:
            print("Invalid option. Please try again.")

# Run the ATM interface
if __name__ == "__main__":
    atm_interface()
