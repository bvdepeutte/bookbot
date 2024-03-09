def main():
    book_path = "books/Frankenstein.txt"
    text = get_book_text(book_path).lower()
    # print(text)
    words = len(get_list(text))
    dic_letters = get_letter_count(text)
    print(dic_letters)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_list(book_text):
    words = []
    words = book_text.split()
    # print(words)
    return words

def get_letter_count(text):
    letters = {}
    for i in range(len(text)):
        if text[i] in letters:
            letters[text[i]] += 1
        else:
            letters[text[i]] = 1
    return letters

main()