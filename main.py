def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    book_char = get_book_char(text)
    char_report = get_char_report(book_char)
    print(f"{num_words} words found in the document")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_book_char(text):
    uniqueCharacters = {}
    for i in text:
        lower=i.lower()
        if lower.isalpha() == True :
            if lower in uniqueCharacters:
                uniqueCharacters[lower] +=1
            else:
                uniqueCharacters[lower] = 1
    return uniqueCharacters

def get_char_report(uniqueCharacters):
    sorted_characters = sorted(uniqueCharacters.items(), key=lambda item: item[1], reverse=True)
    for char in sorted_characters:
        print(f"The {char[0]} character was found {char[1]} times")


main()
