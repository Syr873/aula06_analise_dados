#ATIVIDADES
#Desafio Analise de desempenho escolar
for n in range(10):
    nome = input('Informe o nome do aluno: ')
    nota01 = float(input('Informe a nota 01: '))
    nota02 = float(input('Informe a nota 02: '))
    nota03 = float(input('Informe a nota 03: '))
    nota04 = float(input('Informe a nota 04: '))
    media = (nota01 + nota02 + nota03 + nota04)/ 4

    print(f'A média de {nome} é {media:.2f}')

    if media >= 7:
        print('Aprovado!')
    elif 5 <= media < 7:
        print('Recuperação!')
    else:
        print('Reprovado!')

  

    



