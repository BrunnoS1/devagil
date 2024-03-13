def calculadora(num1, num2, operador):
    match operador:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            return num1 / num2
        case _:
            return "Operador inválido"        

operador = input("Insira o operador (+, -, *, /), 0 para encerrar: ")
while operador != "0":
    num1 = float(input("Insira o primeiro número: "))
    num2 = float(input("Insira o segundo número: "))
    resultado = calculadora(num1, num2, operador)
    print(f"Resultado: {resultado}")
    operador = input("Insira o operador (+, -, *, /), 0 para encerrar: ")