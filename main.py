import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

from stats import count
from stats import countchars
from stats import sort_on

def main():
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    wordcount = count(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {wordcount} total words")
    print("--------- Character Count -------")
    charcount = countchars(text)
    s = sort_on(charcount)
    for i in s:
        print(f"{i['char']}: {i['num']}")

main()