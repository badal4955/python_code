#fibonnaci
'''
num=int(input("enter the number:"))
x=0
y=1
z=0
while(z<=num):
    print(z)
    x=y
    y=z
    z=x+y'''

#linear search:

'''def lsearch(arr,item):
    for i in item(6):
        if arr[i]==item:
            return

l=[4,3,6,2,6,2]
num=int(input("enter searching item:"))
index=lsearch(l,num)
if index or index==0:
    print("item is found on ",index)
else:
    print("item not found")

'''

#binary search

'''ist=[1,2,3,4,5,6]
num=int(input("enter the searching item"))
start=0
end=len(ist)-1
found=False
while(start<=end):
    mid=(start+end)//2
    if ist[mid]==num:
        found=True
        break
    elif num<ist[mid]:
        end=mid-1
    else:
        start=mid+1
if found==True:
     print("element is found")
else:
     print("element is not found")
'''

#gcd of two num.

'''num1=int(input("enter the 1st number :"))
num2=int(input("enter the 2nd number :"))

if num1>num2:
    min=num1
else:
    min=num2
for i in range(1,min+1):
    if num1%i==0 and num2%i==0:
        hcf=i
        print(f"The gcd of two number is {hcf}")'''

# randomized list in python

'''import random

l=[1,2,3,4,5]
random.shuffle(l)
print(l)'''

#reverse of string:

'''str="reverse a string"
str1=" "
for i in str:
    str1=i+str
    print(str1)'''

# prime number of range

'''for i in range(1,20):
    for j in range(2,i):
        if i%j==0:
            break
        else:
            print(i)'''

# greater and less
'''
num1=int(input("enter the 1st number :"))
num2=int(input("enter the 2nd number :"))
if num1>num2:
    print("num1 is greater")
else:
    print("num2 is greater")'''
'''
def greater(x,y):           #using function
    if x>y:
        print("x is big")
    else:
        print("y is big")

greater(2,4)'''


#even or odd:

'''def evenodd(x):
    if x%2==0:
        print("x is even")
    else:
        print("x is odd")

evenodd(2)'''

'''num=int(input("enter the number"))

if num%2==0:
    print("num is even")
else:
    print("num is odd")'''

# slicing in string

'''str="python programming"

find=str[::5]
print(find)'''

#pattern

'''num=5
for i in range(1,num+1):
    print(i*"*")
for i in range(num-1,0,-1):
    print(i*"*")
'''

# 