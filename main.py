print("Hello! \nWelcome to the Ockman Banking System.")
while True:
    print("\nPlease choose an option:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Create account")
    print("5. Delete account")
    print("6. Modify account")
    print("0. Exit")

    choice = input("Enter your choice (0-6): ")

    if choice == "1":
        # Call the function to check balance
        pass
    elif choice == "2":
        # Call the function to deposit money
        pass
    elif choice == "3":
        # Call the function to withdraw money
        pass
    elif choice == "4":
        # Call the function to create a new account
        pass
    elif choice == "5":
        # Call the function to delete an account
        pass
    elif choice == "6":
        # Call the function to modify an account
        pass
    elif choice == "0":
        print("Thank you for using the Banking System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
