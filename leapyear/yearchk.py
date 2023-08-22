fread=open("C:/Users/Arya/Desktop/mypythonprograms/leapyear/year.txt","r")

fwrite=open("C:/Users/Arya/Desktop/mypythonprograms/leapyear/leapyear.txt","w")


for line in fread:
    year=int(line.rstrip("\n"))
    if(year%100==0 and year%400==0):
        fwrite.write(str(year)+"\n")
    
    elif(year%100!=0 and year%4==0):
        fwrite.write(str(year)+"\n")
        