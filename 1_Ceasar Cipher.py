def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            shifted_char = chr((ord(char) - ord('A' if is_upper else 'a') + shift) % 26 + ord('A' if is_upper else 'a'))
            result += shifted_char
        else:
            result += char
    return result

#input
shift_amount = int(input())
text_to_encrypt = input().strip()

#output
encrypted_text = caesar_cipher(text_to_encrypt, shift_amount)
print(encrypted_text)