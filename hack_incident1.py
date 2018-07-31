import string

def encrypt(text, shift):
    alphabet = list(string.ascii_lowercase)
    new_text = []
    shifted = ''.join(alphabet[-shift:] + alphabet[0:-shift])
    #teacher way to do the shifted
    #first_half = alphabet[:shift]
    #second_half = alphabet[shift:]
    #shifted = second_half + first_half
    #print(''.join(alphabet))
    #print(shifted)
    for i,letter in enumerate(text):
        if letter == ' ':
            new_text.append(' ')
        else:
            for y,alph in enumerate(alphabet):
                if letter.lower() == alph:
                    new_text.append(shifted[y])
    #teacher solution
    #for i,letter in enumerate(text.lower()):
    #   if letter in alphabet:
    #       locate the index of the character in the alphabet list
    #       original_index = alphabet.index(letter)
    #       locate the shifted letter in the shifted list with same index
    #       new_letter = shifted_alphabet[original_index]
    #       replace original letter with encripted letter
    #       encripted_text[i] = new_letter
    #   else:
    #       if letter not in the alphabet like a space or special character
    #       keep the special character without encription
    #       encrypted_text[i] = letter
    return ''.join(new_text)
encrypted = encrypt('Daniel is studying Python',12)
print(encrypted)
print('\n')

def decrypt(text, shift):
    alphabet = list(string.ascii_lowercase)
    old_text = []
    shifted = ''.join(alphabet[-shift:] + alphabet[0:-shift])
    #print(''.join(alphabet))
    #print(shifted)
    for i,letter in enumerate(text):
        if letter == ' ':
            old_text.append(' ')
        else:
            for y,alph in enumerate(shifted):
                if letter.lower() == alph:
                    old_text.append(alphabet[y])
    return ''.join(old_text)
decrypted = decrypt(encrypted,12)
print(decrypted)
print('\n')

def brute_force(message):
    for x in range(0,26):
        print('Using a shift value of {}'.format(x))
        print(decrypt(message,x))
        print('\n')
    return
brute_force(encrypted)
