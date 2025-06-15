

FILENAME = "wimbledon.csv"


def main():
    records = load_wimbledon_data(FILENAME)
    champion_to_wins = count_champion_wins(records)
    countries = extract_unique_countries(records)

    print("Wimbledon Champions:")
    for champion, wins in champion_to_wins.items():
        print(f"{champion} {wins}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


def load_wimbledon_data(filename):
    """Load Wimbledon data from file, skipping header row and returning list of lists."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        lines = in_file.readlines()[1:]  # Skip header
        records = [line.strip().split(",") for line in lines]
    return records


def count_champion_wins(records):
    """Count number of wins per champion."""
    champion_to_wins = {}
    for record in records:
        champion = record[2]
        champion_to_wins[champion] = champion_to_wins.get(champion, 0) + 1
    return champion_to_wins


def extract_unique_countries(records):
    """Extract set of unique countries of champions."""
    countries = {record[1] for record in records}
    return countries


if __name__ == "__main__":
    main()
