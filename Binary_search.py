# lst=[10,20,30,40,50,60]
# num=int(input("Enter searching item: "))
# start=0;
# end=len(lst)-1
# found=False

# while start<=end:
#     mid=(start+end)//2
#     if lst[mid]==num:
#         found=True
#         break
#     elif num<lst[mid]:
#         end=mid-1
#     else:
#         start=mid+1

# if found==True:
#     print("Element found in the list")
# else:
#     print("Element not found")


lst=[1,3,4,5,6,7,8]
n=int(input("enter searching item :"))
start=0
end=len(lst)-1
found=False

while start<=end:
    mid=(start+end)//2
    if lst[mid]==n:
        found=True
        break
    elif n<lst[mid]:
        end=mid-1
    else:
        start=mid+1

if found == True:
    print("enter element found")
else:
    print("element not found")


