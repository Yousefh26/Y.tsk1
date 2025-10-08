#FOR PROGRAM
num = int(input("please enter a number"))
for i in range (1,11) : 
    print(num,"x",i,"=",num*i)
print("***********************************")
#WHILE PROGRAM
i = 1 
while i<= 10:
    print(i)
    i +=1
print("***********************************")
#LIST MITHODS
numbers = [3, 1, 4, 2, 1,5]
print("original", numbers)
numbers.append(7)
print("append(7):", numbers)
numbers.insert(4, 10)
print("insert(4, 10):", numbers)
numbers.remove(1)
print("remove(1):", numbers)
numbers.pop(3)
print("pop(3):", numbers)
numbers.sort()
print("sort:", numbers)
numbers.reverse()
print("reverse:", numbers)
print("index(4):", numbers.index(4))
print("count(2):", numbers.count(2))
numbers_copy = numbers.copy()
print("copy:", numbers_copy)
numbers.clear()
print("clear:", numbers)