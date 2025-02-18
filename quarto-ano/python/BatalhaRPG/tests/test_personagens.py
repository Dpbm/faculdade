import unittest

from personagem import Personagem
from arma import Arma

class PersonagemTest(Personagem):
    def ataque_especial(self, outro):
        print("nothing")

class TestPersonagem(unittest.TestCase):
    def test_create(self):
        p = PersonagemTest("A", "B", 10, 1, 100)
        self.assertEqual(p.nome, "A")
        self.assertEqual(p.classe, "B")
        self.assertEqual(p.vida, 10)
        self.assertEqual(p.ataque_min, 1)
        self.assertEqual(p.ataque_max, 100)
        self.assertEqual(p.arma, None)

    def test_vida_setter(self):
        p = PersonagemTest("A", "B", 10, 1, 100)
        self.assertEqual(p.vida, 10)
        p.vida = 3
        self.assertEqual(p.vida, 3)
    
    def test_arma_setter(self):
        p = PersonagemTest("A", "B", 10, 1, 100)
        self.assertEqual(p.arma, None)
        a = Arma("t", 10)
        p.adicionar_arma(a)
        self.assertEqual(p.arma, a)

    def test_get_ataque(self):
        p = PersonagemTest("A", "B", 10, 10, 10)
        ataque = p.get_ataque()
        self.assertEqual(ataque, 10)

    def test_get_ataque_in_range(self):
        p = PersonagemTest("A", "B", 10, 1, 10)
        ataque = p.get_ataque()
        self.assertIn(ataque, list(range(1,10)))

    def test_get_dano_extra_no_weapon(self):
        p = PersonagemTest("A", "B", 10, 1, 10)
        extra = p.get_dano_extra()
        self.assertEqual(extra, 0)

    def test_get_dano_extra_with_weapon(self):
        p = PersonagemTest("A", "B", 10, 1, 10)
        p.adicionar_arma(Arma("T", 3))
        extra = p.get_dano_extra()
        self.assertEqual(extra, 3)
    
    def test_esta_vivo_true(self):
        p = PersonagemTest("A", "B", 10, 1, 10)
        self.assertTrue(p.esta_vivo())

    def test_esta_vivo_false(self):
        p = PersonagemTest("A", "B", 10, 1, 10)
        p.vida = -10
        self.assertFalse(p.esta_vivo())

    def test_atacar_win(self):
        p = PersonagemTest("A", "B", 10, 8,8)
        p2 = PersonagemTest("A2", "B", 10, 1, 10)
        p.adicionar_arma(Arma("T", 3))
        self.assertTrue(p2.esta_vivo())
        self.assertEqual(p2.vida, 10)
        p.atacar(p2)
        self.assertFalse(p2.esta_vivo())
        self.assertEqual(p2.vida, 0)
        
    def test_atacar_partial(self):
        p = PersonagemTest("A", "B", 10, 2,2)
        p2 = PersonagemTest("A2", "B", 10, 1, 10)
        p.adicionar_arma(Arma("T", 3))
        self.assertTrue(p2.esta_vivo())
        self.assertEqual(p2.vida, 10)
        p.atacar(p2)
        self.assertTrue(p2.esta_vivo())
        self.assertEqual(p2.vida, 5)
