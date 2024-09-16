#001 
#Dado os 4 digitos de uma placa, informe o dia do rodizio
#Final 1 ou 2: segunda
#Final 3 ou 4: terça


def ex01():
    placa = input('Digite o valor da placa:')

    if placa.isnumeric():
        placa = int(placa)
        
        if placa > 4:
            print('Digite uma placa válida')
        else:
            utimoDigito = placa%10
            
            match ultimoDigito:
                case 1 | 2:
                    print('Segunda-feira')
                case 3 | 4:
                    print('Terça-feira')
                case 5 | 6:
                    print('Quarta-feira')
                case 7 | 8:
                    print('Quinta-feira')
                case 9 | 0:
                    print('Sexta-feira')
    else:
        print('Digite uma placa válida')

#02
#Calculadora fajuta!!

def ex02():
    valor1 = int(input('Digite o primeiro valor: '))
    operação = input('Digite a operação matemática: ')
    valor2 = int(input('Digite o primeiro valor: '))

    match operação:
        case '+':
            print(valor1 + valor2)
        case '-':
            print(valor1 - valor2)
        case '*':
            print(valor1 * valor2)
        case '/':
            if(valor2 == 0):
                print('Não há divisão por zero')
            else:
                print(valor1 / valor2)
ex02()