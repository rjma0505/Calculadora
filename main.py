# Ricardo Azevedo
# Calculadora de operações básicas, retorna NaN se o operador não for válido


import os
import time

def calculadora(num1: float, num2: float, operador: str) -> float:
    """
    Usar nan como valor inicial é uma boa prática. 
    Se o operador fornecido não corresponder a nenhuma das opções válidas (+, -, etc.), a função retornará nan, 
    sinalizando que o cálculo não pôde ser realizado.
    """
    result = float("nan")
    if operador == '+':
        result = num1 + num2
    elif operador == '-':
        result = num1 - num2
    elif operador == '*':
        result = num1 * num2
    elif operador == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            raise ZeroDivisionError
    elif operador == '**':
        result = num1 ** num2

    return result


if __name__ == "__main__":

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            print('Calculadora')
            print('----------------------------------\n')
            num1 = float(input("Digite o primeiro número: "))
            operador = input("Digite o operador (+, -, *, /, **): ")
            num2 = float(input("Digite o segundo número: "))

            resultado = calculadora(num1, num2, operador)
            if str(resultado) == 'nan':
                print("Operador inválido!")
            else:
                print(f"\nResultado: {num1} {operador} {num2} = {resultado}")

        except ValueError:
            print('Dados inválidos! -> Tente novamente!')
            time.sleep(2)

        except ZeroDivisionError:
            print('Impossível dividir por zero! -> Tente novamente!')
            time.sleep(2)
        continuar = input("\nDeseja continuar? (s/n): ").strip().lower()
        if continuar != 's':
            break
    print('\nVolte sempre!\n')
