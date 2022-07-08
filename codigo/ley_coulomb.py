

"""
LEY DE COULOMB
===============
Definimos la formulade la ley de Coulomb donde
K es una constante 
q1 y q2 es el valor de las cargas eléctricas
d la distancia ente las cargas
"""

K = 9*(10**9)

def ley_de_coulomb(q1,q2,d):
    """con esta función calculamos la fuerza eléctrica que se genera entres dos cargas 
    a que se encuentran a una distancia d entre ellas

    Argumentos:
        q1 (int,float): carga electrica en coulombios \n
        q2 (int,float): carga electrica en coulombios \n
        d (int,float): distancia entre cargas \n

    Raises:
        TypeError: dará error si le entramos si q1, q2 o d se introduce de tipo 'str'
        ZeroDivisionError: dará error si se introduce d=0

    Retorno:
        Nos retorna el valor de la fuerza en newtons y nos dice si las cargas se atraen o se repelen.
        Cuando el valor de alguna de las cargas es 0 nos dice que no hay fuerza. 
    """
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
