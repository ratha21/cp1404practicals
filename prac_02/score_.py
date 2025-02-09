import random


def get_score_result(score: int) -> str:
    """
    Determines the result based on the score.
    :param score: integer score (0-100)
    :return: Result as a string
    """
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def main():
    # Ask the user for their score
    user_score = int(input("Enter your score (0-100): "))
    print(f"Your result: {get_score_result(user_score)}")

    # Generate a random score and print the result
    random_score = random.randint(0, 100)
    print(f"Random score: {random_score}, Result: {get_score_result(random_score)}")


if __name__ == "__main__":
    main()