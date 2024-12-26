def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    book_char = get_book_char(text)
    print(f"{num_words} words found in the document")
    print(f"Unique letters:{book_char}")


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
        if lower in uniqueCharacters:
            uniqueCharacters[lower] +=1
        else:
            uniqueCharacters[lower] = 1
    return (uniqueCharacters)

main()
