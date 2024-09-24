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

ex04()