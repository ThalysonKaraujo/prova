def a(K, lista):
    cont = 0
    while cont < K:
        menor = lista[0]  
        for j in lista:  
            if j < menor:
                menor = j
        lista.remove(menor)  
        cont += 1
    return menor  


lista_exemplo = [7, 3, 9, 1, 5]
K = 3  

print(a(K,lista_exemplo))
