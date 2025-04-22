import os

def get_book_text(book_path: str) -> str:
    with open(book_path, encoding="utf-8") as f:
        return f.read()
    
from stats import count_words
from stats import count_characters
from stats import sort_characters
    
def main():
    script_dir = os.path.dirname(__file__)  # folder where main.py is
    book_path = os.path.join(script_dir, "books", "frankenstein.txt")
    book_text = get_book_text(book_path)

    word_count = count_words(book_text)
    char_counts = count_characters(book_text)
    sorted_chars = sort_characters(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char_dict in sorted_chars:
        if char_dict["char"].isalpha():
            print(f"{char_dict["char"]}: {char_dict["count"]}")
    print("============= END ===============")

if __name__ == "__main__":
    main()