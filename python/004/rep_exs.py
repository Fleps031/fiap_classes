#001

def ex01():
    minV = int(input('Digite o valor inicial: '))
    maxV = int(input('Digite o valor final: '))
    idx = minV+1

    while idx < maxV:
        print(idx, end=' ')
        idx+=1

def ex02():
    maxV = int(input('Digite o valor inicial: '))
    minV = int(input('Digite o valor final: '))
    idx = maxV

    while idx >= minV:
        print(idx, end=' ')
        idx-=1

def ex03():
    number = int(input('Digite um número: '))
    idx = 1

    while idx<=10:
        print(number*idx, end =' ')
        idx+=1
    
def ex04():
    idxInput = 0
    isFirstNumber = True
    biggestNumber = 0

    while idxInput < 10:
        numValor = int(input('Digite um número: '))
        if isFirstNumber == True:
            isFirstNumber = False
            biggestNumber = numValor

        if numValor > biggestNumber:
            biggestNumber = numValor
        idxInput+=1

    print(f'Maior: {biggestNumber}')

def ex06():
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    idx = num1
    if(num1 > num2):
        idx = num2
        num2 = num1

    while idx <= num2:
        print(idx)
        idx+=1

def ex07():
    while True:
        nota1 = float(input('Digite a primeira nota: '))
        if nota1 <= 10 and nota1 >= 0:
            break
        print('Digite uma nota válida!!')
    
    while True:
        nota2 = float(input('Digite a segunda nota: '))
        if nota2 <= 10 and nota2 >= 0:
            break
        print('Digite uma nota válida!!')
    
    print('Média: ', (nota1 + nota2)/2)

ex07()