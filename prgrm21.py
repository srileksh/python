n=int(input("Enter the limit:",))
first=0
second=1
print("Fobonacci series of",n,"is....")
print(first)
print(second)
for i in range(2,n):
  third=first+second
  print(third)
  first=second
  second=third
