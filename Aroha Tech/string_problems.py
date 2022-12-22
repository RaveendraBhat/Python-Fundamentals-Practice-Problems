1)Count the number of vowels and consonants in a string

string = input("Enter the string: ")
string = string.lower()
vowels = ['a','e','i','o','u']
vow_ctr = 0
con_ctr = 0
num_ctr = 0
spc_ctr = 0

for i in string:
    if ('a'<= i <='z'):
        if i in vowels:
            vow_ctr += 1
        else:
            con_ctr += 1
            
    elif '0'<= i <='9':
        num_ctr += 1
        
    else:
        spc_ctr += 1
        
print("No. of vowels in ",string,"are", vow_ctr)
print("No. of consonants in ",string,"are", con_ctr)
        
2)count the number of words is sentence
EX: sentence = 'hai all welcome to programming fundamental session'

sentence = input("Enter the sentence: ")

s_list = sentence.split()
no_of_words = len(s_list)

print("Number of words in the sentence is ",no_of_words)

3)count length of each word
EX: sentence = 'hai all welcome to programming fundamental session'

sentence = input("Enter the sentence: ")
s_list = sentence.split()

print("Length of each word is ")

for i in s_list:
    print(i,":",len(i))

4)count space in sentence
EX: sentence = 'hai all welcome to programming fundamental session'

sentence = input("Enter the sentence: ")

space_ctr = sentence.count(" ")

print("Number of spaces in the sentence is ",space_ctr)

5)print even length string in the sentence
EX: sentence = 'hai all welcome to programming fundamental session'

sentence = input("Enter the sentence: ")

s_list = sentence.split()

print("Even length strings in the sentence are: ")

for i in s_list:
    if len(i)%2 == 0:
        print(i)

6)remove duplicate in string and create new string

string = input("Enter the string: ")

new_str = ''

for ele in string:
    if ele not in new_str:
        new_str += ele

print("New string is ",new_str)

7)st = "hello 123 # hai 98" count number of digits inside string

string = input("Enter the string: ")

number = 0

for i in string:
    if i.isnumeric():
        number += 1

print("Number of digits in the string are ",number)

8)count small letter and capital letter in string
st = "PyThON is A proGrammIng Subject"

string = input("Enter the string: ")

low = 0
upp = 0

for i in string:
    if i.isupper():
        upp += 1
    elif i.islower():
        low += 1

print("No. of lower char are ",low)
print("No. of upper char are ",upp)     
    
9)Reverse a string

string = input("Enter the string: ")

rev_string = string[::-1]

print("The reversed string is",rev_string)

10)Check the string is polindrome or not

string = input("Enter the string: ")

rev_string = string[::-1]

if string == rev_string:
    print("String is palindrome")
else:
    print("String is not palindrome")
    
