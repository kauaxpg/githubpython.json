numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

def contar_valor(valor_procurado, lista=numeros): 
    
    total = 0
    for item in lista:
        if item == valor_procurado:
            total += 1
    return total


print(contar_valor(2))          

