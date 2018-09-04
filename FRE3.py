import string
import random

class Encryption():
    
    def __init__(self,seed):
        self.seed = seed
        self.enc_mes = ''
        self.alphabet = list(string.ascii_lowercase)
        random.seed(self.seed)        
        self.shuffled = random.sample(self.alphabet,len(self.alphabet))
        print(self.alphabet)
        print(self.shuffled)
    
    def encrypt(self, message):
        enl = []
        y=0
        self.message = message
        random.seed(self.seed)
        for x in self.message:
            z = y*2
            enl.insert(z,x)
            enl.insert(z+1,self.alphabet[random.randint(0,25)])
            y += 1
        print(enl)
        enl.reverse()
        print(enl)
        #teacher solution to reverse the string
        #self.encrypted_phrase = output[::-1]
        h_msg = ''.join(enl)        
        for i,letter in enumerate(h_msg.lower()):
            if letter in self.alphabet:
        #       locate the index of the character in the alphabet list
                original_index = self.alphabet.index(letter)
    #       locate the shifted letter in the shifted list with same index
                new_letter = self.shuffled[original_index]
    #       replace original letter with encripted letter
                enl[i] = new_letter
            else:
    #       if letter not in the alphabet like a space or special character
    #       keep the special character without encription
                enl[i] = letter
        print(enl)
        return ''.join(enl)
    
    def decrypt(self,message):
        d_msg = []
        dec_msg = []
        y = 0
        self.message = message
        for letter in self.message:
            d_msg.append(letter)
        print(d_msg)
        for i,letter in enumerate(self.message.lower()):
            if letter in self.shuffled:
                shuffled_index = self.shuffled.index(letter)
                new_letter = self.alphabet[shuffled_index]
                d_msg[i] = new_letter
            else:
                d_msg[i] = letter
        print(d_msg)
        d_msg.reverse()
        print(d_msg)
        for i, letter in enumerate(d_msg):
            if i % 2 == 0:
                dec_msg.insert(y, d_msg[i])
            y += 1
        print(dec_msg)
        #teacher solution to take evry other letter
        #decrypted_message[::2]
        return ''.join(dec_msg)

enc = Encryption(20)
enc_msg = enc.encrypt('hello world')
dec_meg = enc.decrypt(enc_msg)
print(dec_meg)
