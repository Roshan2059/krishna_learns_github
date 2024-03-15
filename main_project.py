class Bank:
    interest_rate = 12
    government_holidays = ["Dashain", "Tihar", "New Year"]

    def __init__(self, first_name, last_name, balance=0):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance

    def check_balance(self):
        if self.balance == 0:
            return "Thukka mulaa garib 0 rupay xa tero bank account ma"
        else:
            return f"The current balance is {self.balance}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Aich kto. Pragati gardai xa kto le j hos!! Tero New balance: {self.balance}"
        else:
            return "Invalid amount for deposit."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Pasia Ghigis, aba moj gar vai. New balance: {self.balance}"
        else:
            return "Insufficient funds or invalid amount for withdrawal."

    def check_government_holidays(self):
        holidays_list = "\n".join([f"{i+1}. {holiday}" for i, holiday in enumerate(self.government_holidays)])
        return f"The government holidays are:\n{holidays_list}"




def main():
    print("Welcome to the Bank!")

    while True:
        print("\nEnter 1 to open bank account")
        print("Enter 2 to check balance")
        print("Enter 3 to deposit balance")
        print("Enter 4 to withdraw balance")
        print("Enter 5 to check interest rate")
        print("Enter 6 to check government holidays list")
        print("Enter q to quit")

        choice = input("Please enter your choice: ")

        if choice == '1':
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            account = Bank(first_name, last_name)
            print("Account opened successfully!")

        elif choice == '2':
            print(account.check_balance())

        elif choice == '3':
            amount = float(input("Enter amount to deposit: "))
            print(account.deposit(amount))

        elif choice == '4':
            amount = float(input("Enter amount to withdraw: "))
            print(account.withdraw(amount))

        elif choice == '5':
            print("We don't discriminate people. So, for everyone the interest rate is :", Bank.interest_rate , "%")

        elif choice == '6':
            print(account.check_government_holidays())

        elif choice.lower() == 'q':
            print("Roshan ko bank ko sewa linu vayekoma dhanyabaad!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()