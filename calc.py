print("CALCULADORA DE 4 OPERAÇÕES")
print("+ -> soma")
print("- -> Subtração")
print("* -> multiplicação")
print("/ -> divisão")

a = float(input("Digite o 1º Número " ))
b= float(input("Digite o 2º Número " ))
operacao = input("Digite a operação a realizar (+,-,*, ou /):" )

if operacao == "+":
    soma = a + b
    print(f"O resultado da soma é:{soma}")
elif operacao == "-":
    subtracao = a - b
    print(f"O resultado da subtração é:{subtracao}")
elif operacao == "*":
    multiplicacao = a * b
    print(f"O resultado da Multiplicação é:{multiplicacao}")
elif operacao == "/":
    divisao = a / b
    print(f"O resultado da Divisão é:{divisao}")
else:
    print("Operação inválida")

