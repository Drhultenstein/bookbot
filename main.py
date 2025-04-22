def get_book_text(book_path: str) -> str:
    with open(book_path) as f:
        return f.read()
    
def count_words(text: str) -> int:
    words = text.split()
    return len(words)
    
def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    print(f"{count_words(book_text)} words found in the document")


if __name__ == "__main__":
    main()