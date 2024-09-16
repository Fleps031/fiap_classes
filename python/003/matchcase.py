systemChoices = ['Saindo...', 'Cadastrando...', 'Consultando...', 'Editando...', 'Excluindo...']

print(f""" 
0 - sair
1 - cadastar
2 - consultar
3 - editar
4 - excluir
""")

choice = int(input('// '))

print(systemChoices[choice])
