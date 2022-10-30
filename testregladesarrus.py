import unittest
from regladesarrus import total

class Testsarrus(unittest.TestCase):
    def setUp(self):
        self.matriz = [[0,1,2],
        [3,4,5],
        [6,7,8]]
        return super().setUp()
if __name__ =='__main__':
    unittest.main()