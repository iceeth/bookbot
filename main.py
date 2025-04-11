import sys
from stats import get_books_text, letter_count, Print_Report


def main():
    get_books_text()
    result = letter_count(sys)
    Print_Report(result, get_books_text())
 
main()