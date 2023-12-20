def number_of_words(text_filename):
    with open(text_filename, 'r', encoding='utf-8') as file:
        content = file.read()
    words = content.split()

    return len(words)