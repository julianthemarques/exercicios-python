
julia1 = [3, 2, 1, 12, 3]
camila1 = [4, 12, 15, 8, 3]
julia2 = [9, 16, 6, 8, 3]
camila2 = [10, 5, 6, 1, 4]


def checarCachorros(listaA, ListaB):
    # tirando os gatos da lista de Julia com splice
    limite = len(listaA)
    listaJuliaSemGatos = listaA[1:limite-2]
    print(listaJuliaSemGatos)
    # concatenando a lista de ambas garotas
    listaTotal = listaJuliaSemGatos + ListaB
    print(listaTotal)
    # adulto ou filhote?
    for e, i in enumerate(listaTotal):
        if i >= 3:
            cachorroIdade = 'adulto'
        else:
            cachorroIdade = 'filhote'
    # um apanhado geral de nossas informações
        print(
            f"O cachorro número {e+1} é um {cachorroIdade} e tem {i} ano(s) de idade")

# rodando a função com dois conjuntos de dados diferentes


checarCachorros(julia1, camila1)
checarCachorros(julia2, camila2)
