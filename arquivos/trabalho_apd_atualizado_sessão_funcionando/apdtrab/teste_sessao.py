import unittest
import controle_sessao

class teste_sessao (unittest.TestCase):
    def setUp(self):
        controle_sessao.remover_todas_sessoes()

    def teste_sem_sessao(self):
        t = controle_sessao.listar_sessao()
        self.assertEqual(0,len(t))

    def teste_buscar_sessao(self):
        controle_sessao.criar_sessao(1,"Alien",1300,12)
        t = controle_sessao.buscar_sessao(1)
        self.assertEqual(1,t[0])
        self.assertEqual("Alien", t[1])
        self.assertEqual(1300,t[2])
        self.assertEqual(12, t[3])

    def teste_remover_sessao(self):
        controle_sessao.criar_sessao(1, "Alien", 1300, 12)
        t = controle_sessao.remover_sessao(1)
        r = self.assertTrue(t)
        if(not r == False):
            print("excluido")

    def adicionando_duas_sessoes(self):
        controle_sessao.criar_sessao(1, "Alien", 1300, 12)
        controle_sessao.criar_sessao(2, "Guardioes da galaxia", 1600, 10)
        t = controle_sessao.listar_sessao(
        self.assertEqual(2,len(t))

        )
if __name__ == '__main__':
    unittest.main(exit=False)