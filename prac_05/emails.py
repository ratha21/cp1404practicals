def extract_name(email):
    parts = email.split('@')[0].split('.')
    name = ' '.join(parts).title()
    return name

def main():
    email_to_name = {}

    while True:
        email = input("Email: ").strip()
        if not email:
            break

        default_name = extract_name(email)
        response = input(f"Is your name {default_name}? (Y/n) ").strip().lower()

        if response and response != 'y':
            name = input("Name: ").strip()
        else:
            name = default_name

        email_to_name[email] = name

    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")

if __name__ == "__main__":
    main()