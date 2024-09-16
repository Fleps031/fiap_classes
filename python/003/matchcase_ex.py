#dia da semana por dia

diaI = input('Digite um digito da semana: ')

try:
    diaI = int(diaI)
except:
    print('digite direito')
    return



match diaI:
    case 1:
        print('Domingo')
    case 2:
        print('Segunda-feira')
    case 3:
        print('Terça-feira')
    case 4:
        print('Quarta-feira')
    case 5:
        print('Quinta-feira')
    case 6:
        print('Sexta-feira')
    case 7:
        print('Sábado')
    case _: 
        print('Dia inválido!')
