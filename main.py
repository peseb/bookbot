
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    
def word_count(text: str):
    words = text.split()
    return len(words)

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = word_count(text)
    print(f"{num_words} words found in the document")

main()