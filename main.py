

def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    num_words = get_word_count(text)
    chars_dict = get_chars_dict(text)
    print_report(num_words, chars_dict, book_path)
    

def get_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(book):
    word_count = book.split()
    return len(word_count)


def get_chars_dict(text):
    chars = {}
    for c in text:
      if c.isalpha():
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1

    sorted_chars = dict(sorted(chars.items()))
    return sorted_chars
    

def print_report(num_words, char_dict, book_path):

    print(f"--- Begin Report Of {book_path} ---")
    print(f"{num_words} words found in the document")

    for key, value in char_dict.items():
        print(f"The '{key}' was found {value} times")

    print("--- End Report ---")
    

   
if __name__ == "__main__":
    main()