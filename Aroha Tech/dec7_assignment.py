1) Input any number find out is it single digit or double digit or triple digit number ex input is 22 print two digit number

number = int(input("Enter number less than 1000: "))

if number // 10 == 0:
    print("The number is single digit")
elif number // 100 == 0:
    print("The number is double digit")
else:
    print("The number is triple digit")

##############

2) find the greatest of 3 numbers

no_1 = int(input("Enter number1: "))
no_2 = int(input("Enter number2: "))
no_3 = int(input("Enter number3: "))
             
if no_1 >= no_2 and no_1 >= no_3:
    print('Greatest number is ',no_1)
elif no_2 >= no_1 and no_2 >= no_3:
    print('Greatest number is ',no_2)
else:
    print('Greatest number is ',no_3)
    
##############

3)Calculte BMI based value display the conditions

Height = int(input("Enter height in cm : "))
Weight = int(input("Enter weight in kg : "))

bmi  = Weight/(Height**2)*10000

print("BMI is ",bmi)

if bmi <= 18.5:
    print("Underweight")
elif 18.5 < bmi <= 25:
    print("Normal")
elif 25 < bmi <= 30:
    print("Overweight")
else:
    print("Obese")

################

4)write a program to display 
a)shortilisted for Bsc maths when puc avg>50,pcm_avg>70,maths>75 
b)when puc avg>50,pcm_avg<70 then display not eligible for B.Sc Maths(H), try for B.Sc General 
c)when puc avg< 50 then display not eligible for any course in this college

puc_avg = int(input("Enter puc_avg_percentage: "))
pcm_avg = int(input("Enter pcm_avg_percentage: "))
maths = int(input("Enter maths score: "))    
    
if puc_avg >= 50:
    if pcm_avg >= 70:
        if maths> 75:
            print("Shortilisted for B.Sc Maths")
        else:
            print("Not shortilisted for B.Sc Maths, try other course")
    else:
        print("Not eligible for B.Sc Maths(H), try for B.Sc General")
else:
    print("Not eligible for any course in this college")
    
#################

5) enter the state name and capital name based on the choice of state display the capital name

st1 = 'karnataka'
cp1 = 'bengaluru'
st2 = 'maharashtra'
cp2 = 'mumbai'
st3 = 'kerala'
cp3 = 'trivandrum'
st4 = 'tamil nadu'
cp4 = 'chennai'

ip = input("Enter state: ")

if ip == st1:
    print("Capital is ", cp1)
elif ip == st2:
    print("Capital is ", cp2)
elif ip == st3:
    print("Capital is ", cp3)
elif ip == st4:
    print("Capital is ", cp4)
else:
    print("No data found ")
    
    
