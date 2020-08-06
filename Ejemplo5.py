#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
Esto es para mostar la documentacion del codigo
# Para documentar ir al root con CMD y ejecutar: python -m pydoc -w Ejemplo5
# Para obtener paquetes pip freeze > requirements.txt
# Para instalar requirimientos pip install -r requirements.txt


"""

import sys

def Documentación_de_prueba():
    """# Para documentar ir al root con CMD y ejecutar python -m pydoc -w Ejemplo5"""
    pass


def sumoPotencio(num1, num2):
    """ 
    Esta función recibe por entrada de consola dos números y se encarga de sumar y obtener la potencia de los mismo.

    Para ejecutar en Turing se debe empaquetar como .exe y utilizar la expresión:


    # Declaro variables necesarias
    # num1 representa la base y num2 la potencia.
    #
    DefineVariable type "string" as "num1" with the value "x"
    DefineVariable type "string" as "num1" with the value "y"
    DefineVariable type "string" as "potencia"
    DefineVariable type "string" as "suma"


    # Corro custom
    #
    RunCustomLocal Ejemplo5 "<<<num1>>>" , "<<<num2>>>" 
    
    """
    print("potencia : " + str(num1**num2))
    print("suma : " + str(num1+num2))
    


if __name__ == "__main__":
    try:
        # Se realiza la pontencia y suma de dos numeros. num1 representa la base y num2 la potencia.
        #
        sumoPotencio(int(sys.argv[1]), int(sys.argv[2]))
    except:
        # En caso de error, salida para Frida
        print("Error : " + "Error al ejecutar el Custom Local: " + str(sys.exc_info()[0]) + str(sys.exc_info()[1]))