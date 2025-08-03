"""
Simple Wikipedia page lookup tool.
"""
from re import search

import wikipedia



def main():
    """Prompt for a Wikipedia page and display its details."""
    title = input("Enter a Wikipedia page title: ")
    while title:
        try:
            page = wikipedia.page(title)
            print(f"\nTitle: {page.title}")
            print(f"Summary: {page.summary}")
            print(f"URL: {page.url}")
        except wikipedia.exceptions.DisambiguationError as e:
            print(f"Too many matches. Suggestions: {e.options}")
        except wikipedia.exceptions.PageError:
            print("Page not found. Please try a different title.")
        title = input("\nEnter another title (or blank to quit): ")


if __name__ == "__main__":
    main()
