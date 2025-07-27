def get_book_text(file):
    with open(file, encoding="utf-8", errors="ignore") as f:
        file_contents = f.read()
        file_contents = file_contents.lower()
        litery = set(file_contents)
        dic = {}
        for litera in litery:
            x = 0
            if litera.isalpha():
                for word in file_contents:
                    if litera == word:
                        x += 1
                dic[litera] = x
        lista_par = list(dic.items())
        lista_par.sort(key=lambda item: item[1], reverse=True)
    return(lista_par)
