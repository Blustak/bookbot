def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        print(f"Word count:{word_count}")


def count_words(s: str):
    return len(s.split())


if __name__ == "__main__":
    main()
