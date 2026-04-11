balance = 500 # starting balance

while True:
    try:
        print("\n1. Withdraw")
        print("2. Check Balance")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter amount to withdraw: "))

            if amount > balance:
                print("Insufficient funds!")
            else:
                balance -= amount
                print("Withdrawal successful!")

        elif choice == "2":
            print("Current balance:", balance)

        elif choice == "3":
            print("Thank you! Exiting...")
            break

        else:
            print("Invalid option!")

    except:
        print("Invalid input! Please enter numbers only.")
