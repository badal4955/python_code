def lsearch(ar,item):
    for i in range(6):
        if ar[i]==item:
            return i
l=[4,2,3,6,7,8]
s=int(input("enter item to search: "))
index=lsearch(l,s)
if index or index==0:
    print("item found at index:",index)
else:
    print("item not found")