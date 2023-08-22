year=2000
# is_leapyear=False

# if((year%4)==0):
#     is_leapyear=True
    
# elif(year%400==0):
#     is_leapyear=True
# elif(yera%100!=0):
#     is_leapyear=False
# print(year,"is_leapyear",is_leapyear)  
# 
#   
if((year%4==0 or year%400==0) and (year%100!=0)):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")


    


