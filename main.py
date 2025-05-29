
from stats import char_count, word_count


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    
def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = word_count(text)
    print(f"{num_words} words found in the document")

    char_stats = char_count(text)
    print(char_stats)

main()