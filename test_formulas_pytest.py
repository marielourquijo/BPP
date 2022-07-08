"""
Alumna:Maria Eloisa Urquijo Sagarduy
ACTIVIDAD 2:
Implementa un Script con un conjunto de funciones y crea un mínimo de 5 
test para cada una de las librerías de test vistasen la clase (unittest y pytest)
"""

from formulas import ley_de_coulomb
import pytest

# comprueba que las svariables de entrada sean muméricas
def test_control_non_numero():
    with pytest.raises(TypeError):
        ley_de_coulomb(9,'2',2)

# comprueba que la distancia entre cargas no sea cero
def test_distancia_cero():
    with pytest.raises(ZeroDivisionError):
        ley_de_coulomb(1,1,0)

# cumprueba si la carga es nula
def test_carga_nula():
    assert ley_de_coulomb(0,1,1) == (0, False, False)

# comprueba si las cargas se repelen cuando tienen el mismo signo
def test_repelen1():
   assert ley_de_coulomb(1,1,30) == (10000000, True, True)

def test_repelen2():
   assert ley_de_coulomb(-1,-1,30) == (10000000, True, True)

# comprueba que las cargas se atraen si tienen diferente signo
def test_atraen():
    assert ley_de_coulomb(1,-1,30) == (-10000000, False, True)