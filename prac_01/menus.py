"""
Simple menu-driven program to greet or say goodbye to the user.
"""

# Get the user's name
name = input("Enter name: ")

MENU = "(H)ello\n(G)oodbye\n(Q)uit"
print(MENU)

# Get initial choice
choice = input(">>> ").upper()

while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    # Display menu again and get the next choice
    print(MENU)
    choice = input(">>> ").upper()

print("Finished.")
