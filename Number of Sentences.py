def number_of_sentences(text_filename):
    with open(text_filename, 'r', encoding='utf-8') as file:
        content = file.read()
    
    sentences = content.split('.')

    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

    return len(sentences)