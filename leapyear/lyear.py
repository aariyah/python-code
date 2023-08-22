# years=[2000,2024,1991,1995,1200,1400,1234]
f=open("C:/Users/Arya/Desktop/mypythonprograms/leapyear/data.txt","w")

# year="value"
# for y in years:
#     if(y%100==0 and y%400==0):
#         print(y)
#     elif(y%100!=0 and y%4==0):
#         print(y)

#     f.write(str(y)+"\n")
# print("finished")



f=open("C:/Users/Arya/Desktop/mypythonprograms/leapyear/year.txt","w")
for num in range(1890,3001):
    f.write(str(num)+"\n")
print("process finished")