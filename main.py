
from stats import char_count, sort_statistics, word_count


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def print_char_statistics(sorted: list):
    print("--------- Character Count -------")
    for entry in sorted:
        char = entry["char"] + ""
        if char.isalpha():
            print(f"{char}: {entry["num"]}")

def print_word_statistict(count: int):
    print("----------- Word Count ----------")
    print(f"Found {count} total words")

def print_title(filepath: str):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")

def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    print_title(filepath)

    num_words = word_count(text)        
    print_word_statistict(num_words)

    char_stats = char_count(text)
    sorted = sort_statistics(char_stats)
    print_char_statistics(sorted)

    print("============= END ===============")

main()