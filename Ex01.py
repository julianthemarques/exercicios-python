idade = {'cachorro 1 Ju': 3, 'cachorro 2 Ju': 2,
         'cachorro 3 Ju': 1, 'cachorro 4 Ju': 12, 'cachorro 5 Ju': 3}

idade2 = {'cachorro 1 Ca': 3, 'cachorro 2 Ca': 2,
          'cachorro 3 Ca': 1, 'cachorro 4 Ca': 12, 'cachorro 5 Ca': 3}


def checarCachorros():
    # tirando os gatos da lista
    del idade['cachorro 1 Ju']
    del idade['cachorro 4 Ju']
    del idade['cachorro 5 Ju']
    # concatenando a lista de ambas garotas
    idade.update(idade2)
    # adulto ou filhote?
    if idade.keys() >= 3:
        cachorroIdade = 'adulto'
    else:
        cachorroIdade = 'filhote'
    # enumerando index dos cachorros
    for i in enumerate(idade.items()):
        print(
            f"O cachorro número {i} é um {cachorroIdade} e tem {idade[1]} ano(s) de idade")
    # um print de como está nosso dicionário
    print(idade)


checarCachorros()
