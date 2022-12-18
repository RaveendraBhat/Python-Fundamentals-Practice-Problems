1) input a number and check whether the FIRST and the LAST digits are same
 example:  96789
           |   |   they are same
 note it should be atleast a THREE digit number...


num = int(input("Enter the number: "))


if num > 99:

    last_digit = num % 10

    while num >= 10:
        num = num // 10
    
        first_digit = num
    
    if first_digit == last_digit:
        print("FIRST and the LAST digits are same")
    else:
        print("FIRST and the LAST digits are not same")

else:
    print("Please enter atleast a THREE digit number...")
    
 
OR


num = int(input("Enter the number: "))

if num > 99:
    string = str(num)

    if string[0] == string[-1]:
        print("FIRST and the LAST digits are same")
    else:
        print("FIRST and the LAST digits are not same")
else:
    print("Please enter atleast a THREE digit number...")



2) Given a text ="ABC-4567-WXYZ-23091929-FGH" something like this...
find all the digits , sum them up
display the total and the avg
if there are no digits then it should display NO DIGITS FOUND


text = "ABC-4567-WXYZ-23091929-FGH"

total = 0
count = 0

for i in text:
    if '0' <= i <='9':
        total += int(i)
        count += 1

if count == 0:
    print("NO DIGITS FOUND")
else:
    avg = total/count

    print("Total sum is",total)
    print("Average is",avg)


3) once 1) is working... then attempt this...
check whether the LAST digit and SECOND DIGIT is matching
96786  
 |  |   matching 
    last
second


num = int(input("Enter the number: "))

last_digit = num % 10

while num >= 100:    
    num = num // 10
    
    second_digit = num % 10
    
if second_digit == last_digit:
    print("SECOND and the LAST digits are same")
else:
    print("SECOND and the LAST digits are not same")


OR


num = int(input("Enter the number: "))

string = str(num)

if string[1] == string[-1]:
    print("SECOND and the LAST digits are same")
else:
    print("SECOND and the LAST digits are not same")
