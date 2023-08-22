# num1=4
# num2=10
# num3=13
# if((num1>num2)and(num1>num3)):
#     print(" num1 is greater")
# elif((num2>num1)and(num2>num3)):
#     print("num2 is greater")
# elif((num3>num1)and(num3>num2)):
#     print("num3 is largest")

# num1=4
# num2=10
# num3=13   
# if (num1>num2) and (num1>num3):
#     if (num2>num3):
#         print("second largest = num2")
#     else:
#         print("second largest = num3")
# elif (num2>num1) and (num2>num3):
#     if(num1>num3):
#         print("second largest = num1")
#     else:
#         print("second largest = num3")
# else:
#     if (num1>num2):
#         print("second largest = num1")
#     else:
#         print("second largest = num2")



num1=4
num2=10
num3=15

first=0
second=0
third=0

if((num1>num2)and(num1>num3)):
    first=num1
    if num2>num3:
     second=num2
     third=num3
    else:
       second=num3
       third=num2
elif(num2>num1)and(num2>num3):
   first=num2
   if num1>num3:
      second=num1
      third=num3
   else:
      second=num3
      third=num1
elif (num3>num1) and (num3>num2):
   first=num3
   if num1>num2:
      second=num1
      third=num2
   else:
      second=num2
      third=num1

      
print(first,second,third)  
print(second)    
      









      
#Q1) second largest
# Q2)sort these three numbers
# Q3)CALCULATE BMI(body mass index)wheidgt,height in meter
