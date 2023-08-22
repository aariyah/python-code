
age=int(input("enter the age"))
if age>0 and age<12:
    print("Child")
elif(age>11 and age<19):
    print("teenage")
elif(age>20 and age<25):
    print("adult")
elif age>25:
    print("senior citizen")



age=int(input("enter the age"))
if age>0 and age<10:
    print("Child")
elif(age>10 and age<20):
    print("teenage")
elif(age>18 and age<25):
    print("adult")
elif age>25:
    print("senior citizen")
"""
lst1=[10,11,13,15]
lst2=[9,8,11,13,14]
l1=0
l2=0
while((l1<len(lst1)) and (l2<len(lst2))):
    if lst1[l1]==lst2[l2]:
        print(lst1[l1])
        l2+=1
    elif(lst1[l1]>lst2[l2]):
        l2+=1
    elif(lst1[l1]<lst2[l2]):
        l1+=1"""



lst=[[2,0,3],[0,2,0],[4,0,2]]
for i in range(len(lst)):
    for j in range(len(lst[0])):
        
        lst[i][j]=i+j-lst[i][j]
print(lst)

