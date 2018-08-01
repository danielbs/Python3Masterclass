class Sphere():
    pi = 3.141592

    def __init__(self,radius):
        self.radius = radius
    
    def surface_area(self):
        return 4 * Sphere.pi * self.radius * self.radius
    
    def volume(self):
        return (4 / 3) * Sphere.pi * self.radius * self.radius * self.radius

s = Sphere(3)
print(s.surface_area())
print(s.volume())
