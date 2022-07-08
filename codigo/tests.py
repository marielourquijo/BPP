from ley_coulomb import ley_de_coulomb
import unittest

class test_ley_de_coulomb(unittest.TestCase):
    """En esta clase se definen las funciones de los tests para
    la función definida en el archivo ley_coulom"""

    def test_control_non_numero(self):
        """Comprueba que las variables de entrada sean muméricas
        """
        with self.assertRaises(TypeError):
            F = ley_de_coulomb(9,'2',2)

# comprueba que la distancia entre cargas no sea cero
    def test_distancia_cero(self):
        """Comprueba que la distancia entre cargas no sea cero 
        """
        with self.assertRaises(ZeroDivisionError):
            F = ley_de_coulomb(1,1,0)

    def test_carga_nula(self):
        """Prueba cuando alguna carga es nula
        """
        F = ley_de_coulomb(0,1,1)
        self.assertEqual(F, (0, False, False))

    def test_repelen1(self):
        """Comprueba si las cargas se repelen cuando tienen el mismo signo +
        """
        F = ley_de_coulomb(1,1,30)
        self.assertEqual(F, (10000000, True, True))

    def test_repelen2(self):
        """Comprueba si las cargas se repelen cuando tienen el mismo signo -
        """
        F = ley_de_coulomb(-1,-1,30)
        self.assertEqual(F, (10000000, True, True))

    def test_atraen(self):
        """Comprueba que las cargas se atraen si tienen diferente signo
        """
        F = ley_de_coulomb(1,-1,30)
        self.assertEqual(F, (-10000000, False, True))


if __name__ == '__main__':
    unittest.main()