limit=25
start=1

evensum=0
oddsum=0



for num in range (start,limit):
    if num%2==0:
        evensum+=num
    else:
        oddsum+=num 

print("evensum=",evensum)
print("oddsum=",oddsum)