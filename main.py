def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = count_characters(text)
    print(chars_dict)

# Function to split and get word count
def get_num_words(text):
    words = text.split()
    return len(words)

# Function to pull full book text
def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
    

# Function to separate characters and count them
def count_characters(text):
    lower_string = text.lower()
    lowered = {}
    for t in lower_string:
        lowered[t] = lowered.get(t, 0) + 1
    return lowered


main()