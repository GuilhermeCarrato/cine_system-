import unittest
import controlador_ingresso

class TesteIngresso(unittest.TestCase):
    def setUp(self):
        controlador_ingresso.remover_todos_ingressos()

    def teste_sem_ingresso(self):
        ingresso = controlador_ingresso.listar_ingresso()
        self.assertEqual(0,len(ingresso))

    def teste_buscar_ingresso(self):
        t = controlador_ingresso.retornar_sessao()
        controlador_ingresso.gerar_ingresso(1,t)
        e = controlador_ingresso.buscar_ingresso(1)
        self.assertEqual(1, e[0])
        self.assertEqual("Alien", e[1])
        self.assertEqual(14, e[2])
        print("ok")
    def remover_ingresso(self):
        t = controlador_ingresso.retornar_sessao()
        valor1 = controlador_ingresso.gerar_ingresso(1, t)
        auxv1 = valor1
        valor2 = controlador_ingresso.listar_ingressos_vendidos()
        auxv2 = valor2
        controlador_ingresso.remover_ingresso(1,1,"addvendas")
        if valor1 != auxv1 and auxv2 != valor2:
            b = True
            print("ok")
        else:
            b = False
        self.assertTrue(b,"não corremponde")
    def vender_meia(self):
        t = controlador_ingresso.retornar_sessao()
        controlador_ingresso.gerar_ingresso(2,t)
        controlador_ingresso.venda_ingresso_meia(2)
        e = controlador_ingresso.buscar_ingresso(2)
        self.assertEqual(3,len(e))
        print("ok")
    def vender_inteira(self):
        t = controlador_ingresso.retornar_sessao()
        controlador_ingresso.gerar_ingresso(2,t)
        controlador_ingresso.venda_ingresso_inteira(2)
        e = controlador_ingresso.buscar_ingresso(2)
        self.assertEqual(3,len(e))
        print("ok")

if __name__ == '__main__':
    unittest.main(exit=False)