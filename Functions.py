#P1
def max_of_two(x,y):
    if x > y:
        return x
    return y
     
def max_of_three(x,y,z):
    return max_of_two(x, max_of_two(y,z))

print(max_of_three(5,8,2))

#P2
def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total

print(multiply([1,2,3,4]))
print(multiply({1,2,3,4}))
print(multiply((1,2,3,4)))

#P3
def caseCounter(string):
    d = {"UPPER_CASE": 0, "LOWER_CASE": 0}
    for c in string:
        if c.isupper():
            d["UPPER_CASE"] += 1
        elif c.islower():
            d["LOWER_CASE"] += 1
        else:
            pass
    print(f'The number of uppercase characters are {d["UPPER_CASE"]}')
    print(f'The number of lowercase characters are {d["LOWER_CASE"]}')

print(caseCounter('GooD MorNIng'))

#P4
def duplicateEliminator(list):
    return set(list)
print(duplicateEliminator([1,2,1,2,3,3]))

#P5
def squareMachine(list):
    l = []
    for i in list:
        x = i*i
        l.append(x)
    return l

print(squareMachine([1,2,3,4,5,10,5,7,1,8,2]))

def squareMachine(theList):
    i = 0
    while i < len(theList):
        theList[i] = theList[i] ** 2
        i+=1
    return theList

print(squareMachine([1,2,3,4,5]))

#P6
def dictDecomposer(theDict):
    print('The keys of the dictionary are',list(theDict.keys()))
    print('The values of the dictionary are',list(theDict.values()))

print(dictDecomposer({'firstName':'Nick', 'lastName':'McCullum'}))
    
