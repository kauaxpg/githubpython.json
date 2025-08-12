natureza = ["rio", "floresta", "leão", "montanha", "oceano", "estrela", "vento", "cachoeira", "lua", "girassol"]
tecnologia = ["algoritmo", "API", "blockchain", "código", "software", "nuvem", "hardware", "interface", "pixel", "servidor"]

def juntar_listas(nat, tec):
    return nat + tec 

lista_completa = juntar_listas(natureza, tecnologia)
print(lista_completa)