import string
import random

class Encryption():
    
    def __init__(self,seed):
        self.seed = seed
        self.enc_mes = ''
        self.alphabet = list(string.ascii_lowercase)
        shift = random.randint(1,self.seed)
        print(shift)
        self.shuffledalpha = ''.join(self.alphabet[shift:] + self.alphabet[:shift])
        print(self.alphabet)
        print(self.shuffledalpha)
    
    def encrypt(self, message):
        return

enc = Encryption(20)
