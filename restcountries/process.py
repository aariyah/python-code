from json import load

with open("C:/Users/Arya/Desktop/mypythonprograms/restcountries/rest.json",encoding="UTF-8") as f:
    data=load(f)


    # print(len(data))



# print all country names>>>>>>>>
# for n in data:
#     print(n.get("name"))

# country_names= [n.get("name") for n in data] 
# print(country_names)


# print all region names>>>>>>>>>>>> 
# region_name={n.get("region") for n in data}
# print(region_name)

# print all asian countris>>>>>>>>>>>
for c in data:
    if c.get("region")=="Asia":
        print(c.get("name"))
# asian_country=[c.get("name") for c in data if c.get("region")=="Asia"]
# print(asian_country)


# print population of afganisthan>>>>>>>>>>>

population = [c.get("population") for c in data if c.get("name")=="Afghanistan"] 
print(population)


# indian population>>>>>>>>>>>>>>>>>>>>


# country_borders=[c.get("borders")for c in data if c.get("name")=="India"][0]
# print(country_borders)


# country_border_name=[c.get("names") for c in data if c.get("alpha3code")in country_borders]
# print(country_border_name)



# country_code=[c.get("currencies") for c in data if c.get("code")=="" ]
# print(country_code)

