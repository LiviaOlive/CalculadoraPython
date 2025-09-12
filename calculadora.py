import funcoes

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
        resultado = funcoes.somar(resultado, numero)
    elif operador == '-':
        resultado = funcoes.subtrair(resultado, numero)
    elif operador == '*':
        resultado = funcoes.multiplicar(resultado, numero)
    elif operador == '/':
        try:
            resultado = funcoes.dividir(resultado, numero)
        except ValueError as erro:
            print(erro)
            continue
    else:
        print("Operador inválido. Tente novamente.")
        continue
    print("Resultado atual: ", resultado)