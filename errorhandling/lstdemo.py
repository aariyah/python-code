lst=[10,20,30,40,50]

location=int(input("enter location to fetch value from list"))

try:
    print(lst[location])

except Exception as e:
    location=int(input("enter location to fetch value from list"))
    print(lst[location])

finally:

  print("db commit")
  print("file read")
     