"""
CP1404/CP5632 Practical - Programming Language file reader and object creator
Estimate: 20 minutes
Actual: __ minutes
"""

import csv
from programming_language import ProgrammingLanguage

def main():
    """Read languages.csv, create ProgrammingLanguage objects, and display them."""
    languages = load_languages("languages.csv")
    for language in languages:
        print(language)

def load_languages(filename):
    """Load languages from CSV file and return list of ProgrammingLanguage objects."""
    languages = []
    with open(filename, 'r') as in_file:
        next(in_file)  # skip header
        reader = csv.reader(in_file)
        for parts in reader:
            name = parts[0]
            typing = parts[1]
            reflection = parts[2] == "Yes"
            year = int(parts[3])
            languages.append(ProgrammingLanguage(name, typing, reflection, year))
    return languages

if __name__ == "__main__":
    main()
