import sys


def get_book_text(filepath: str):
    with open(filepath, encoding="utf-8") as f:
        for line in f:
            for word in line.split():
                yield word

def word_count(filepath: str):
    words = list(get_book_text(filepath))
    return len(words)

def count_characters(filepath: str):
    words = list(get_book_text(filepath))
    character_counts = {}
    for word in words:
        for char in word.lower():
            character_counts[char] = character_counts.get(char, 0) + 1
    return character_counts

def get_num(d):
    return d["num"]


def build_sorted_list(char_dict):
    result = []

    for char, count in char_dict.items():
        if char.isalpha():
            result.append({"char": char, "num": count})

    result.sort(key=get_num, reverse=True)

    return result

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    words = word_count(book_path)
    chars = count_characters(book_path)

    print("----------- Word Count ----------")
    print(f"Found {words} total words")

    print("--------- Character Count -------")
    sorted_chars = build_sorted_list(chars)

    for entry in sorted_chars:
        print(f"{entry['char']}: {entry['num']}")

    print("============= END ===============")