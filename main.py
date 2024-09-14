def get_book_text():
    with open("books/frankenstein.txt", encoding="utf-8") as file:
        file_contents = file.read()
    return file_contents


def get_num_words(file_contents):
    words = file_contents.split()
    return len(words)


def count_characters(file_contents):
    character_counts = {}


def main():
