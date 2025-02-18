import unittest

from arma import Arma
from classes.guerreiro import Guerreiro
from classes.arqueiro import Arqueiro
from classes.mago import Mago

class TestClasses(unittest.TestCase):
    def test_special_attack_warrior(self):
        p = Guerreiro("A", 10, 100, 100)
        p2 = Guerreiro("B", 140, 10, 10)
        self.assertEqual(p2.vida, 140)
        p.ataque_especial(p2)
        self.assertEqual(p2.vida, 10)
    
    def test_special_attack_warrior_plus_extra(self):
        p = Guerreiro("A", 10, 100, 100)
        p.adicionar_arma(Arma("t", 5))
        p2 = Guerreiro("B", 140, 10, 10)
        self.assertEqual(p2.vida, 140)
        p.ataque_especial(p2)
        self.assertEqual(p2.vida, 5)

    def test_special_attack_archer(self):
        p = Arqueiro("A", 10, 10, 100)
        p2 = Arqueiro("B", 140, 10, 10)
        self.assertEqual(p2.vida, 140)
        p.ataque_especial(p2)
        self.assertEqual(p2.vida, 120)


    def test_special_attack_archer_plus_extra(self):
        p = Arqueiro("A", 10, 10, 100)
        p.adicionar_arma(Arma("t", 20))
        p2 = Arqueiro("B", 140, 10, 10)
        self.assertEqual(p2.vida, 140)
        p.ataque_especial(p2)
        self.assertEqual(p2.vida, 100)

    
    def test_special_attack_wizard(self):
        p = Mago("A", 10, 10, 100)
        p2 = Mago("B", 140, 10, 10)
        self.assertEqual(p2.vida, 140)
        p.ataque_especial(p2)
        self.assertEqual(p2.vida, 40)


    def test_special_attack_wizard_plus_extra(self):
        p = Mago("A", 10, 10, 100)
        p.adicionar_arma(Arma("t", 20))
        p2 = Mago("B", 140, 10, 10)
        self.assertEqual(p2.vida, 140)
        p.ataque_especial(p2)
        self.assertEqual(p2.vida, 20)
