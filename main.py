def main ():
    get_books_text()

def get_books_text():
    with open('./books/frankenstein.txt', encoding="utf-8") as f:
        print(f)
        Book = f.read()
    print(Book)
    
    


main()