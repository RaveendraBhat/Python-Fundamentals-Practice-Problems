1)Check the given number is even or odd

number = int(input("Enter the number: "))

if number%2 == 0:
    print("Number is even")
else:
    print("Number is odd")

#############

2)Enter the student maths marks, science marks, if maths marks greater than 70 and science marks greater than 65 passout year should be 2022d isplay he is eligible to take engineering course

maths = int(input("Enter the Maths score: "))
science = int(input("Enter the Science score: "))
yop = int(input("Enter the year of passing: "))

if maths>70 and science>65 and yop == 2022:
    print("Eligible for Engineering course")
else:
    print("Not eligible for Engineering course")

##############

3)create a list of products check the perticular product looking is available in stock or not

products = ['brush','soap','toothpaste','juice','icecream']

item = input("Enter the product name: ")

if item in products:
    print('Product is available')
else:
    print('Product is out of stock')
    
#############

4)write a program to check the inputed number is positive number or not

number = int(input("Enter the number: "))

if number>0:
    print("Number is positive")
else:
    print("Number is not positive")

#############

5)write a program to check the entered number within the range of 25 to 50

number = int(input("Enter the number: "))

if number >= 25 and number <= 50:
    print("Number is in range of 25 to 50")
else:
    print("Number is not in range of 25 to 50")

#############

6)enter a string check its capital letter or not

string = input("Enter the string: ")

if string == string.upper():
    print("String is in uppercase")
else:
    print("String is not in uppercase")

#############

7)enter a number if number completely divisible by 5 then add 10 to it else 5 to it

number = int(input("Enter the number: "))

if number % 5 == 0 :
    print("New number is: ", number+10)
else:
    print("New number is: ", number+5)

