def main ():
    get_books_text()

def get_books_text():
    with open('./books/frankenstein.txt', encoding="utf-8") as f:
        file_contents = f.read()
        words = file_contents.split()
        Num_Words = len(words)
        print(f"{Num_Words} words found in the document")
    
main()