'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

print("Ejercicio de cifrado de Cesar")


abecedario_ingles = "abcdefghijklmnopqrstuvwxyz"

abecedario_espanol = "abcdefghijklmnñopqrstuvwxyz"

print("\nMenu para cifrar")
print("1. Cifrar")
print("2. Descifrar")
opcion = input("¿Que quieres hacer (1 o 2): ")

print("\nMenu para idioma")
print("1. Ingles")
print("2. Español")
opcion_idioma = input("¿Que quieres hacer (1 o 2): ")


if opcion_idioma == "1":
    alfabeto = abecedario_ingles
else:
    alfabeto = abecedario_espanol
    
texto = input("\nIngresa tu texto: ")

desplazamiento = int(input("Numero de desplazamiento: "))

if opcion == "2":
    desplazamiento = -desplazamiento


resultado = ""


for letra in texto:
    letra_min = letra.lower()
    
    if letra_min in alfabeto:
        posicion = alfabeto.find(letra_min)
        
        nueva_posicion = (posicion + desplazamiento) % len(alfabeto)
        nueva_letra = alfabeto[nueva_posicion]
        
        if letra.isupper():
            resultado = resultado + nueva_letra.upper()
        else:
            resultado = resultado + nueva_letra
    else:
        resultado = resultado + letra

print("\n---------------------------")
print("Resultado final:", resultado)
print("---------------------------")
