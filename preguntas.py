"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
with open("data.csv", 'r') as file:
    data = file.readlines()
    data = [row.replace('\n', '') for row in data]
    data = [row.split('\t') for row in data]

def pregunta_01():
    # ['E', '1', '1999-02-28', 'b,g,f', 'jjj:12,bbb:3,ddd:9,ggg:8,hhh:2']
    global data
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    p1 = sum([int(row[1]) for row in data])
    return p1


def pregunta_02():
    # ['E', '1', '1999-02-28', 'b,g,f', 'jjj:12,bbb:3,ddd:9,ggg:8,hhh:2']
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    letras = [row[0] for row in data]
    p2 = [ ( letra,letras.count(letra) ) for letra in sorted(set(letras))]
    return p2


def pregunta_03():
    # ['E', '1', '1999-02-28', 'b,g,f', 'jjj:12,bbb:3,ddd:9,ggg:8,hhh:2']
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    p3 = {}
    for row in data:
        p3[ row[0] ] = p3.get( row[0],0) + int(row[1] )  
    p3 = sorted(list(p3.items()))
    return p3


def pregunta_04():
    # ['E', '1', '1999-02-28', 'b,g,f', 'jjj:12,bbb:3,ddd:9,ggg:8,hhh:2']
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    meses = [row[2][5:7] for row in data]
    p4 = [ ( mes,meses.count(mes) ) for mes in sorted( set(meses) ) ]
    return p4


def pregunta_05():
    # ['E', '1', '1999-02-28', 'b,g,f', 'jjj:12,bbb:3,ddd:9,ggg:8,hhh:2']
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    p5 = {}
    for row in data:
        key,value = row[0],int(row[1])
        if key in p5:
            p5[key].append(value)
        else:
            p5[key] = [value]
    p5 = sorted([(k, max(v), min(v)) for k, v in p5.items()])
    return p5


def pregunta_06():
    # ['E', '1', '1999-02-28', 'b,g,f', 'jjj:12,bbb:3,ddd:9,ggg:8,hhh:2']
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    p6 = {}
    rows = [row[4].split(",") for row in data]
    for row in rows:
        for word in row:
            key, value = word.split(":")
            if key in p6:
                p6[key].append(int(value))
            else:
                p6[key] = [int(value)]
    p6 = sorted([(k, min(v), max(v)) for k, v in p6.items()])
    return p6


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    p7 = {}
    for row in data:
        key,value = int(row[1]),row[0]
        if key in p7:
            p7[key].append( value )
        else:
            p7[key] = [value]
    #p7 = sorted([(k,v) for k, v in p7.items()])
    p7 = sorted(list(p7.items()))
    return p7


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    p8 = {}
    for row in data:
        if row[1] in p8:
            p8[row[1]].append(row[0])
        else:
            p8[row[1]] = [row[0]]
    p8 = sorted([(k,sorted(set(v))) for k, v in p8.items()])

    return p8


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    p9 = {}
    rows = [row[4].split(",") for row in data]
    for row in rows:
        for word in row:
            key, value = word.split(":")
            p9[key] = p9.get(key, 0) + 1
    #p9 =  {k:v for k,v in sorted(p9.items())}
    p9 = dict(sorted(p9.items()))
    return p9


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    p10 = [(row[0], len(row[3].split(",")), len(row[4].split(","))) for row in data]
    return p10


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    p11 = {}
    for row in data:
        for letra in row[3].split(","):
            p11[letra] = p11.get(letra, 0) + int(row[1])
    p11 = dict(sorted(p11.items()))
    return p11


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    return
