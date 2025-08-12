objetos = [
    {"nome": "Espada", "tipo": "arma"},
    {"nome": "Copo", "tipo": "item"},
    {"nome": "Bola", "tipo": "item"},
    {"nome": "Vaso", "tipo": "item"},
    {"nome": "Máscara", "tipo": "vestimenta"}
]

def nomes_objetos(lista_objetos):
    nomes = [] 
    for objeto in lista_objetos:  
        nomes.append(objeto["nome"]) 
    return nomes 

print(nomes_objetos(objetos))