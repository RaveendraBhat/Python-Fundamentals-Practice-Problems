1)Write a program to display all the character except t and o
st = 'Python'

string = 'Python'

for char in string:
    if char == 't' or char == 'o':
        continue
    else:
        print(char, end='')


2)Write a program to iterate the integer from 1 to 25 
a)if no completely divide by 4 and 5 then print "zigzog"
b)if no completely divide by 4 and not by 5 print "zig"
c)if no completely divide by not by 4 and by 5 print "zog"
d)not by any number print the number

start = 1
end = 26

for num in range(start,end):
    if num%5 == 0 and num%4 == 0:
        print("zigzog")
    elif num%4 == 0 and num%5 != 0:
        print("zig")
    elif num%5 == 0 and num%4 != 0:
        print("zog")
    else:
        print(num)


3)Based on user input month display how many days are there on perticular month

month = int(input("Enter the month: "))

month_31 = [1,3,5,7,8,10,12]

if month in month_31:
    print("No. of days are",31)
elif month == 2 :
    year = int(input("Enter the year: "))
    
    if (year%4 == 0 and year%100 != 0) or year%400 ==0:
        print("No. of days are",29)
    else:
        print("No. of days are",28)
else:
    print("No. of days are",30)


4)check the given no is prime or not 
A prime number is a number that is only divisible by 1 and itself.

num = int(input("Enter the number: "))

if num > 1:
    for i in range(2,num):
        if num % i == 0:
            print("The number is not prime")
            break
    else:
        print("The number is prime")
else:
    print("The number is not prime")


5)write a program to check the number is armstrong or not
Armstrong number is a number that is equal to the sum of cubes of its digits.
For example 0, 1, 153, 370, 371 and 407 are the Armstrong numbers.

num = int(input("Enter the number: "))
total = 0
string = str(num)

for i in string:
    total += (int(i)**3)

if total == num:
    print("The number is an Armstrong number")
else:
    print("The number is not an Armstrong number")
    

6)print largest and smallest no in list

num_list = [5,8,9,7,6,1,3,4,6]

largest = max(num_list)
smallest = min(num_list)

print("Smallest number is",smallest)
print("Largest number is",largest)


7)print sum of nested loops

li = [[1,2,3],[4,5,6],[7,8,9]]

num_sum = 0

for num in li:
    num_sum += sum(num)

print("Sum of nested loops is",num_sum)


8) if list contain string the reverse the string and print other data type print as it is

li = ['python',1,2,"123",3+4j,"java"]

str_typ = "<class 'str'>"

for ele in li:
    if str(type(ele)) == str_typ :
        print(ele[::-1])
    else:
        print(ele)


9)Check the 2 given string is anagram
eat = ate >> anagram

str1 = input("Enter string1: ")
str2 = input("Enter string2: ")

list1 = sorted(str1)
list2 = sorted(str2)

if list1 == list2:
    print("The two strings are Anagrams")
else:
    print("The two strings are not Anagrams")
    
 
10) display how many string elements in a list

li = ['python',1,2,"123",3+4j,"java"]

str_typ = "<class 'str'>"
count = 0

for ele in li:
    if str(type(ele)) == str_typ :
        count += 1

print("No. of string elements in a list are",count)
