def hora():
    hora = int(input('Digite a hora:'))

    if hora >= 12:
        print('Boa tarde')
    elif hora >=18:
        print('Boa noite')
    else:
        print('Bom dia')


def maiorValor():
    n1 = int(input('digite um numero: '))
    n2 = int(input('digite outro numero: '))
    n3 = int(input('digite outro numero: '))

    lista = [n1,n2,n3]
    lista.sort()
    print(lista[2])

maiorValor()