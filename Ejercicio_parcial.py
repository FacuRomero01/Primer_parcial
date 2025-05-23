def calcular_promedio(lista:list,valor:int)->bool:
    suma_lista = 0
    for i in range(len(lista)):
        suma_lista += lista[i]
    
    promedio_lista = suma_lista/len(lista)
    if promedio_lista > valor:
        res = True
    else:
        res = False
    return res

entrada = [10,20,30,40]
valor = 40

if calcular_promedio(entrada,valor):
    print("\nEl promedio de la lista dada es mayor al valor dado\n")
else:
    print("\nEl promedio de la lista dada es menor al valor dado\n")
