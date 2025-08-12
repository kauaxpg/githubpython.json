def listas_geral(lista):
    if len(lista) == 0: 
        return True     
    else:
        return False     

lista_com_itens = [1, "Marcos", True]  
lista_vazia = []                    

print("Lista com itens:", listas_geral(lista_com_itens))  
print("Lista vazia:", listas_geral(lista_vazia))      