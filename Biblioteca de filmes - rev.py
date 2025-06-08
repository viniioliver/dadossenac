# 1 - cria um dicionario vazio onde a chave sera o nome do usuario e o valor o filme assistido
usuarios_filmes = {
    'Vinicius': ['Matrix', 'Contratempo', 'A ilha'],
    'Ana': ['Quarteto', 'A ilha'],
    'Carlos': ['Interestelar'],
    'Jose' : ['Planeta dos macacos'],
    'Maria' : ['Lagoa azul'],
    'Eliana' : ['Mascara', 'Matrix']
}
# 2 - While true para criar um looping no menu de opçoes
while True:
    print('\n+++ Menu de Opções: +++')
    print('1. Cadastrar usuario e filme assistido')
    print('2. Remover filme assistido de um usuário')
    print('3. Listar todos os usuários e seus filmes')
    print('4. Consultar filmes de um usuário específico')
    print('0. Sair')

    numero = input('Escolha um numero: ')
#3 - Match case para menu um numero
    match numero:
        case '1':
            usuario = input('Digite o nome do usuario: ').strip() #strip para remover espaços no nome
            filme = input('Digite o nome do filme: ').strip()
            usuarios_filmes.setdefault(usuario, []).append(filme) #append para adicionar usuario e filme ao dicionario
            print(f'O filme {filme} foi adicionado ao usuario {usuario}')
        case '2':
            usuario = input('Digite o nome do usuario: ').strip() #Vai solicitar o nome do usuario
            filmes = usuarios_filmes.get(usuario) #com o nome do usuario , vai buscar no dicionario e apresentar os filmes cadastrados

            if filmes:
                print(f'Filmes assistindo pelo {usuario}')
                for a in filmes:
                    print(f'{a}')
                remover = input('Digite o filme que será removido: ').strip() #nova variavel para remoçao do filme
                if remover in filmes:
                    filmes.remove(remover)#deverá remover e mostrar filme removido
                    print(f'O filme {remover} foi removido')
                    if not filmes:
                        usuarios_filmes.pop(usuario)#Esse pop deverá excluir usario da lista
                        print('Usuario removido')
                else:
                    print('Filme nao encontrado')
            else:
                print(f'Usuario de nome {usuario} nao encontrado ou sem filme')
        case '3':
            if usuarios_filmes: #se
                print('\n--- Usuários e seus filmes ---')
                for usuario, filmes in usuarios_filmes.items():#items pecorre valores e chaves ao mesmo tempo
                    print(f'\n {usuario}:')
                    for filme in filmes:
                        print(f' {filme}')
            else:
                print('Nenhum usuario cadastrado')
        case '4':
            usuario = input('Digite o nome do usuário: ').strip()
            filmes = usuarios_filmes.get(usuario)
            if filmes:
                print(f'\n Filmes assistindos por {usuario}')
                for filme in filmes:
                    print(f' {filme}')
            else:
                    print(f'{usuario} nao cadastrado ou sem filmes')
        case '0': #Opçao 0 para sair
            print('Programa encerrado')
            break #break para encerrar
        case _:
            print('Opçao invalida')






