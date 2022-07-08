"""
Alumna:Maria Eloisa Urquijo Sagarduy
ACTIVIDAD 2:
Implementa un Script con un conjunto de funciones y crea un mínimo de 5 
test para cada una de las librerías de test vistasen la clase (unittest y pytest)
"""

"""
Definimos la formulade la ley de Coulomb donde
K es una constante 
q1 y q2 es el valor de las cargas eléctricas
d la distancia ente laas cargas
"""


def ley_de_coulomb(q1,q2,d):
    K = 9*(10**9)
    if isinstance(q1, str) or isinstance(q2, str) or isinstance(d, str):
        raise TypeError("Alguna de las variables no es un número")
    elif d==0:
        raise ZeroDivisionError("la distancia introducida es cero")
    else:
        F = (K*q1*q2)/(d**2)
    print("La fuerza eléctrica es", F)
    repele = False
    fuerza = False
    if q1==0 or q2==0:
        repele = False
        fuerza = False
        print("No hay fuerza")
    elif q1!=0 and q2!=0:
        fuerza = True
        if (q1>0 and q2>0) or (q1<0 and q2<0):
            repele = True
            print("Las cargas se repelen")
        else:
            repele = False
            print("Las cargas se atraen")
    return F, repele, fuerza

# l= ley_de_coulomb(1,3,0)