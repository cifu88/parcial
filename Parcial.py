"""Programa para identificar un numero inteligente.
Un numero es inteligente cuando tiene una cantidad impar
de factores. Por ejemplo el 9 cuyos factores son:
1, 3, 9"""
#Librerias:
import random as rd
import math as mt

#Variables:
Cantidad = 0
Num = 0
Numeros = []
Clave = 1
Division = 0
k = 0
i = 0
Raiz = 0
VerifiRaiz = 0


#Definicion de variables:
Cantidad = int(input("Por favor ingrese la cantidad de numeros a evaluar : "))
for k in range (Cantidad):
    Num = rd.randint(1,100)
    Numeros.append(Num)
#Operaciones:
    Raiz = mt.sqrt(Num)
    VerifiRaiz = Raiz%1

    if VerifiRaiz == 0:
        for i in range (Num):
            Division = Num%Clave
            Clave += 1               
        print("El numero ",Num," es inteligente") 
    else:
        print("El numero",Num," no es inteligente")
print("Los numeros a evaluar fueron : ",Numeros)
