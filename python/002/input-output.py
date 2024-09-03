valor = int(input('Digite o valor a sacar:'))

notas_ans = {}
notas_available = [50, 20, 10]

def calcularnotas(nota, valor, idx_notas):
    notas_ans[nota] = (valor//nota)
    if(idx_notas <= len(notas_available)):
        print(notas_ans)
        idx_notas+=1
        try:
            calcularnotas(notas_available[idx_notas], valor % (valor/nota), idx_notas)
        except:
            return       
    return

calcularnotas(notas_available[0], valor, 0)

print(notas_ans)
