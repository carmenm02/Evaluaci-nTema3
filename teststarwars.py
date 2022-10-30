import unittest
from starwars import Nodo, Nave

class Teststarwars(unittest.TestCase):
    def setUp(self):
        self.n= Nave()
        self.n1 = Nave("Halcon Milenario")
        self.n2 = Nave("Estrella de la muerte")
if __name__ =='__main__':
    unittest.main()