f=open("C:/Users/Arya/Desktop/mypythonprograms/users/data.txt","r")

usres=[]
for line in f:
    text=line.rstrip("\n")
    name,followers,following=text.split(",")
    print(name,followers,following)