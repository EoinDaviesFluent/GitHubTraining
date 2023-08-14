import random
class Dice:
    def __init__(self,sides_of_dice):
        self.faces=sides_of_dice
    def roll(self):
        return (random.randint(1,self.faces))

dice_1=Dice(6)
dice_2=Dice(20)
dice_3=Dice(2)
dice_4=Dice(4)

print (dice_1.roll())