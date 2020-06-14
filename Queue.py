##### generate random floating point values
from random import randint,random,gauss,shuffle,sample
#Set 5 lists for storing data
list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
# generate random numbers between 0-1
i = 1
while i<=5:
    list1.append(randint(0,10))
    list2.append(round(random(),2))
    list3.append(round(gauss(0,1),3))
    list4.append(randint(0,10))
    list5.append(round(random(),3))
    i+=1
print(list1)
print("\n")
print(list2)
print("\n")
print(list3)
print("\n")
print(sorted(list4))
print("\n")
print(list5)
print("\n")