balance=10000
user_pin=int(input("Enter the PIN number: "))
pin=9876
if pin==user_pin:
    print("Login Successful")
    choice = 0
    while choice !=4:
        print("\n1.Check balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        choice=int(input("Enter your choice: "))

        if choice==1:
            print(balance)

        elif choice==2:
            amount=int(input("Enter the deposit amount: "))
            balance+=amount
            print("Deposit Successful")
            print("Updated balance",balance)

        elif choice==3:
            amount=int(input("Enter the Withdraw amount: "))

            if amount<=balance:
                balance -=amount
                print("Withdraw Successful")
                print("Remaining amount",balance)
            else:
                print("Insufficient balance")

        elif choice==4:
            print("Thank you for using our ATM")
            print("Exited successfully")

        else:
            print("Invalid choice")

else:
    print("Incorrect PIN")
