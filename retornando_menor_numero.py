numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

def encontrar_menor (lista):
    menor = lista[0]
    for numero in lista: 
        if numero < menor:
            menor = numero

    return menor

menor_numero = encontrar_menor (numeros)
print ("O menor numero dentro dessa lista é o",menor_numero)