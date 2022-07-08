"""
ALUMNA: MARIA ELOISA URQUIJO SAGARDUY

ACTIVIDAD 1

APARTADO 1:
Implemente un programa que lea el contenido del fichero y realice los 
siguientes cálculos:
● ¿Qué mes se ha gastado más?
● ¿Qué mes se ha ahorrado más?
● ¿Cuál es la media de gastos al año?
● ¿Cuál ha sido el gasto total a lo largo del año?
● ¿Cuáles han sido los ingresos totales a lo largo del año?
● Opcional: Realice una gráfica de la evolución de ingresos a lo largo del 
año .
APARTADO 2:
Haciendo uso de excepciones, haga las siguientes comprobaciones:
● Compruebe que el fichero existe y que tiene 12 columnas, una para 
cada mes del año.
● Para cada mes compruebe que hay contenido.
● Compruebe que todos los datos son correctos. De no haber un dato 
correcto, el programa debe saber actuar en consecuencia y continuar 
con su ejecución.
"""

import pandas as pd
import matplotlib.pyplot as plt

try:
    finanzas = pd.read_csv("finanzas2020.csv", sep='\t', header=0)
    fin = pd.DataFrame(finanzas)

# utilizo la excepción para comprobar que el fichero exista y se pueda abrir
except FileNotFoundError: 
    print("no se encuentra el fichero o no se puede leer")

else:
#  obtenemos el número de filas y columnas del dataframe
    filas = len(fin.axes[0])
    columnas = len(fin.axes[1])
    
#  para comprobar que el fichero tenga 12 columnas y coinciden con los meses 
    assert(columnas==12), "El número de columnas no es correcto"
    mes = ['Enero','Febrero','Marzo','Abril','Mayo','Junio',
           'Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
    assert(list(fin)==mes), "las columnas no corresponden con los meses del año"
# para que haya datos tiene que haber más de una fila   
    assert(filas>1), "no hay datos en el fichero"
    
# comprobabos los tipos de datos de cada columna y sustituimos por NaN los que no lo son
    for i in range(12):
        if fin[mes[i]].dtypes==object:
            fin[mes[i]] = pd.to_numeric(fin[mes[i]], errors='coerce')
            print("Existen datos no numéricos en la columna de", mes[i],
                  "estos datos se sutituirán por NaN y no cuentan para los cálculos")

# si todo va y los datos corregidos si fuera necesario seguimos adelante
   
# con un bucle for los totales de cada columna y los metemos en una lista
    sum_meses=[]
    for i in range(12):
        sum_meses.append(fin[mes[i]].sum(axis=0))

# calculamos los gastos y los ingresos de cada mes y los metemos en sendas listas
# para eso definimos la función gasto_ingreso_mes
    def gasto_ingreso_mes(datos, n):
        i = 0
        gastos = 0
        ingresos = 0
        for i in range(n):
            if datos[i] < 0:
             gastos = gastos - datos[i]
            elif datos[i] >= 0:
                ingresos = ingresos + datos[i]
        return gastos, ingresos

    gastos_mes = []
    ingresos_mes =[]
    for j in range(12):
        gi = gasto_ingreso_mes(fin[mes[j]], filas) 
        gastos_mes.append(gi[0])
        ingresos_mes.append(gi[1])

# creamos un nuevo dataframe las nuevas listas para guardar los datos que necesitamos para hacer los cálculos
    datos_año = { 'mes' : mes,
                  'gastos' : gastos_mes,
                  'ingresos': ingresos_mes,
                  'valance mes': sum_meses}
    anual = pd.DataFrame(datos_año)

    print("\n")
    print(anual)
    print("\n")

# mes de mayor gasto
    max_gasto = anual.loc[anual["gastos"] == anual["gastos"].max()]['mes'].values
    print("El mes de mayor gasto ha sido", max_gasto[0], "con un gasto de:", anual["gastos"].max()) 

# mes que más a ahorrado, mayor beneficio
    max_ahorro = anual.loc[anual["valance mes"] == anual["valance mes"].max()]['mes'].values
    print("El mes de mayor ahorro ha sido", max_ahorro[0], "con un beneficio de:", anual["valance mes"].max()) 


# media de gastos del año
    print("La media de gastos del año ha sido: ", anual["gastos"].mean())

# El gasto total de a lo largo del año
    print("El gasto de total del año ha sido: ", anual['gastos'].sum(axis=0))

# Ingresos totales a lo largo del año
    print("Los ingresos totales a lo largo del año han sido: ", anual['ingresos'].sum(axis=0))

# Gráfica de evoluvión de ingresos anual
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(mes, ingresos_mes)
    plt.show()
