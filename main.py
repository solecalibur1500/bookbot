def get_book_text():
    with open("books/frankenstein.txt") as f:
        f_as_string = f.read()
        return f_as_string
def main():
    text = get_book_text()
    words = text.split()
    print (f"Found {(len(words))} total words")    
    return words
main()