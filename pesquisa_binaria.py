'''
Esse algoritmo faz uma pesquisa binária em um array ordenado,
retornando True ou False.
Complexidade: Como o algoritmo elimina metade dos valores a cada iteração,
a complexidade é log n base 2, onde n é o tamanho da entrada.
Ex: se array tivesse 240.000 posições, quantas etapas seriam necessárias para encontrar
o valor, no pior caso?
resp: 2^x = 240.000 <=> log(2) 240.000 = 18 etapas!
Se fosse uma busca simples (começando do início), seriam necessárias 240.000 etapas!!!!

'''

def pesquisa_binaria(lista, valor):
    
    baixo = 0
    alto = len(lista)-1
    chute = (alto + baixo)//2

    while baixo <= alto:  # Enquanto não chegar num único elemento (baixo == alto), que é o pior caso
        if valor < chute:
            alto = chute - 1
            chute = (alto + baixo)//2
        elif valor > chute:
            baixo = chute + 1
            chute = (alto + baixo)//2
        else:  # valor == chute:
            return True
        
    return False


lista = [i for i in range(100)]
if (pesquisa_binaria(lista, 101)):
    print("Valor encontrado!")
else:
    print("Valor não encontrado!")
    



