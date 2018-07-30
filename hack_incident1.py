import string

def encrypt(text, shift):
    alphabet = list(string.ascii_lowercase)
    new_text = []
    shifted = ''.join(alphabet[-shift:] + alphabet[0:-shift])
    print(''.join(alphabet))
    print(shifted)
    for i,letter in enumerate(text):
        if letter == ' ':
            new_text.append(' ')
        else:
            for y,alph in enumerate(alphabet):
                if letter.lower() == alph:
                    new_text.append(shifted[y])
    return ''.join(new_text)
encrypted = encrypt('Daniel is studying Python',12)
print(encrypted)

def decrypt(text, shift):
    alphabet = list(string.ascii_lowercase)
    old_text = []
    shifted = ''.join(alphabet[-shift:] + alphabet[0:-shift])
    print(''.join(alphabet))
    print(shifted)
    for i,letter in enumerate(text):
        if letter == ' ':
            old_text.append(' ')
        else:
            for y,alph in enumerate(shifted):
                if letter.lower() == alph:
                    old_text.append(alphabet[i])
    return ''.join(old_text)
decrypted = encrypt(encrypted,12)
print(decrypted)
