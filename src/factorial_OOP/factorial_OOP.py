#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

class Factorial:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def factorial(self, num): 
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
    
    def run(self):  
        # Calcular los factoriales para el rango entre min_value y max_value
        for num in range(self.min_value, self.max_value + 1):
            print(f"Factorial {num}! es {self.factorial(num)}")

def get_range_from_input(input_range):
    # Verificar los casos sin límite inferior o superior
    if input_range.startswith('-'):
        try:
            # Si es de la forma '-hasta'
            end = int(input_range[1:])
            return 1, end  # El inicio será 1
        except ValueError:
            print("Formato no válido. Use el formato '-hasta' (ejemplo: '-10').")
            sys.exit()
    
    elif input_range.endswith('-'):
        try:
            # Si es de la forma 'desde-'
            start = int(input_range[:-1])
            return start, 60  # El final será 60
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
            return start, end
        except ValueError:
            print("El formato del rango no es válido. Use el formato 'inicio-fin', como '4-8'.")
            sys.exit()

if len(sys.argv) < 2:
    input_range = input("Ingrese un rango de números (ej. 4-8 o -10 o 5-): ")
else:
    input_range = sys.argv[1]

start, end = get_range_from_input(input_range)

# Crear la instancia de la clase Factorial
factorial_calculator = Factorial(start, end)

# Ejecutar el cálculo de factoriales
factorial_calculator.run()


