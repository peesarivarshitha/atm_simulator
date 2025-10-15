def check_balance(balance):
    print(f"\nYour current balance is: ₹{balance:.2f}")
def deposit(balance):
    try:
        amount = float(input("\nEnter amount to deposit: ₹"))
        if amount <= 0:
            print("Amount must be positive.")
            return balance
        if amount > 50000:
            print("Deposit limit exceeded. Try again.")
            return balance
        balance += amount
        print(f"₹{amount:.2f} deposited successfully.")
        return balance
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return balance
def withdraw(balance):
    try:
        amount = float(input("\nEnter amount to withdraw: ₹"))
        if amount <= 0:
            print("Amount must be positive.")
            return balance
        if amount > 20000:
            print("Withdrawal limit exceeded. Maximum ₹20,000 per transaction.")
            return balance
        if amount % 100 != 0:
            print("Amount must be in multiples of 100.")
            return balance
        if amount > balance:
            print("Insufficient funds.")
            return balance
        if balance - amount < 1000:
            print("Transaction rejected. Minimum balance of ₹1,000 must be maintained.")
            return balance
        balance -= amount
        print(f"₹{amount:.2f} withdrawn successfully.")
        return balance
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return balance
def atm():
    correct_pin = "1234"  
    balance = 10000.0   
    attempts = 3
    print("🏦 Welcome to the ATM Machine Simulator!")
    while attempts > 0:
        pin = input("\nPlease enter your 4-digit PIN: ")
        if pin == correct_pin:
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Wrong PIN. {attempts} attempt(s) remaining.")
            else:
                print("Card Blocked. Please contact bank.")
                return
    while True:
        print("\n" + "="*40)
        print("          ATM MENU")
        print("="*40)
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        print("="*40)
        choice = input("Please select an option (1-4): ")
        if choice == '1':
            check_balance(balance)
        elif choice == '2':
            balance = deposit(balance)
        elif choice == '3':
            balance = withdraw(balance)
        elif choice == '4':
            print("\nThank you for banking with us!")
            break
        else:
            print("Invalid option. Please try again.")
if __name__ == "__main__":
    atm()
