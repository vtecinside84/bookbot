from stats import get_wordcount, get_each_letter_count, sorted_letter_count
import sys

def get_book_text(path_to_file):
    
    with open(path_to_file) as f:
        file_contents = f.read()
        return(file_contents)
        
def main():
    if len(sys.argv) > 1:
        path_to_file = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {get_wordcount(get_book_text(path_to_file))} total words")
    print("----------- Character Count ----------")
    sorted_letter_count(get_each_letter_count(get_book_text(path_to_file)))
    print("============= END ===============")
main()
