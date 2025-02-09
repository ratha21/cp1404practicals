def get_password() -> str:
    """Prompt the user to enter a valid password."""
    password = input("Enter a password (min 3 characters): ")
    while len(password) < 3:
        print("Password too short. Please enter at least 3 characters.")
        password = input("Enter a password: ")
    return password


def print_asterisks(password: str) -> None:
    """Print asterisks matching the length of the password."""
    print('*' * len(password))


def main():
    password = get_password()
    print_asterisks(password)


if __name__ == "__main__":
    main()
