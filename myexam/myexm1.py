age=int(input("enter the age"))
if age>0 and age<11:
    print("Child")
elif(age>10 and age<20):
    print("teenage")
elif(age>18 and age<40):
    print("adult")
elif age>40:
    print("senior citizen")