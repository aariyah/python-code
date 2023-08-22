#swapping

num1=10
num2=20
print(f"value before swapping num1={num1} num2={num2}")
# temp=num1
# num1=num2
# num2=temp
# (num1,num2)=(num2,num1)
num1=num2+num1     #num1=30
num2=num1-num2     #num2=10
num1=num1-num2      #num1=20


print(f"value after swapping num1={num1} num2={num2}")