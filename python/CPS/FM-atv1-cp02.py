#Aluno: Felipe Gomes Molinari Lopes
#RM: 559885

votos1 = 0
votos2 = 0
votos3 = 0
nulos = 0

votos1Percentual = 0
votos2Percentual = 0
votos3Percentual = 0
nulosPercentual = 0

totalVotos = 0

vencedor = 'Nulos'


print('CANDIDATOS')
candidato1 = input("Candidato 1: ")
candidato2 = input("Candidato 2: ")
candidato3 = input("Candidato 3: ")

while True:
    print(f"""
    CANDIDATOS
    1 - {candidato1}
    2 - {candidato2}
    3 - {candidato3}
    0 - FIM DA VOTAÇÃO
    """)
    votoInput = input('VOTO: ')
    if votoInput.isnumeric():
        voto = int(votoInput)
        if voto == 0:
            break
        match voto:
            case 1:
                votos1+=1
            case 2:
                votos2+=1
            case 3:
                votos3+=1
            case _:
                nulos+=1
    else:
        nulos+=1

totalVotos = votos1 + votos2 + votos3 + nulos

if totalVotos == 0:
    vencedor = 'Nulos'
else:
    if votos1 > 0:
        votos1Percentual = votos1/totalVotos * 100
    if votos2 > 0:
        votos2Percentual = votos2/totalVotos * 100
    if votos3 > 0:
        votos3Percentual = votos3/totalVotos * 100
    if nulos > 0:
        nulosPercentual = nulos/totalVotos * 100

    if votos1 > votos2 and votos1 > votos3 and votos1 > nulos:
        vencedor = candidato1
    elif votos2 > votos1 and votos2 > votos3 and votos2 > nulos:
        vencedor = candidato2
    elif votos3 > votos1 and votos3 > votos2 and votos3 > nulos:
        vencedor = candidato3

    if votos1 > 0 and votos1 == votos2 and votos2 == votos3 and votos3 == nulos:
        vencedor = 'Empate!'

print(f""" 
    CANDIDATOS
    TOTAL DE VOTOS: {totalVotos}
    1 - {candidato1} -> {votos1} votos - {votos1Percentual:.2f}%
    2 - {candidato2} -> {votos2} votos - {votos2Percentual:.2f}%
    3 - {candidato3} -> {votos3} votos - {votos3Percentual:.2f}%
    Nulos -> {nulos} votos - {nulosPercentual:.2f}%
    
    Vencedor: {vencedor}
""")