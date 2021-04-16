class Tier:
    pass
print(type(Tier))

Hund = type("Hund",(Tier,),{"alter":3})
obj = Hund()
print(type(obj))