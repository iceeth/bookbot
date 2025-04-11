def get_books_text():
    with open('./books/frankenstein.txt', encoding="utf-8") as f:
        file_contents = f.read()
        words = file_contents.split()
        Num_Words = len(words)
        return Num_Words

def letter_count(sys):
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path = sys.argv[1]  # Get the first argument after the script name
        
    with open(file_path, encoding="utf-8") as f:
        file_contents = f.read()
    Conv_LwCase = file_contents.lower()
    letter_dict = {}
    for letter in Conv_LwCase:
        if letter.isalpha():
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1
    return letter_dict

def Print_Report(letter_dict, Num_Words):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {Num_Words} total words")
    print("----------- Character Count ----------")
    # Sort the dictionary items by count (value) in descending order
    sorted_letters = sorted(letter_dict.items(), key=lambda x: x[1], reverse=True)
    
    # Print each letter and its count
    for letter, count in sorted_letters:
        print(f"{letter}: {count}")
    
    print("============= END ===============")
