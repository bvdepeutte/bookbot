def main():
    book_path = "books/Frankenstein.txt"
    text = get_book_text(book_path)
    # print(text)
    words = len(get_list(text))
    print(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_list(book_text):
    words = []
    words = book_text.split()
    # print(words)
    return words



main()