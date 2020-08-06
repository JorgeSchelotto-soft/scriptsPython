import sys


try:
    # Se realiza la pontencia y suma de dos numeros. num1 representa la base y num2 la potencia.
    #
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    print("potencia : " + str(num1**num2))
    print("suma : " + str(num1+num2))
except:
    # En caso de error, salida para Frida
    print("Error : " + "Error al ejecutar el Custom Local: " + str(sys.exc_info()[0]) + str(sys.exc_info()[1]))



