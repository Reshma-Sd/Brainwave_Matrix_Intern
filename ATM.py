class ATM:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def display_menu(self):
        print("\nWelcome to the ATM")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

    def check_balance(self):
        print(f"\nYour current balance is: ₹{self.balance}")

    def deposit_money(self):
        try:
            amount = float(input("\nEnter the amount to deposit: ₹"))
            if amount > 0:
                self.balance += amount
                print(f"₹{amount} deposited successfully. New balance: ₹{self.balance}")
            else:
                print("Please enter a valid amount.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    def withdraw_money(self):
        try:
            amount = float(input("\nEnter the amount to withdraw: ₹"))
            if amount > 0:
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"₹{amount} withdrawn successfully. Remaining balance: ₹{self.balance}")
                else:
                    print("Insufficient balance.")
            else:
                print("Please enter a valid amount.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    def run(self):
        while True:
            self.display_menu()
            choice = input("\nEnter your choice (1-4): ")
            if choice == '1':
                self.check_balance()
            elif choice == '2':
                self.deposit_money()
            elif choice == '3':
                self.withdraw_money()
            elif choice == '4':
                print("\nThank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


# Initialize the ATM with a starting balance
atm = ATM(initial_balance=5000)  # You can set any initial balance here
atm.run()

