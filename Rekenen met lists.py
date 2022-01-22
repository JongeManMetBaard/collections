# Calc add
listOne = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listTwo = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

def addAndDisplayLists(list1, list2):
    print("---------")
    print("Add lists")
    for x in range(10):
        answer = list1[x] + list2 [x]
        print(list1[x], " + "    ,list2[x],     " = " ,(answer))
addAndDisplayLists(listOne, listTwo)

# Calc substract
def substractAndDisplayLists(list1, list2):
    print("---------")
    print("Substract lists")
    for x in range(10):
        answer = list1[x] - list2[x]
        print(list1[x], " - "    ,list2[x],     " = " ,(answer))
substractAndDisplayLists(listOne, listTwo)

# Calc multiply
def multiplyAndDisplayLists(list1, list2):
    print("---------")
    print("Multiply lists")
    for x in range(10):
        answer = list1[x] * list2[x]
        print(list1[x], " * "    ,list2[x],     " = " ,(answer))
multiplyAndDisplayLists(listOne, listTwo)

# Calc divide
def divideAndDisplayLists (list1, list2):
    print("---------")
    print("Divide lists")
    for x in range(10):
        answer = list1[x] / list2[x]
        print(list1[x], " / "    ,list2[x],     " = " ,(answer))
divideAndDisplayLists(listOne, listTwo)