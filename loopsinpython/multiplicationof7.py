
#multiplication of 7


# num1=7
# for i in range(1,11):
#     print(f"{num1}*{i}={num1*i}")



# print all the numbrs which are multiples of seven from 1to100

# num1=7
# for i in range(1,101):
#     if (i%num1==0):
#       print(f"{i}")


#u can select a range of 10 numbers,check whether the number is
#divisible by 9 ,if divisible by 9 then the result should be number multiplied by 9

# num1=9
# for i in range(1,11):
#     if((i%num1==0)*(9)):
#         print(f"{i}")



# Select a range of 10 numbers


# Check each number in the range
for num in range(1,11):
    # Check if the number is divisible by 9
    if num % 9 == 0:
                                                 # Multiply the number by 9
        result = num * 9
        print(f"{num} is divisible by 9. Result: {result}")
    else:
        print(f"{num} is not divisible by 9.")
