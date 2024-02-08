
i = 1

while i<=5:
    print("Jurgen",end="")
    j = 1
    while j<=4:
        print("rocks",end="")
        j=j+1
    i=i+1
    print()
x = ["banana","pineapple","orange"]
for i in x:
    print(i)
y = ["cockroach","millipede","centipede"]
g = 0
while g < len(y):
    print(y[g])
    g=g+1
from array import *
val = array("i",[])

n = int(input("Enter the lenght of the array "))

for j in range(n):
    x = int(input("Enter the next value "))
    val.append(x)
    print(val)

search = int(input("Enter the value for search "))
k = 0
for e in val:
    if e==search:
       print(k)
       break

    k +=1

print(val.index(search))
val2 = array(val.typecode,[x for x in val])

#e = 0
#while e<len(val2):
for e in val2:
   print(e)

   #e+=1


if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

