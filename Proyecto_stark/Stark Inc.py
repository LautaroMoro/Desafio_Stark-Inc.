from data_stark import lista_personajes
#B

for el in (lista_personajes):
    print({el['nombre']})

#C
def mostrar_altura_y_nombre_del_heroe(lista_personajes: list):
    """Muestra la altura y nombre de cada heroe

    Args:
        lista_personajes (list): lista de set de datos de superheroes
    """
    for el in (lista_personajes):
        print({el['nombre']}, {el['altura']})
#D
def calcular_mayor(lista_personajes:list)->float:
    """recorre la lista y retorna al superheroe de mayor estatura

    Args:
        lista_personajes (list): es la lista de los superheroes
    Raises:
        ValueError: indica si la lista "lista_personajes" esta vacia
    Returns:
        return mayor estatura: retorna al superheroe con mas estatura
    """

    if len(lista_personajes) == 0:
        raise ValueError("No se ha definido el mayor de una lista vacía")
    
    bandera_primer_elemento = True
    mayor_estatura = lista_personajes[0]
    for el in lista_personajes:
        if bandera_primer_elemento == True or mayor_estatura['altura'] < el['altura']:
            bandera_primer_elemento = False
            mayor_estatura = el
    print(mayor_estatura["nombre"])

    return mayor_estatura
        
#E
def calcular_menor(lista_personajes:list)->float:
    """recorre la lista y retorna al superheroe de menor estatura
    Args:
        lista_personajes (list): es la lista de los superheroes
    Raises:
        ValueError: indica si la lista "lista_personajes" esta vacia
    Returns:
        return menor estatura: retorna al superheroe con menor estatura
    """

    if len(lista_personajes) == 0:
        raise ValueError("No se definio el menor de una lista vacía")
    bandera_primer_elemento = True
    menor_estatura = lista_personajes[0]
    for el in lista_personajes:
        if bandera_primer_elemento == True or menor_estatura['altura'] > el['altura']:
            menor_estatura = el
            bandera_primer_elemento = False
    print(menor_estatura["nombre"])


    return menor_estatura
#F
def promedio_altura_superheroes(lista_personajes: list):
    """saca el promedio de la altura de todos los superheroes

    Args:
        lista_personajes (list): lista de set de datos de superheroes
    """
    suma_alturas = 0
    for el in lista_personajes:
        suma_alturas += float(el['altura'])
    promedio_altura_de_heroes = suma_alturas / len(lista_personajes)
    print(f"El promedio de altura de los superheroes es: {promedio_altura_de_heroes}")




#G
def el_mas_heavy(lista_personajes:list)->float:
    """calcula e informa cual es el heroe más pesado

    Args:
        lista_personajes (list): es la lista de los superheroes
    Raises:
        ValueError: indica si "lista_personajes" no es el dato de tipo lista
    Returns:
        return mayor estatura: retorna al superheroe más pesado
    """

    if type(lista_personajes) != list:
        raise ValueError("lista_personajes no es una lista")
    
    bandera_primer_elemento = True
    mas_pesado = lista_personajes[0]
    for el in lista_personajes:
        if bandera_primer_elemento == True or mas_pesado['peso'] < el['peso']:
            bandera_primer_elemento = False
            mas_pesado = el

    print(mas_pesado["nombre"])

    return mas_pesado
        
#E
def el_mas_liviano(lista_personajes:list)->float:
    """recorre la lista y retorna al superheroe de menor estatura
    Args:
        lista_personajes (list): es la lista de los superheroes
    Raises:
        ValueError: indica si "lista_personajes" no es una lista
    Returns:
        return mas liviano: retorna al superheroe con menor peso
    """

    if type(lista_personajes) != list:
        raise ValueError("lista_personajes no es una lista")
    bandera_primer_elemento = True
    mas_liviano = lista_personajes[0]
    for el in lista_personajes:
        if bandera_primer_elemento == True or mas_liviano['peso'] > el['peso']:
            mas_liviano = el
            bandera_primer_elemento = False
    print(mas_liviano["nombre"])


    return mas_liviano

mostrar_altura_y_nombre_del_heroe(lista_personajes)
calcular_mayor(lista_personajes)
calcular_menor(lista_personajes)
promedio_altura_superheroes(lista_personajes)
el_mas_heavy(lista_personajes)
el_mas_liviano(lista_personajes)


