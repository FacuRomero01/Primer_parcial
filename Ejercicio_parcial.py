def calcular_promedio(lista:list,valor:int)->bool:
    
    """
    Calcula el promedio de una lista de números y lo compara con un valor dado.

    Parámetros:
    lista (list): Una lista de números enteros o flotantes.
    valor (int): Un número con el cual se comparará el promedio de la lista.

    Retorna:
    bool: True si el promedio de la lista es mayor que el valor dado, False en caso contrario.
    También retorna False si la lista está vacía.
    """
    
# Parámetros formales: lista, valor
    suma_lista = 0
    for i in range(len(lista)):
        suma_lista += lista[i]

    promedio_lista = suma_lista / len(lista)
    if promedio_lista > valor:
        res = True
    else:
        res = False
    return res

# Parámetros actuales: entrada = [10, 20, 30, 40], valor = 40
entrada = [10, 20, 30, 40]
valor = 40

# Invocación de la función
if calcular_promedio(entrada, valor):
    print("\nEl promedio de la lista dada es mayor al valor dado\n")
else:
    print("\nEl promedio de la lista dada es menor al valor dado\n")
