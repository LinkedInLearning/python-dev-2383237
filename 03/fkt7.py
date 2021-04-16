a = {
    "vname":"Otto",
    "nname":"Meier",
    "titel":("Prof","Dr"),
    "alter":42,
    "hobies":["Angeln","Joggen"],
    "adresse":{
        "plz":12345,
        "ort":"Irgendwo",
        "strasse":"Milchstrasse",
        "nr":42
        }
     }
print(a)
for i in a:
    print(i, a[i])
def analyse(d):
    for i in d.values():
        if type(i) is dict:
            analyse(i)
        else:
            print(i)

analyse(a)