1)Registartion process
a)Enter user name check is it available already if not go and create a pass word
b)password length should greater than 8 len(password) > 8
--and contains only alphanumeric value
--if password contain spl charcter you cannot create password

username = input("Enter username: ")

u_list = ['ravi','raghu','ramesh','suresh','sudi']

if username not in u_list:
    password = input("Enter your password:")
    if len(password) > 8:
        if password.isalnum():
            print("Password created successfully")
        else:
            print("Please enter password which contains only alphanumeric values")
    else:
        print("Please enter password which contains more than 8 characters")
else:
    print("User exists, Please enter password to continue")

###########

2)person age
0-14 - children
15-24 - youth
25-64 - adult
65 > senior citizen
Display the value based on age

age = int(input("Enter your age: "))

if 0 <= age <= 14:
    print("You belong to Children category")
elif 15 <= age <= 24:
    print("You belong to Youth category")
elif 25 <= age <= 64:
    print("You are an Adult")
elif age >= 65:
    print("You are a Senior Citizen")
else:
    print("Invalid age")

############

3)input the gross salary of the employee per month
    given tax to be computed is as following 
    salary above 70000 then tax is 14.5%
    salary above 50000 but less than 70000 then tax is 10.5%
    salary above 35000 but less than 50000 then tax is 7.5%

    net salary = gross salary - tax
    display the net salary after the tax is computed and dedcuted

gross_sal = int(input("Enter your salary: "))

if gross_sal >= 70000:
    tax = (14.5*gross_sal)/100
    net_sal = gross_sal - tax
    print("Net salary is ",net_sal)
elif 50000 <= gross_sal < 70000:
    tax = (10.5*gross_sal)/100
    net_sal = gross_sal - tax
    print("Net salary is ",net_sal)
elif 35000 <= gross_sal < 50000:
    tax = (7.5*gross_sal)/100
    net_sal = gross_sal - tax
    print("Net salary is ",net_sal)
else:
    print("Net salary is ",gross_sal)
    
############

4)Enter a single character display weather its capital/small/number or special character

char = input("Enter the character: ")

if 'A'<=char<='Z':
    print("It's a capital letter")
elif 'a'<=char<='z':
    print("It's a small letter")
elif '0'<=char<='9':
    print("It's a number")
else:
    print("It's a special character")

############

5) check whether the this number m = 125 is three digit number or not and is this divisible by 5 as well as 7 ?

m = 125

if 100<=m<=999:
    print("m is a three digit number")
    if m%5==0 and m%7==0:
        print("m is divisible by both 5 and 7")
    else:
        print("m is not divisible by both 5 and 7")
else:
    print("m is not a three digit number")

############

6)sales commision is given on following criteria if the sales made is 
	more than  100000 per month then the commision % is 6.5%
	more than 78000 but less than 100000 then the commision % is 5%
	more than 60000 but less than 78000 then the commision % is 4%
	more than 50000 but less than 60000 then the commision is 3%
	otherwise no commission

Total_Sales_Amount = int(input("Enter total sales amount: "))

if Total_Sales_Amount >= 100000:
    com =  (Total_Sales_Amount * 6.5)/100
    print("Commision is 6.5% i.e",com)
elif 78000 <= Total_Sales_Amount < 100000:
    com =  (Total_Sales_Amount * 5)/100
    print("Commision is 5% i.e",com)
elif 60000 <= Total_Sales_Amount < 78000:
    com =  (Total_Sales_Amount * 4)/100
    print("Commision is 4% i.e",com)
elif 50000 <= Total_Sales_Amount < 60000:
    com =  (Total_Sales_Amount * 3)/100
    print("Commision is 3% i.e",com)
else:
    print("No commision")

############

7) input the cost price of the item
   input the type of the item
   lets say the type of item would be 
   one of these....
    A
    B
    C
     if the item type is A then the profit percentage is 10% of the item cost
     if the item type is B then the profit percentage is 13% of the item cost
     if the item type is C then the profit percentage is 15.5% of the item cost
     display the selling price 

Note selling price = cost price of the item + profit percentage on the cost price
example....
if the cost price is 150 and the type of item is B then 13% is the profit percentage
150 + (150 * 13/100)  ::: will be the selling price

cp = int(input("Enter the cost price: "))
prod_type = input("Enter the type of the product: ")

if prod_type == 'A':
    pp = 10
    sp = cp + (cp*pp/100)
    print("Selling price is", sp)
elif prod_type == 'B':
    pp = 13
    sp = cp + (cp*pp/100)
    print("Selling price is", sp)
elif prod_type == 'C':
    pp = 15.5
    sp = cp + (cp*pp/100)
    print("Selling price is", sp)
else:
    print("Product type does not exist")
    

          
