from json import load

with open("C:/Users/Arya/Desktop/mypythonprograms/jsonprocess/data.json","r") as f:
    data=load(f)


names=[u.get("name") for u in data]
print(names)