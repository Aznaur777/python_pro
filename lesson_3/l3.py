def menu():
    print("-"*10 + "menu" + '-'*10)
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Exit")
    print("-"*25)
    choice = input("Select an option (1-4): ")
    if choice == '1':
        return 1
    elif choice == '2':
        return 2
    elif choice == '3':
        return 3
    elif choice == '4':
        return 4
    else:
        print("Invalid choice, please try again.")
        return menu()
    
f = menu()
while f != 4:
    print(f"You selected option {f}.")
    f = menu()
    