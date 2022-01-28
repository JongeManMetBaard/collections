import random

color = ["oranje", "blauw", "groen", "bruin"]

def contentOfBag(amountOfmnm):
    bag = {}
    for x in range(amountOfmnm):
        randomColor = random.choice(color)
        if randomColor in bag:
            bag[randomColor] += 1
        else:
            bag[randomColor] = 1
    mnmDictionaryBag = {}
    return bag

amountOfmnm = int(input("How much M&M'S do you want?"))
print(contentOfBag(amountOfmnm))