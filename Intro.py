#1
a = "Good"
b = "Morning"
print(a,b)
print(a+b)

#2
a = "   Good"
print(a)
print(a.lstrip())

#3
a = "Good     "
b = "Morning"
print(a+b)
print(a.rstrip()+b)

#4
a = "   Good  "
b = "   Morning"
print(a+b)
print(a.strip()+b.strip())

#5
msg = "GooD mORnInG"
print(msg)
print(msg.upper())
print(msg.lower())
print(msg.title())

#6
lst = [45,89,13,75,56]
print(lst)
lst[2] = 30
print(lst)
lst.append(73)
print(lst)
lst.insert(2,38)
print(lst)
lst.pop()
print(lst)
lst.pop(3)
print(lst)
del lst[4]
print(lst)
lst.remove(89)
print(lst)
lst.clear()
print(lst)
del lst
print(lst)

#7
num = ['abc','qwe','tyu','fgh']
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)

#8
num = ['abc','qwe','tyu','fgh']
print(num)
print(sorted(num))
print(sorted(num, reverse=True))
print(num)
