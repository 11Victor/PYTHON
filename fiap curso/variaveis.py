nome=input("Digite um funcionário: ")
empresa=input("Digite a instituição: ")
qtde_funcionarios=int(input("Digite a quantidade de funionários: "))
mediaMensalidade=float(input("Digite a média da mensalidade: "))
print(nome + " trabalha na empresa " + empresa)
print("possui: ", qtde_funcionarios, " funcionários.")
print("A média da mensalidade é: " + str(mediaMensalidade))
print("====================VERIFIQUE OS TIPOS DE DADOS ABAIXO=======================")
print("O tipo de dado da variável [nome] é: ",type(nome))
print("O tipo de dado da variável [empresa] é: ",type(empresa))
print("O tipo de dado da variável [qtde_funcionarios] é: ",type(qtde_funcionarios))
print("O tipo de dado da variável [mediaMensalidade] é: ",type(mediaMensalidade))


