'''
1)input cost price, input desired profit percentage find selling price
sp--->selling price
cp---->cost price
sp = CP + (CPxprofit percentage)
'''

cp = float(input("Enter cost price: "))
profit_per = float(input("Enter profit percentage: "))

sp = cp + (cp * (profit_per/100))

print("The Selling Price is ",sp)
                   
'''
2)Input the product price,qty,Gst in percentage. Find the total amount of the the product
'''

product_price = float(input("Enter product price: "))
Quantity = int(input("Enter no. of items: "))
gst = float(input("Enter gst in percentage: "))

TA = (product_price * Quantity) + ((product_price * Quantity)*(gst/100))

print("The Total Amount is ",TA)

'''
3)Input 2 numbers check the relation ship between those numbers
ex: Input_1 = 86
    Input_2 = 47
Input_1 > Input_2 ----True
check for all condition
'''

input1 = int(input("Enter input1: "))
input2 = int(input("Enter input2: "))
a = input1 > input2
b = input1 < input2
c = input1 >= input2
d = input1 <= input2
e = input1 != input2
f = input1 == input2
print("input1  > input2: ",a)
print("input1  < input2: ",b)
print("input1 >= input2: ",c)
print("input1 <= input2: ",d)
print("input1 != input2: ",e)
print("input1 == input2: ",f)

'''
4)Input 6 Subjects Marks find the total Marks,and Percentage
'''

Physics = int(input("Enter Physics marks: "))
Chemistry = int(input("Enter Chemistry marks: "))
Maths = int(input("Enter Maths marks: "))
English = int(input("Enter English marks: "))
Kannada = int(input("Enter Kannada marks: "))
Sanskrit = int(input("Enter Sanskrit marks: "))

Marks_Scored = Physics + Chemistry + Maths + English + Kannada + Sanskrit

Total_Marks = int(input("Enter Total marks: "))

Percentage = (Marks_Scored/Total_Marks)*100

print("Marks Scored is ", Marks_Scored)
print("Total Percentage is ", Percentage)

'''
5)Based on user input Height and Weight calculate BMI(Body Mass Index)
BMI  = Weight/Height^2
'''

Height = int(input("Enter height in cm : "))
Weight = int(input("Enter weight in kg : "))

BMI  = Weight/(Height**2)*10000

print("BMI is ",BMI)

