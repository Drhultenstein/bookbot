import os

def get_book_text(book_path: str) -> str:
    with open(book_path, encoding="utf-8") as f:
        return f.read()
    
from stats import count_words
from stats import count_characters
    
def main():
    script_dir = os.path.dirname(__file__)  # folder where main.py is
    book_path = os.path.join(script_dir, "books", "frankenstein.txt")
    book_text = get_book_text(book_path)
    print(f"{count_words(book_text)} words found in the document")

    char_counts = count_characters(book_text)
    print(char_counts)


if __name__ == "__main__":
    main()