import random

color = ["oranje", "blauw", "groen", "bruin"]

def contentOfBag(amountOfMMs):
    bag = []
    for x in range(amountOfMMS):
        bag.append(random.choice(color))
    return bag

amountOfMMS = int(input("How much M&M'S do you want?"))
print(contentOfBag(amountOfMMS))
