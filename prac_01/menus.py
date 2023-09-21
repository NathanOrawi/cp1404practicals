MENU = """(H)ello
(G)ood bye
(Q)uit"""
name = input("Enter name: ")
print(MENU)
choice = input(">>> ").upper()
while choice != 'Q':
    if choice == 'H':
        print(f"Hello {name}")
    elif choice == 'G':
        print(f"Good bye {name}")
    else:
        print("Invalid choice")
    print(MENU)
    choice = input(">>> ").upper()
print("Finished")