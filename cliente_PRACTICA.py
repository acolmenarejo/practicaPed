import socket



def cliente():
    # Pido al cliente que quiere hacer
    cometido = pedir_cometido()
    repeticiones = 3
    while repeticiones != 0:
        # Introudcir por teclado frase o numero
        comprobar = input("Introduce el dato a comprobar: ")
        host = input("Introduce el host: ")
        port= input("Introduce el puerto: ")
        st = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # host = 'localhost'
        # port = 16031
        st.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        conexion_con_servidor(st,host, port)
        # obtengo del usuario por pantalla: detener o comprobar dato
        mensaje = procesar_cometido(cometido, comprobar)
        # Envío al servidor lo que ha dicho el usuario
        st.send(mensaje.encode('utf-8'))
        # Recibo datos
        st.settimeout(3)
        # comprobar_datos_recibidos(recibido)
        recibido = st.recv(512)
        # Imprimir datos
        print(recibido.decode('utf-8'))

        st.close()
        repeticiones -= 1




def pedir_cometido():
    c = str(input("Cometido (1: Detener servidor, 2: Comprobar frase o numero): "))
    if c not in ['1', '2']:
        print('Cometido incorrecto, introduzca (1) o (2) para usar el cometido deseado')
        c = pedir_cometido()
    return c

def procesar_cometido(cometido, comprobar):
    if cometido == '1':
        mensaje = 'Detener'
    elif cometido == '2':
        mensaje = comprobar
    else:
        raise CometidoError("Error: Cometido incorrecto")
    return mensaje

def conexion_con_servidor(st, host, port):
    try:
        st.connect((host, int(port)))
    except ConexionError:
        raise CometidoError("Error: Puerto o host incorrectos")






class CometidoError(Exception):
    pass

class ConexionError(Exception):
    pass

