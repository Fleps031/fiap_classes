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


#07 - PEDREIRO
hb = 0.2
lb = 0.4

area_bloco = 0.4*0.2

hm = float(input('Informe a altura: '))
lm = float(input('Informe a largura: '))

blocos_por_largura = lm/lb
blocos_por_altura = hm/hb
print(blocos_por_largura)
print(blocos_por_altura)


AREA_MURO = hm * lm
# print(f'Gasto com blocos: R$ {GASTO_COM_BLOCOS:.2f}')
quantidade_de_blocos =  blocos_por_altura*blocos_por_largura
print(quantidade_de_blocos)

CUSTO_POR_BLOCOS = 5
CUSTO_MAO_DE_OBRA = 100

BLOCOS_NECESSARIOS = int(((quantidade_de_blocos * 0.05) + quantidade_de_blocos)) + 1
GASTO_COM_MAO_DE_OBRA = AREA_MURO * CUSTO_MAO_DE_OBRA
GASTO_COM_BLOCOS = BLOCOS_NECESSARIOS * CUSTO_POR_BLOCOS

GASTO_TOTAL = GASTO_COM_BLOCOS+GASTO_COM_MAO_DE_OBRA
TOTAL_COM_PIX = GASTO_TOTAL - GASTO_TOTAL*0.05
TOTAL_COM_CREDITO = GASTO_TOTAL + GASTO_TOTAL*0.03

print('Área total do muro em m²:', AREA_MURO)
print('Quantidade de blocos necessários:', BLOCOS_NECESSARIOS)
print(f'Gasto com blocos: R${GASTO_COM_BLOCOS:.2f}' )
print(f'Gasto com mão de obra: R${GASTO_COM_MAO_DE_OBRA:.2f}')
print(f"""Gasto total: 

        Valor em dinheiro ou pix: R${TOTAL_COM_PIX:.2f}
        Valor em débito: R${GASTO_TOTAL:.2f}
        Valor em crédito: R${TOTAL_COM_CREDITO:.2f}

    """)




