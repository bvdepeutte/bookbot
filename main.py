def main():
    book_path = "books/Frankenstein.txt"
    text = get_book_text(book_path).lower()
    # print(text)
    words = len(get_list(text))
    dic_letters = get_letter_count(text)
    list_dictionary = get_dict_list(dic_letters)
    print(f"--- Begin report of ", book_path," ---")
    print(words,"words found in the document")
    print("")
    for i in range(0, len(list_dictionary)):
        print(f"The '",list_dictionary[i]["name"],"' character was found",list_dictionary[i]["count"],"times")
    # print(list_dictionary)


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

def sort_on(dict):
    return dict["count"]


def get_dict_list(dictionary):
    dictionary_list = []
    for letter, count in dictionary.items():
        if letter.isalpha():
            dictionary_list.append({'name': letter,'count': count})
    dictionary_list.sort(reverse=True, key=sort_on)
    return dictionary_list

main()