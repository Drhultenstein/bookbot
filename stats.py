def count_words(text: str) -> int:
    words = text.split()
    return len(words)

def count_characters(text: str) -> dict:
    char_count = {}
    for char in text:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_characters(char_count: dict):
    char_list = []
    for char, count in char_count.items():
        char_dict = {"char": char, "count": count}
        char_list.append(char_dict)

    def sort_on(dict):
        return dict["count"]

    char_list.sort(reverse=True, key=sort_on)
    return char_list