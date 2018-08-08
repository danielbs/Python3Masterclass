class Sphere():
    pi = 3.141592

    def __init__(self,radius):
        self.radius = radius
    
    def surface_area(self):
        return 4 * Sphere.pi * self.radius**2
    
    def volume(self):
        return (4 / 3) * Sphere.pi * self.radius**3

s = Sphere(5)
print(s.surface_area())
print(s.volume())

from random import randint
class GuessingGame():
    
    def __init__(self):
        rc = randint(0,100)
        self.rand_choice = rc
    def reset_random(self,rand_choice):
        self.rand_choice = randint(0,10)
    def guess(self, num):
        self.num = num
        if self.num == self.rand_choice:
            return True
        elif self.num > self.rand_choice:
            return 'big'
        else:
            return 'small'
gg = GuessingGame()
g_num = int(input('Please enter your guess: '))
while gg.guess(g_num) != True:    
    if gg.guess(g_num) == 'big':
        print('Your number is bigger than mine')
    else:
        print('Your number is smaller than mine')
    g_num = int(input('Please enter your guess: '))
    gg.guess(g_num)
print('You are correct')
