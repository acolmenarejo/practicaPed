import socket



def cliente():
    # Pido al cliente que quiere hacer
    cometido = pedir_cometido()

    # Introudcir por teclado frase o numero
    comprobar = input("Introduce el dato a comprobar: ")

    st = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'localhost'
    port = 16031
    st.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    st.connect((host, port))
    # obtengo detener o ruta del fichero
    mensaje = procesar_cometido(cometido, comprobar)
    # Envío al servidor
    st.send(mensaje.encode('utf-8'))
    # Recibo datos
    st.settimeout(3)
    # comprobar_datos_recibidos(leer)
    recibido = st.recv(512)
    print(recibido.decode('utf-8'))
    #recibir_datos(st)
    st.close()





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








class CometidoError(Exception):
    pass