import math

def is_number(numero):
    return numero.replace('.','',1).isdigit()

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
       case "^":
          return num1 ** num2
       case "RAIZ":
          print('Só é tirada a raiz do primeiro número inserido.')
          return math.sqrt(num1)
       case "TAN":
           print('A tangente só é tirada do primeiro número inserido.')
           return math.tan(num1)
       case "COS":
           print('O cosseno só é tirado do primeiro número inserido.')
           return math.cos(num1)
       case "SIN":
           print('O seno só é tirado do primeiro número inserido.')
           return math.sin(num1)

calc = False
while calc == False:
    num1 = input('Digite o primeiro número: ')
    if is_number(num1) == False:
        calc = False
        print('Número inválido.')
    else:
        calc = True
        operator = False
        while operator == False:
            operador = input("Digite o operador (+, -, *, /, ^, raiz, tan, cos ou sin): ").upper()
            calcular = ['+', '-', '*', '/', '^', 'RAIZ', 'TAN', 'COS', 'SIN']
            if operador not in calcular:
                print('Operador inválido.')
                operator = False
            else:
                operator = True
                calc2 = False
                while calc2 == False:
                    num2 = input('Digite o segundo número: ')
                    if is_number(num2) == False:
                        calc2 = False
                        print('Número inválido.')
                    else:
                        calc = True
                        calc2 = True
                        num1 = float(num1)
                        num2 = float(num2)
                        resultado = calculadora(num1, num2, operador)
                        print(resultado)
                        continuar = False
                        while continuar == False:
                            print('Escolha a opção desejada. \n 1. Continuar calculando a partir do resultado anterior. \n 2. Reiniciar o cálculo com novos números. \n 3. Encerrar o programa.')
                            c = input('Sua opção: ')
                            if c == '1':
                                continuar = True
                                num1 = resultado
                                operator = False
                            elif c == '2':
                                continuar = True
                                print('Reiniciando o programa...')
                                calc = False
                            elif c == '3':
                                print('Saindo...')
                                continuar = True
                            else:
                                print('Resposta não identificada.')
                                continuar = False