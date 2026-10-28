

def calculoPersona(nombre,ape1,ape2,edad):
    if (edad>17):
        return f"{nombre} {ape1} {ape2} es mayor de edad"
    else:
        return f"{nombre} {ape1} {ape2} es menor de edad"


print (calculoPersona("Alberto","Fernandez","Sanchez",32))
print (calculoPersona("Lemur","Santos","Vizcaino",12))

