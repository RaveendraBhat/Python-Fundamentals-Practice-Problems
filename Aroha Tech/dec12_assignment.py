1)Print sum of all even numbers from 10 to 20

num_list = list(range(10,21))
total = 0

for i in num_list:
    if i%2 == 0:
        total += i

print("Total sum is ",total)

############

2)Calculate the square of each number of list
ex = [1,2,3,4] = [1,4,9,16]

num_list = list(range(1,6))
square_list = []

for i in num_list:
    square_list.append(i**2)

print("Square of numbers is",square_list)

#############

3)calculate li = [25,67,88,45,75] sum and avg 

li = [25,67,88,45,75]

length = len(li)
total = 0

for i in li:
    total += i

average = total/length

print("Sum is ",total)
print("Avg is ",average)

############

4)display all the even number in range 10 to 50

num_list = list(range(10,51))

even_list = []

for i in num_list:
    if i%2 == 0:
        even_list.append(i)

print(even_list)
        
############

5)Count how many 'P' characters are there in a given string

string = 'Python is Programming language'

count = 0

for i in string:
    if i == 'p' or i == 'P':
        count += 1

print("No. of 'P' char in string is ",count)

############

6)print list in reverse order

num_list = list(range(1,6))
rev_list = []

for i in num_list[::-1]:
    rev_list.append(i)

print("The reverse list is ",rev_list)

############

7)print factorial of given number

num = int(input("Enter the number: "))

fact = 1

if num > 1:
    for i in range(1,num+1):
        fact = fact*i

    print("Factorial of", num, "is", fact)
    
elif num == 0 or num == 1:
    print("Factorial of", num, "is", 1)
    
else:
    print("Invalid number")

############

8)Convert Upper to lower lower to upper case in a string
if it is a number or spl character print as it is

string = input("Enter the string: ")
new_string = ''

for i in string:
    if 'a'<= i <= 'z':
        new_string += chr(ord(i)-32)
    elif 'A'<= i <= 'Z':
        new_string += chr(ord(i)+32)
    else:
        new_string += i
    
print("The new string is ",new_string)

############

9)Count how many Vowels and consonants in a string

string = input("Enter the string: ")

vowel_list = ['a','e','i','o','u','A','E','I','O','U']
 
vowels = 0
consonants = 0

for i in string:
    if i in vowel_list:
        vowels += 1
    else:
        consonants += 1

print("No. of vowels is",vowels)
print("No. of consonants is",consonants)

#############

10)input 5 numbers,if entered number is in the range of 15 to 30 then add those numbers
else count the numbers which are not in range 15 to 30

count = 0
total = 0

for i in range(0,5):
    num = int(input("Enter the number: "))

    if num in range(15,31):
        total += num
    else:
        count += 1

print("Sum of numbers in the range of 15 to 30 is",total)
print("Count of numbers not in the range of 15 to 30 is",count)

