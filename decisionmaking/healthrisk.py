tummy_size=.25
buttock_size=5
healthrisk=tummy_size/buttock_size
gender1="female"
gender2="male"
print(healthrisk)
if((gender1=="female")):
    print("female")
    if((healthrisk<=.80)):
        print("low risk")
    elif(.81<=healthrisk<=.85):
        print("moderate risk")
    elif(healthrisk>=.85):
        print("high risk")
elif((gender2=="male")):
    print("male")
    if((healthrisk<=.95)):
        print("low risk")
    elif((.96<=healthrisk<=1.0)):
        print("moderate risk")
    elif((healthrisk>=1.0)):
        print("high risk")


    

