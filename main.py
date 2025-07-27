import sys
from stats import get_book_text
from total import get_book_total

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        plik = sys.argv[1]
        print(f"Found {get_book_total(f"{plik}")} total words")
        print("--------- Character Count -------")
        wynik = get_book_text(f"{plik}")
        for litera, liczba in wynik:
            print(f"{litera}: {liczba}")




main()
