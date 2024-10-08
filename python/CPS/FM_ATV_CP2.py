#FELIPE GOMES MOLINARI LOPES
#RM 559885

system_prefix = '-> '

#01 - Next
def prox_num(n: int) -> int:
    return n+1

#02 - Double
def dobro(n: int) -> int:
    return n*2

#03 - Delta
def calc_delta(a: float, b: float, c: float) -> int:
    return((b*b)-(4*(a*c)))

#04 - Nome por ordem alfabética
def nome_ordem(s1: str, s2: str) -> None:
    primeiro = s1
    segundo = s2

    if primeiro > s2:
        primeiro = s2
        segundo = s1
    
    print(f'{system_prefix}Nomes ordenados: {primeiro} e {segundo}')

#05 - Fatorial
def fatorial(n: int) -> int:
    idx = n-1
    result = n
    while idx >= 1:
        result = result * idx
        idx-=1
    return result

#06 - Potência
def potencia(base: int, expoente: int) -> int:
    return base**expoente

while True:
    print("""
    Bem vindo ao sistema. Escolha uma das opções abaixo:

    1. Calcular o próximo número
    2. Calcular o dobro de um número
    3. Calcular o delta dado A,B e C
    4. Ordenar 2 nomes em ordem alfabética
    5. Calcular o fatorial de um número
    6. Calcular a pôtencia de um número
    0. Finalizar o sistema
    """)

    choice = input('-> ')
    
    match choice:
        case '1':
            print(f'{system_prefix}Próximo número: {prox_num(45)}')          
        case '2':
            print(f'{system_prefix}Dobro: {dobro(25)}')          
        case '3':
            print(f'{system_prefix}Delta: {calc_delta(1,2,3)}')          
        case '4':
            nome_ordem("Jonas","Adriana")          
        case '5':
            print(f'{system_prefix}Fatorial: {fatorial(4)}')          
        case '6':
            print(f'{system_prefix}Potência: {potencia(2,3)}')               
        case '0':
            print(f'{system_prefix}Desligando...')
            break
        case _:
            print(f'{system_prefix}Opção inválida, tente novamente.')
