numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

def encontrar_maior (lista):
    maior = lista[0]
    for numero in lista: 
        if numero > maior:
            maior = numero

    return maior

maior_numero = encontrar_maior (numeros)
print ("O maior numero dentro dessa lista é o",maior_numero)