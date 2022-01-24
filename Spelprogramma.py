import random

spelList = [ 'Monopoly', 'Yathzee', 'Bridge', 'Poker', 'Pesten', 'Mens erger je niet', 'Cluedo']


def spelProgramma(spelList):
    listResult = []
    for x in range(random.randrange(3,11)):
        listResult.append(random.choice(spelList)) 
    return listResult

print("---------------------Lijst 1------------------------------------")
print(spelProgramma(spelList))  

import random

spelList = [ 'Monopoly', 'Yathzee', 'Bridge', 'Poker', 'Pesten', 'Mens erger je niet', 'Cluedo']


def spelProgramma(spelList, minimum):
    listResult = []
    for x in range(random.randrange(minimum, 11)):
        listResult.append(random.choice(spelList)) 
    return listResult

print("---------------------Lijst 2------------------------------------")
print(spelProgramma(spelList, 3))  


import random

spelList = [ 'Monopoly', 'Yathzee', 'Bridge', 'Poker', 'Pesten', 'Mens erger je niet', 'Cluedo']


def spelProgramma(spelList, minimum, maximum):
    listResult = []
    for x in range(random.randrange(minimum, maximum)):
        listResult.append(random.choice(spelList)) 
    return listResult

print("---------------------Lijst 3------------------------------------")
print(spelProgramma(spelList, 3, 11))  