import sys
from stats import count_words, count_characters, sorting

def get_book_text(path):
    with open(path, encoding="utf8") as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    
    number = count_words(text)
    print(f"Found {number} total words")

    total_chars, char_dict = count_characters(text)
    print("Total characters (including spaces and symbols):", total_chars)

    sorted_char_data = sorting(char_dict)
    print("Sorted alphabetical character counts:")
    for item in sorted_char_data:
        print(f"{item['char']}: {item['num']}")

if __name__ == "__main__":
    main()