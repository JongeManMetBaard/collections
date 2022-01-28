from operator import itemgetter
import random

color = ["oranje", "blauw", "groen", "bruin"]

def generateList(amountOfMMs):
    bag = []
    for x in range(amountOfMMS):
        bag.append(random.choice(color))
    return bag

def generateDictionary(amountOfmnm):
    bag = {}
    for x in range(amountOfmnm):
        randomColor = random.choice(color)
        if randomColor in bag:
            bag[randomColor] += 1
        else:
            bag[randomColor] = 1
    return bag


amountOfMMS = int(input("How much M&M'S do you want?"))
mnmListBag = generateList(amountOfMMS)
mnmDictBag = generateDictionary(amountOfMMS)

def sortBag(mnmBag):
    if isinstance(mnmBag, list):
        mnmBag.sort()
    else:
        mnmBag = dict(sorted(mnmBag.items(), key=itemgetter(1), reverse=True)) 
    return mnmBag

print(sortBag(mnmListBag))
print(sortBag(mnmDictBag))