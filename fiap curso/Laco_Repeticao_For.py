tabuada=int(input("Digite m número para exibir a tabuada: "))
print("Tabuada do número ", tabuada)

# (começo, fim, encremento(++))
for valor in range (1,21,1):
    print(str(tabuada) + " x " + str(valor) + " = " + str((tabuada*valor)))