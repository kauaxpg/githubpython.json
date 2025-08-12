numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

def segundo_maior(numeros):
    lista_sem_rep = list(set(numeros))
    
    lista_ordem = sorted(lista_sem_rep, reverse=True)
    
    return lista_ordem[1]

print("O segundo maior numero dessa lista é",segundo_maior(numeros))