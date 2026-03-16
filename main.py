import sys
from stats import get_num_words, get_num_chars, sort_counts

def get_book_text(file_path):
    with open(file_path) as f: 
        contents = f.read()
        return contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    book = sys.argv[1]
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    book_text = get_book_text(book)
    num_words = get_num_words(book_text)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    counts = get_num_chars(book_text)
    counts_list = []
    for char in counts:
        counts_list.append({"char": char, "num": counts[char]})
    sorted_counts_list = sort_counts(counts_list)
    for item in sorted_counts_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()