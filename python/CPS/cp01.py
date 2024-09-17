#ALUNO: Felipe Gomes Molinari Lopes
#RM: 559885

saleAmount = input('Venda.......................: ')
hasCoupon = input('Tem cupom, [s]im ou [n]ão?..: ')

couponAmount = 0
discountPercentage = 0
discountAmount = 0


isSaleAmountValid: False
isHasCouponValid: False



if saleAmount.isnumeric():
    isSaleAmountValid = True
    saleAmount = int(saleAmount)
else:
    print('Digite um valor válido para a venda!')


match hasCoupon:        
    case 's':
        isHasCouponValid = True
        couponAmount = 50
    case 'n':
        isHasCouponValid = True
    case _:
        print("Digite 's' ou 'n' ")        

if isSaleAmountValid and isHasCouponValid:
    if(saleAmount <= 1000):
        discountPercentage = 0.05
    else:
        discountPercentage = 0.1

    discountAmount = saleAmount * discountPercentage
    finalAmount = saleAmount - discountAmount - couponAmount

    print('RELATÓRIO:')
    print(f'Venda...........: {saleAmount:.2f}')
    print(f'Desconto........: {discountAmount:.2f}')
    print(f'Cupom...........: {couponAmount:.2f}')
    print(f'Venda final.....: {finalAmount:.2f}')

