def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
        words = file_contents.split()
        number = len(words)
    return(number)
