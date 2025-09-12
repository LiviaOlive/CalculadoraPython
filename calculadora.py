print("====Calculadora====")

resultado = float(input("Digite o primeiro número: "))

while True:
    operador = str(input("Digite o operador (+, -, *, /) ou 'sair' para encerrar: "))
    
    if operador.lower() == 'sair':
        print("Encerrando a calculadora. Até mais!")
        break
    
    if operador not in ['+', '-', '*', '/']:
        print("Operador inválido. Tente novamente.")
        continue
    
    numero = float(input("Digite o próximo número: "))

    if operador == '+':
        resultado += numero
    elif operador == '-':
        resultado -= numero
    elif operador == '*':
        resultado *= numero
    elif operador == '/':
        if numero != '0':
            resultado /= numero
        else:
            print("Erro: Divisão por zero não é permitida.")
            continue
    else:
        print("Operador inválido. Tente novamente.")
        continue
    print("Resultado atual: ", resultado)