"""
numero = input("mete un número ")
print ("El número elegido es " + numero)
if (numero == "15"):
    print ("Eres la niña bonita")
elif (numero == "22"):
    print ("Eres los dos patitos")
else:
    print ("Has perdido, no eres nada")
    """

"""
# Haz un menu de bios de 6 opciones.

print("Elige una de las opciones (SOLO NUMEROS)")
print("1) Opciones de arranque")
print("2) Opciones de alimentacion")
print("3) Opciones de ventilador")
opcion = input("PON UNO DE LOS NUMEROS DE LAS OPCIONES: ")

if (opcion=="1"):
    print("Has elegido opciones de arranque")
elif (opcion=="2"):
    print("Has elegido opciones de alimentacion")
elif (opcion=="3"):
    print("Has elegido opciones de ventilador")
else:
    print("No has elegido una opcion valida")
"""

opcion = input("Selecciona una opción (1, 2, 3): ")
match opcion:
    case "1":
        print("Has seleccionado la opción 1: Ver perfil.")
    case "2":
        print("Has seleccionado la opción 2: Editar perfil.")
    case "3":
        print("Has seleccionado la opción 3: Cerrar sesión.")
    case _:
        print("Opción no válida. Inténtalo de nuevo.")

