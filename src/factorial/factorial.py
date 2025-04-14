#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return 0
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

if len(sys.argv) < 2:
    input_range = input("Ingrese un rango de números (ej. 4-8 o -10 o 5-): ")
else:
    input_range = sys.argv[1]

# Verificar los casos sin límite inferior o superior
if input_range.startswith('-'):
    try:
        # Si es de la forma '-hasta'
        end = int(input_range[1:])
        start = 1  # El inicio será 1
        for num in range(start, end + 1):
            print(f"Factorial {num}! es {factorial(num)}")
    except ValueError:
        print("Formato no válido. Use el formato '-hasta' (ejemplo: '-10').")
        sys.exit()
    
elif input_range.endswith('-'):
    try:
        # Si es de la forma 'desde-'
        start = int(input_range[:-1])
        end = 60  # El final será 60
        for num in range(start, end + 1):
            print(f"Factorial {num}! es {factorial(num)}")
    except ValueError:
        print("Formato no válido. Use el formato 'desde-' (ejemplo: '5-').")
        sys.exit()
    
else:
    try:
        # Parseo el rango de números
        start, end = map(int, input_range.split('-'))
        if start > end:
            print("El número inicial debe ser menor o igual al final.")
            sys.exit()
        for num in range(start, end + 1):
            print(f"Factorial {num}! es {factorial(num)}")
    except ValueError:
        print("El formato del rango no es válido. Use el formato 'inicio-fin', como '4-8'.")
        sys.exit()

