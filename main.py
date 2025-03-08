import sys
from stats import get_num_words, get_char_count, get_sorted_list

def get_book_text(file_path):
    content = None
    with open(file_path) as f:
        content = f.read()
    
    return content

def main():
    file_path = sys.argv[1]
    content = get_book_text(file_path)
    num_words = get_num_words(content)
    char_count = get_char_count(content)
    sorted_char_list = get_sorted_list(char_count)

    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {file_path}...')
    print('----------- Word Count ----------')
    print(f'Found {num_words} total words')
    print('--------- Character Count -------')
    for x in sorted_char_list:
        if x['label'].isalpha():
            print(f'{x["label"]}: {x["count"]}')
    print('============= END ===============')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    
    main()