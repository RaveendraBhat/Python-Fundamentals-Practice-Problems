1)add number from 15 to 25

i = 15
total_sum = 0
while i <=25:
    total_sum += i
    i+=1

print('The sum is ',total_sum)

###########

2)Enter 10 numbers count number of even numbers and odd numbers and sum of even and odd number

i = 0
count_even = 0
count_odd = 0
total_sum = 0

while i < 10:
    num = int(input("Enter the number: "))
    
    if num%2 == 0:
        count_even += 1
    else:
        count_odd +=1

    total_sum += num

    i += 1
    
print('Count of even numbers is ',count_even)
print('Count of odd numbers is ',count_odd)
print('Sum of numbers is ',total_sum)

############

3)input 5 numbers check its completerly divisible by 5 add those numbers
ex = input 1 = 5 ,input 1 = 10,input 1 = 3,input 1 = 25,input1 = 22
sum = 40

i = 0
total_sum = 0

while i < 5:
    num = int(input("Enter the number: "))

    if num%5 == 0:
        total_sum += num

    i += 1

print('Sum of numbers is ',total_sum)

############

4)input 5 subjects marks find total,average marks, if marks greater than 35 pass less than 35 fail 
count how many subjects are passes and how many are failed

i = 0
count_pass = 0
count_fail = 0
total_sum = 0

while i < 5:
    num = int(input("Enter the marks: "))
    
    if num >= 35:
        count_pass += 1
    else:
        count_fail +=1

    total_sum += num

    i += 1

print('No of subjects passed: ',count_pass)
print('No of subjects failed: ',count_fail)
print('Total marks is ',total_sum)
print('Average marks is ',total_sum/5)

############

5)input 5 numbers, if entered number is in the range of 25 to 75 
then add those numbers else count the numbers which are not in range of 25 to 75
input =5,6,88,25,35
sum = 60 (25+35)
count = 3 (5,6,88)

i = 0
count = 0
total_sum = 0

while i < 5:
    num = int(input("Enter the number: "))

    if num in range(25,76):
        total_sum += num
    else:
        count += 1

    i += 1

print("Sum of numbers in range of 25 to 75 is ",total_sum)
print("Count of numbers not in range of 25 to 75 is ",count)

############

6)Count how many Vowels and consonants in a string

string = input("Enter the string: ")
vowels = 0
consonants = 0
i = 0
vowels_list = ['a','e','i','o','u','A','E','I','O','U']

while i < len(string):
    if string[i] in list:
        vowels += 1
    else:
        consonants += 1

    i += 1

print('No of vowels in string: ',vowels)
print('No of consonants in string: ',consonants)

###########

7)Convert Upper to lower lower to upper case in a string if it is a number or spl character print as it is

string = input("Enter the string: ")
i = 0
new_string = ''
length = len(string)

while i < length:
    if string[i].isupper():
        s += string[i].lower()
    elif string[i].islower():
        s += string[i].upper()
    else:
        s += string[i]

    i += 1

print('New string is: ',new_string)

############

8)Based on the user input display the multiplication table

num = int(input("Enter the number: "))
i = 1

while i <= 10:
    print(i*num)

    i += 1

############

9)Based on the user input findout the factorial number

num = int(input("Enter the number: "))
fact = 1

while num > 0:
    fact = fact * num 

    num -= 1

print('Factorial is ',fact)

############

10)write a program to Reverse a string

string = input("Enter the string: ")

i = len(string)
new_string = ''

while i > 0:
    s += string[i-1]
    
    i -= 1

print("Reversed string is ", new_string)
        

    

    
    

        
    
