def get_book_total(file):
    with open(file, encoding="utf-8", errors="ignore") as f:
        file_contents = f.read()
        words = file_contents.split()
        number = len(words)
    return(number)
