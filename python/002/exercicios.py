#01 - Exibir o proximo numero
def ex1():
    n = int(input('(01) Digite o numero: '))
    print('ans:', n+1)
#02 - Calcular o cubo
def ex2():
    n = int(input('(02) Digite o numero a ser cubado:'))
    print(n**3)
#03 - Calcular todas as operações
def ex3():
    n1 = int(input('(04) Digite o primeiro número'))
    n2 = int(input('(04) Digite o segundo número'))

    print('Soma:', n1 + n2)
    print('Subtração:', n1 - n2)
    print('Multiplicação', n1 * n2)
    print('Divisão', n1 / n2)
    print('Módulo', n1 % n2)
    print('Div. Inteira', n1 // n2)
    print('Exponenciação', n1 ** n2)

#04 - Calcular o delta
def ex4():
    a = float(input('(04) Digite o A: '))
    b = float(input('(04) Digite o B: '))
    c = float(input('(04) Digite o C: '))
    print('Delta:', b**2 - (4*a*c))
#05 - Cedulas
def ex5():
    valor = int(input('Digite o valor a sacar:'))
    resto = 1

    c50 = valor // 50
    resto = valor % 50

    c20 = resto // 20
    resto = resto % 20

    c10 = resto // 10
    resto = resto % 10

    print(f"""
            R$50 - {c50} cédulas
            R$20 - {c20} cédulas
            R$10 - {c10} cédulas
         """)

#06 - Proximo multiplo de 5
def ex6():
    n = int(input('Insira o numero: '))

    print('Próximo múltiplo de 5:', ((n//5) + 1)*5)

ex6()



