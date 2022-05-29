#P1
trueBool = True
falseBool = False

print(trueBool != falseBool)

#P2
firstMeal = 'breakfast'
secondMeal = 'lunch'
thirdMeal = 'supper'

print(firstMeal != secondMeal != thirdMeal)

#P3
variable = True
print(not variable)

#P4
one = 1
two = 2

areTheyEqual = one == two
print(areTheyEqual)

#P5
var1 = True
var2 = False
var3 = True

print(var1 and var2 and var3)
print(var1 or var2 or var3)

#P6
var1 = 5
var2 = 4
if (var1>var2):
    print('var1 is greater than var2')
else:
    print('var2 is greater than or equal to var1')

#P7
number = 100
if(number<10):
    print('Number is less than 10')
elif(number>=10 and number<=20):
    print('Number is between 10 and 20,inclusive')
else:
    print('Number is greater than 20')
