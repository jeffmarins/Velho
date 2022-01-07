# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")
print("\nSelecione o número da operação desejada: ")
print("\n1-Soma\n2-Subtração\n3-Multiplicação\n4-Divisão")
opcao = int(input("\nDigite uma opção 1/2/3/4 ou 5 para sair: "))
while opcao != 5:
    if opcao == 1:
        a = int(input("Digite o primeiro número: "))
        b = int(input("Digite o segundo número: "))
        c = a+b
        print(f"Solução: {a} + {b} = {c}")
        opcao = int(input("\nDigite uma opção 1/2/3/4 ou 5 para sair: "))
    elif opcao == 2:
        a = int(input("Digite o primeiro número: "))
        b = int(input("Digite o segundo número: "))
        c = a-b
        print(f"Solução: {a} - {b} = {c}")
        opcao = int(input("\nDigite uma opção 1/2/3/4 ou 5 para sair: "))
    elif opcao == 3:
        a = int(input("Digite o primeiro número: "))
        b = int(input("Digite o segundo número: "))
        c = a*b
        print(f"Solução: {a} * {b} = {c}")
        opcao = int(input("\nDigite uma opção 1/2/3/4 ou 5 para sair: "))
    elif opcao == 4:
        a = int(input("Digite o primeiro número: "))
        b = int(input("Digite o segundo número: "))
        c = a/b
        print(f"Solução: {a} / {b} = {c}")
        opcao = int(input("\nDigite uma opção 1/2/3/4 ou 5 para sair: "))
    else:
       print("Opção Inválida")
       opcao = int(input("\nDigite uma opção 1/2/3/4 ou 5 para sair: "))
else:
    print("Calculadora encerrada")    
    
            



