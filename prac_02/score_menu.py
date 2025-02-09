

MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""

def main():
    print("Welcome to the Score Menu Program!")
    score = get_valid_score()
    while True:
        print(MENU)
        choice = input("Choose an option: ").strip().upper()
        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            print_result(score)
        elif choice == 'S':
            show_stars(score)
        elif choice == 'Q':
            print("Thank you for using the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from the menu.")


def get_valid_score():
    """Prompt the user until they enter a valid score between 0 and 100 inclusive."""
    while True:
        try:
            score = int(input("Enter a valid score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


def print_result(score):
    """Print the result based on the score."""
    result = determine_result(score)
    print(f"The result for score {score} is: {result}")


def show_stars(score):
    """Display stars equivalent to the score."""
    print("*" * score)


if __name__ == "__main__":
    main()