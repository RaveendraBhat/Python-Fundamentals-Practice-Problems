1)Print the sum of the current number and the previous number --10 numbers

ex Current Number 1 Previous Number  0  Sum:  1
Current Number 2 Previous Number  1  Sum:  3
Current Number 3 Previous Number  2  Sum:  5

count = 0
prev_num = 0

while count < 10:
    curr_num = int(input("Enter the number: "))
    total = prev_num + curr_num
    prev_num = curr_num
    
    print("Sum of last two numbers is ", total)

    count += 1


2)Print characters from a string that are present at an even index number

string = input("Enter the string: ")

length = len(string)

for i in range(length):
    if i>0 and i%2 == 0:
        print(string[i], end=' ')


3)Find the sum of the series upto n terms
2 + 22 + 222 + 2222 + 22222 = 24690

num = int(input("Enter the number: "))
start = 2
total = 0

for i in range(num):
    print(start)
    total += start
    start = (start*10)+2
               
print("Total sum is ", total)


4)count total no of digits num = 1234567891

num = int(1234567891)
count = 0
string = str(num)

for i in string:
    count += 1

print('Total no of digits are',count)


5)Write a program to print fibonacii series upto 10 number

num = int(input("Enter the number: "))

a = 0
b = 1

for i in range(10):
    print(a, end = ' ')
    c = a+b
    b = a
    a = c


6)Leap year 
a)input date   - 31
b)input month 04
c)input year 2022
check weather it’s a leap year
conditions
date should be valid
month should be valid
year should be valid

check weather its a leap year or not
if (year%4 == 0 and year%100 !=0) or year%400==0:


date =  int(input("Enter the date: "))  
month =  int(input("Enter the month: "))
year =  int(input("Enter the year: "))

month_31 = [1,3,5,7,8,10,12]

if 1 <= month <= 12:
    if month in month_31:
        if 1 <= date <= 31:
            if (year%4 == 0 and year%100 != 0) or year%400 ==0:
                print("Its a Leap Year")
            else:
                print("Not a Leap Year")
        else:
            print("Invalid date")
    elif month == 2:
        if 1 <= date <= 29:
            if (year%4 == 0 and year%100 != 0) or year%400 ==0:
                print("Its a Leap Year")
            else:
                print("Not a Leap Year")
        else:
            print("Invalid date")
    else:
        if 1 <= date <= 30:
            if (year%4 == 0 and year%100 != 0) or year%400 ==0:
                print("Its a Leap Year")
            else:
                print("Not a Leap Year")
        else:
            print("Invalid date")

else:
    print("Invalid month")









