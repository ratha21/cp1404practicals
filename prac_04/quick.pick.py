import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6

def main():
    number_of_picks = int(input("How many quick picks? "))
    for _ in range(number_of_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{num:2}" for num in quick_pick))

def generate_quick_pick():
    """Generate a sorted quick pick with unique numbers."""
    quick_pick = set()
    while len(quick_pick) < NUMBERS_PER_PICK:
        quick_pick.add(random.randint(MIN_NUMBER, MAX_NUMBER))
    return sorted(quick_pick)

if __name__ == "__main__":
    main()
