from abc import ABC, abstractmethod
# Wing Length, Can Fly, 
class Bird(ABC):
    eggs=0
    def diet(self):
        pass
    def lay_eggs(self):
        pass
class Owl(Bird):
    can_fly=True
    def diet(self):
        return 'Carnivore'
    def lay_eggs(self):
        self.eggs+=5
class Dodo(Bird):
    can_fly=False
    def diet(self):
        return 'Omnivore'
    def lay_eggs(self):
        self.eggs+=1
polly=Dodo()
print ('Dodo can fly:',polly.can_fly)
print ('Dodo diet:',polly.diet())
hoot=Owl()
print ('Owl can fly:',hoot.can_fly)
print ('Owl diet:',hoot.diet())
#print (polly.eggs)
polly.lay_eggs()
polly.lay_eggs()
polly.lay_eggs()
polly.lay_eggs()
polly.lay_eggs()
print ('Egg count of Dodo after laying 5 times',polly.eggs)
hoot.lay_eggs()
hoot.lay_eggs()
hoot.lay_eggs()
hoot.lay_eggs()
hoot.lay_eggs()
print ('Egg count of Owl after laying 5 times',hoot.eggs)

for x in (polly,hoot):
    print (x.diet())