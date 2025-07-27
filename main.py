from stats import get_book_text

def main():
    xd = get_book_text("books/frankenstein.txt")
    print(f"{xd} words found in the document")

main()
