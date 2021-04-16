a = {
    "vname":"Otto",
    "nname":"Meier",
    "titel":("Prof","Dr"),
    "adresse":{
        "plz":12345,
        "ort":"Irgendwo",
        "strasse":"Milchstrasse",
        "nr":42
        }
     }
print(type(a),a)
for i in a:
    print(i, a[i])
for i in a.values():
    print(i)    
for i in a.keys():
    print(i)
print(a.pop("vname"))
for i in a:
    print(i, a[i])
