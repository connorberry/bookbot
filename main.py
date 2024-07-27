def main():
    book_name = "frankenstein.txt"
    book_path = f"books/{book_name}"
    file_contents = get_text(book_path)
    #print(file_contents)

    words = count_words(file_contents)
    char_counts = count_chars(file_contents) 
    #print(f"there are {words} words in {book_name}")
    #print(f"Character counts in {book_name}:")
    #print(char_counts)
    char_stats = sort_chars(char_counts)
    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document")
    print()
    for stat in char_stats:
        if stat["char"].isalpha():
            char = stat["char"]
            count = stat["count"]
            print(f"The {char} character was found {count} times")
    print("--- End Report ---")



def count_words(data):
    return len(data.split())


def count_chars(text):
    counts = {}
    for c in text.lower():
        try:
            counts[c] += 1
        except KeyError:
            counts[c] = 1
    return counts


def get_text(filename):
    file_contents = None
    with open(filename) as f:
        file_contents = f.read()
    return file_contents


def sort_on(dict):
    return dict["count"]


def sort_chars(char_counts):
    char_stats = []
    for char in char_counts:
        new_dict = {"char": char, "count": char_counts[char]}
        char_stats.append(new_dict)
    char_stats.sort(reverse=True, key=sort_on)
    return char_stats


if __name__ == "__main__":
    main()
