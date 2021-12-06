print('-=' * 25)
print('SISTEMA DE INSCRIÇÕES PARA O EVENTO'.center(50))
print('-=' * 25)

usuarios_cadastrados = {}


def cadastrar_usuario():
    nome = input('Digite seu nome completo: ')
    email = input('Digite seu email: ')
    usuarios_cadastrados[email] = nome
    print(f'Cadastro efetuado com sucesso! Seja bem vindo(a), {(nome.split()[0])}\n')
    print('-=' * 40)


def exibir_usuarios_cadastrados():
    cadastro = 1
    print('Listando usuários cadastrados:')
    for usuario in usuarios_cadastrados:
        print(f'{cadastro} - {usuario} - {usuarios_cadastrados[usuario]}')
        cadastro += 1
    print('-=' * 40)


def procurar_usuario():
    usuario = input('Digite o nome do usuario que deseja buscar: ')
    if usuario in usuarios_cadastrados.values():
        print(f'Usuário encontrado: {usuario}\n')
    else:
        print('Usuário não encontrado.\n')
    print('-=' * 40)


def remover_usuario():
    usuario = input('Digite o email do usuário que deseja remover: ')
    if usuario in usuarios_cadastrados:
        print(f'Usuário {usuarios_cadastrados[usuario]} do email: {usuario} removido com sucesso\n')
        del usuarios_cadastrados[usuario]
    else:
        print('Usuário não encontrado.')
    print('-=' * 40)


def alterar_nome_usuario():
    usuario = input('Digite o email do usuário que deseja alterar o nome: ')
    if usuario in usuarios_cadastrados:
        print(f'Usuario encontrado: {usuarios_cadastrados[usuario]} - {usuario}!')
        novo_nome = input(f'Digite o novo nome de usuario para o email {usuario}: ')
        usuarios_cadastrados[usuario] = novo_nome
        print(f'O nome foi alterado para {novo_nome} com sucesso.')
    else:
        print('Usuário não encontrado.\n')
    print('-=' * 40)


def validacao():
    while True:
        cadastramento = input('Deseja cadastrar um usuario? [S/N] ').upper()
        if cadastramento in 'SIM':
            cadastrar_usuario()
        elif cadastramento in 'NAO':
            break
        else:
            print('Caractere inválido. Digite S ou N')
            validacao()


validacao()
exibir_usuarios_cadastrados()
exibir_usuarios_ordenados()
procurar_usuario()
remover_usuario()
alterar_nome_usuario()