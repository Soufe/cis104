sentence = input()
letter_frequency = {}
for char in sentence:
    if char.isalpha():
        char = char.lower()
        letter_frequency[char] = letter_frequency.get(char, 0) + 1
for letter in sorted(letter_frequency):
    print(f"{letter} {letter_frequency[letter]}")