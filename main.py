def main():
    book_path = "./books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        character_count = character_occurences(file_contents)
        generate_report(book_path, word_count, character_count)


def count_words(s: str):
    return len(s.split())


def character_occurences(s: str):
    s = s.lower()
    unique_chars = set(filter(lambda x: x.isalpha(), s))
    occurences = {}
    for c in unique_chars:
        occurences[c] = s.count(c)
    return occurences


def generate_report(book_path, word_count, letter_occurences):
    letter_occurences = list(
        map(lambda x: (x, letter_occurences[x]), letter_occurences)
    )
    letter_occurences.sort(reverse=True, key=lambda x: x[1])
    print(
        f"""
    ---BOOK REPORT:{book_path}---
    There were {word_count} words found in the document
    ***
    """
    )
    for letter, count in letter_occurences:
        print(f"The {letter} character was found {count} times.")
    print("---END OF REPORT---")


if __name__ == "__main__":
    main()
