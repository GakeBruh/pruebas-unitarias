import unittest
from operaciones_comparacion import es_mayor_que, es_menor_que, es_mayor_o_igual_que, es_menor_o_igual_que, son_iguales

class TestOperacionesComparacion(unittest.TestCase):

    def test_es_mayor_que(self):
        self.assertTrue(es_mayor_que(5, 3)) 
        self.assertFalse(es_mayor_que(3, 5))  
        self.assertFalse(es_mayor_que(5, 5))
        self.assertGreater(int(es_mayor_que(10, 7)), 0)
        self.assertGreater(int(es_mayor_que(5, 3)), 0)

    def test_es_menor_que(self):
        self.assertLess(int(es_menor_que(3, 5)), 2)  
        self.assertLess(int(es_menor_que(0, 1)), 2)  
        self.assertLess(int(es_menor_que(5, 3)), 1)  
        self.assertLess(int(es_menor_que(5, 5)), 1)

    def test_es_mayor_o_igual_que(self):
        self.assertTrue(es_mayor_o_igual_que(5,3))
        self.assertTrue(es_mayor_o_igual_que(5,5))
        self.assertAlmostEqual(int(es_mayor_o_igual_que(10,9)), 1)
        self.assertGreaterEqual(es_mayor_o_igual_que(7,7),True)
        self.assertGreaterEqual(es_mayor_o_igual_que(50, 50), True)

    def test_es_menor_o_igual_que(self):
        self.assertTrue(es_menor_o_igual_que(6,7))
        self.assertFalse(es_menor_o_igual_que(100,1))
        self.assertAlmostEqual(int(es_menor_o_igual_que(6, 7)), 1)
        self.assertLessEqual(es_menor_o_igual_que(1570,1571),True)
        self.assertLessEqual(es_menor_o_igual_que(2500,2005),False)
    
    def test_son_iguales(self):
        self.assertTrue(son_iguales(7,7))
        self.assertFalse(son_iguales(108,100))
        self.assertEqual(son_iguales(10,10),True)
        self.assertNotEqual(son_iguales(100,10), True)

if __name__ == '__main__':
    unittest.main()
