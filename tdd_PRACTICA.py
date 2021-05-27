import unittest
import cliente_PRACTICA as cli
import servidor_PRACTICA as serv

class MyTestCase(unittest.TestCase):
    def test_cs_01(self):
        # cliente. Se puede hacer refactoring
        self.refactor1('1', 'Avanza')
    def test_cs_02(self):
        # cliente
        cometido = '2'
        comprobar = 'Avanza'
        mensaje = cli.procesar_cometido(cometido, comprobar)
        # servidor
        escuchado = mensaje
        estado_final = serv.procesar_escucha(escuchado)
        self.assertEqual('Enviada la comprobacion', estado_final)

    # tests cliente
    def test_cliente_01_procesar_cometido_1(self):
        cometido = '1'
        comprobar = 'Avanza'
        mensaje = cli.procesar_cometido(cometido, comprobar)
        self.assertEqual('Detener', mensaje)
    def test_cliente_02_procesar_cometido_2(self):
        cometido = '2'
        comprobar = 'Enviada la comprobacion'
        mensaje = cli.procesar_cometido(cometido, comprobar)
        self.assertEqual('Enviada la comprobacion', mensaje)
    def test_cliente_03_procesar_cometido_x(self):
        cometido = 'x'
        comprobar = 'Avanza'
        with self.assertRaises(cli.CometidoError):
            mensaje = cli.procesar_cometido(cometido, comprobar)
    # Servidor
    def test_servidor_tipoDato1(self):
        dato = '12'
        respuesta = serv.comprobar_tipo_dato(dato)
        self.assertEqual('capicua', respuesta)
    def test_servidor_tipoDato2(self):
        dato = 'hola'
        respuesta = serv.comprobar_tipo_dato(dato)
        self.assertEqual('palindromo', respuesta)
    def test_servidor_tipoDato3(self):
        dato = b'hola'
        with self.assertRaises(serv.TipeError):
            respuesta = serv.comprobar_tipo_dato(dato)
    # Test de resultado
    def test_servidor_capicuaSi(self):
        dato = '121'
        respuesta = serv.comprobar_capicua(dato)
        self.assertEqual('SI', respuesta)
    def test_servidor_capicuaNo(self):
        dato = '1212'
        respuesta = serv.comprobar_capicua(dato)
        self.assertEqual('NO', respuesta)
    def test_servidor_palindromoSi(self):
        dato = 'romamor'
        respuesta = serv.comprobar_palindromo(dato, False)
        self.assertEqual('SI', respuesta)
    def test_servidor_palindromoParcial(self):
        dato = 'rom.am;o r'
        respuesta = serv.comprobar_palindromo(dato, False)
        self.assertEqual('PARCIAL', respuesta)
    def test_servidor_palindromoNo(self):
        dato = 'roma.;or'
        respuesta = serv.comprobar_palindromo(dato, False)
        self.assertEqual('NO', respuesta)



# ESTO YA NO SON TESTS
    def refactor1(self, cometido, comprobar):
        mensaje = cli.procesar_cometido(cometido, comprobar)
        # servidor
        escuchado = mensaje
        estado_final = serv.procesar_escucha(escuchado)
        self.assertEqual('Servidor detenido', estado_final)



if __name__ == '__main__':
    unittest.main()
