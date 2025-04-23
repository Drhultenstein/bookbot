import sys

def get_book_text(book_path: str) -> str:
    with open(book_path, encoding="utf-8") as f:
        return f.read()
    
from stats import count_words
from stats import count_characters
from stats import sort_characters
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    try:
        book_text = get_book_text(book_path)
    except FileNotFoundError:
        print(f"Error: The file {book_path} was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

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
            print(f"{char_dict['char']}: {char_dict['count']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()