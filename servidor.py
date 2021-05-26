import socket



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
        escucha_procesada = procesar_escucha(escucha.decode("utf-8"))
        if escucha_procesada == 'Servidor detenido':
            nuevo_socket.close()
            st.close()
            print('Servidor detenido')
            # TODO break
        else:
            tipo_dato = comprobar_tipo_dato(escucha.decode("utf-8"))
            print(tipo_dato)
            if tipo_dato == 'capicua':
                nuevo_socket.send(bytes('capicua', "UTF-8"))
                # comprobar_capicua()
            else:
                nuevo_socket.send(bytes('palindromo', "UTF-8"))
                # comprobar_palindromo()
            #abrir_ruta(escucha.decode('utf-8'), nuevo_socket)
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
        return 'capicua'
    elif isinstance(dato, str):
        return 'palindromo'
    else:
        raise TypeError("Error: Tipo de dato incorrecto")