with open("data.csv", 'r') as file:
    timesheet = file.readlines()
    timesheet = [row.replace('\n', '') for row in timesheet]
    data = [row.split('\t') for row in timesheet]


suma = sum([int(row[1]) for row in data])

print("1: ", suma)
print()
#--------------------------------------------------------------------------------
letras = [row[0] for row in data]
tuplas = [ ( letra,letras.count(letra) ) for letra in sorted(set(letras))]
print("2: ", tuplas)
print()
#--------------------------------------------------------------------------------

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
print("3: ", p3)
print()
#--------------------------------------------------------------------------------

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

"""
meses = [row[2][5:7] for row in data]
p4 = [ ( mes,meses.count(mes) ) for mes in sorted( set(meses) ) ]
print("4: ", p4)
print()
#--------------------------------------------------------------------------------




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
    if row[0] in p5:
        p5[row[0]].append(int(row[1]))
    else:
        p5[row[0]] = [int(row[1])]
p5 = sorted([(k, max(v), min(v)) for k, v in p5.items()])
print("5: ", p5)
print()
#--------------------------------------------------------------------------------

    # ['E', '1', '1999-02-28', 'b,g,f', 'jjj:12,bbb:3,ddd:9,ggg:8,hhh:2']


"""
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
print("6: ", p6)
print()
#--------------------------------------------------------------------------------
p7 = {}
for row in data:
    key,value = int(row[1]),row[0]
    if key in p7:
        p7[key].append( value )
    else:
        p7[key] = [value]
#p7 = sorted([(k,v) for k, v in p7.items()])
p7 = sorted(list(p7.items()))

print("7: ", p7)
print()
#--------------------------------------------------------------------------------
p8 = {}
for row in data:
    key,value = int(row[1]),row[0]
    if key in p8:
        p8[key].append( value )
    else:
        p8[key] = [value]
p8 = sorted([(k,sorted(set(v))) for k, v in p8.items()])
print("8: ", p8)
print()
#--------------------------------------------------------------------------------
p9 = {}
rows = [row[4].split(",") for row in data]
for row in rows:
    for word in row:
        key, value = word.split(":")
        p9[key] = p9.get(key, 0) + 1
#p9 =  {k:v for k,v in sorted(p9.items())}
p9 = dict(sorted(p9.items()))
print("9: ", p9)

#--------------------------------------------------------------------------------

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

print("10: ", p10)
print()
#--------------------------------------------------------------------------------

"""
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
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

    columna 4, ordenadas alfabeticamente.
"""

p11 = {}
for row in data:
    for letra in row[3].split(","):
        p11[letra] = p11.get(letra, 0) + int(row[1])
p11 = dict(sorted(p11.items()))
print("11: ", p11)
print()
#---------------------------------------------------------------------------------

