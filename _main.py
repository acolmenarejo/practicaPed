import cliente_PRACTICA as cli
import servidor_PRACTICA as serv

opcion = str(input("introduzca (1) para ejecutar cliente o (2) para ejecutar servidor "))
if opcion == '1':
    cli.cliente()
elif opcion == '2':
    print('Eligió ejecutar servidor')
    serv.servidor()
else:
    print('Error en la introducción de datos')