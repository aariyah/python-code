txt="i have a car 2 bikes and 3 cycles"
k=txt.split(" ")
for i in k:
    if i.isdigit():
        print(i)