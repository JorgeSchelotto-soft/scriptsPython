import sys


try:
    num1 = int(sys.argv[1])
    print("salida : " + num1**num2)
except:
    # En caso de error, salida para Frida
    print("Error : " + "Error al ejecutar el Custom Local: " + str(sys.exc_info()[0]) + str(sys.exc_info()[1]))



