from formulas import ley_de_coulomb
import unittest

class test_ley_de_coulomb(unittest.TestCase):

# comprueba que las variables de entrada sean muméricas
    def test_control_non_numero(self):
        with self.assertRaises(TypeError):
            F = ley_de_coulomb(9,'2',2)

# comprueba que la distancia entre cargas no sea cero
    def test_distancia_cero(self):
        with self.assertRaises(ZeroDivisionError):
            F = ley_de_coulomb(1,1,0)

# cumprueba si la carga es nula
    def test_carga_nula(self):
        F = ley_de_coulomb(0,1,1)
        self.assertEqual(F, (0, False, False))

# comprueba si las cargas se repelen cuando tienen el mismo signo
    def test_repelen1(self):
        F = ley_de_coulomb(1,1,30)
        self.assertEqual(F, (10000000, True, True))

    def test_repelen2(self):
        F = ley_de_coulomb(-1,-1,30)
        self.assertEqual(F, (10000000, True, True))

# comprueba que las cargas se atraen si tienen diferente signo
    def test_atraen(self):
        F = ley_de_coulomb(1,-1,30)
        self.assertEqual(F, (-10000000, False, True))


if __name__ == '__main__':
    unittest.main()