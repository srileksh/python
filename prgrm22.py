list=[]
num=int(input("How many number:"))
for i in range(num):
  num=int(input("Enter the number:"))
  list.append(num)
print("Sum of counts in given list is:",sum(list))
