num=int(input("Enter a number:"))
print("Table of ",num)
for i in range(1,11):
  mul=num*i
  print(num,"x",i,"=",mul)




adj=["red","healthy","tasty"]
fruits=["apple","banana","cherry"]

for x in adj:
   for y in fruits:
       print(x,y)


c=1
while c<6:
  print(c)
  c+=1

for d in range(0,11,2):
  print(d)



#Write a Python program for printing the sum of the first ten natural numbers using the while loop.

num=1
sum=0
while(num<=10):
  sum=sum+num
  num=num+1

print("Sum of first 10 natural numbers is:",sum)