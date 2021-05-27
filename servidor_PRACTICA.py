import socket
import sys

st = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def servidor():
    print('Servidor levantado')
    host = 'localhost'
    port = 16031
    st.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    st.bind((host, port))
    st.listen(3)
    while True:
        # Acepto la conexion
        nuevo_socket, nueva_ruta_socket = st.accept()
        # Recibe o detener servidor o la comprobacion
        escucha = nuevo_socket.recv(512)
        # conexion cliente
        print(host, file=sys.stderr)
        print('\n')
        print(escucha.decode("utf-8"), file=sys.stderr)
        escucha_procesada = procesar_escucha(escucha.decode("utf-8"))
        # Proceso lo recibido por el cliente
        if escucha_procesada == 'Servidor detenido':
            nuevo_socket.close()
            st.close()
            print('Servidor detenido')
            break
        else:
            # Compruebo si recibo un numero o una frase
            tipo_dato = comprobar_tipo_dato(escucha.decode("utf-8"))
            print(tipo_dato)
            # Si recibo un numero, compruebo si es capicua
            if tipo_dato == 'capicua':
                deliberacion = comprobar_capicua(escucha.decode("utf-8"))
            else:
                # Si recibo frase, compruebo si es palindromo
                parcial = False
                deliberacion = comprobar_palindromo(escucha.decode("utf-8"), parcial)
                print('palindromo: ', deliberacion)
            # Envio al cliente la solucion
            nuevo_socket.send(bytes(deliberacion, "UTF-8"))
            print('Contenido enviado\n')

        nuevo_socket.close()



def procesar_escucha(escucha):
    if escucha == 'Detener':
        estado = 'Servidor detenido'
    else:
        estado = 'Enviada la comprobacion'
    return estado



def comprobar_tipo_dato(dato):
    if dato.isdigit():
        # if dato starts with C
        return 'capicua'
    elif isinstance(dato, str):
        # if dato starts with P
        return 'palindromo'
    else:
        raise TipeError("Error: Tipo de dato incorrecto")



def comprobar_capicua(dato):
    dato = int(dato)
    temp = dato
    rev = 0
    while dato > 0:
        dig = dato%10
        rev = rev*10+dig
        dato = dato //10
    if temp == rev:
        return 'SI'
    else:
        return 'NO'


def comprobar_palindromo(str, parcial):
    contador = 0
    str = str.lower()
    print('palabra original: ', str)
    if str == str[::-1] and parcial != True:
        return 'SI'
    elif str == str[::-1] and parcial != False:
        valor = 'PARCIAL'
        return valor
    else:
        for letra in str:
            if not letra.isalpha():
                print(letra)
                str = str.replace(letra, '')
                contador +=1
                parcial = True
        if contador != 0:
            print('palabra final: ', str)
            return comprobar_palindromo(str, parcial)
        else:
            return 'NO'


class TipeError(Exception):
    pass

