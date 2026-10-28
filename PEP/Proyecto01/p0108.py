def saludoParticular(nombre):
    print(f"hola {nombre}")

def sumarDosNumeros(numero1,numero2):
    return numero1+numero2

def sumarTresNumeros(numero1,numero2,numero3):
    return numero1+numero2+numero3

def sumarCincoNumeros(numero1,numero2,numero3,numero4,numero5):
    return sumarDosNumeros(numero1,numero2)+sumarTresNumeros(numero3,numero4,numero5)

print( sumarDosNumeros(8,7) )

print(sumarTresNumeros(1,2,3))

print(sumarCincoNumeros(1,2,3,4,5))

'''
saludoParticular("Adrián")
saludoParticular("PEPE")
saludoParticular("Ivan")



for i in range(100):
    saludoParticular(f"Chapi{i}")
'''

