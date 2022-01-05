import csv


def ex1_ler_arquivo(arquivo, delim=','):
    with open(arquivo, 'r') as arq:
        leitor = csv.reader(arq, delimiter=delim)
        for linha in leitor:
            print(linha)


def ex2_copiar_arquivo(arquivo, delim, arquivo2):
    linha_copia = []

    with open(arquivo, 'r') as arq:
        leitor = csv.reader(arq, delimiter=delim)
        for linha in leitor:
            linha_copia.append(linha)
    with open(arquivo2, 'w', newline='') as arq2:
        escritor = csv.writer(arq2)
        escritor.writerows(linha_copia)


def ex2_arquivo_media(arquivo, delim, arquivo2):
    linha_copia = []

    with open(arquivo, 'r') as arq:
        leitor = csv.reader(arq, delimiter=delim)
        for linha in leitor:
            linha.append('Media')
            linha_copia.append(linha)  # header
            break
        # leitura acima faz essa abaixo começar de onde esta acima parou
        for linha in leitor:
            media = (float(linha[3])+float(linha[4])+float(linha[5])+float(linha[6])) / 4
            linha.append(str(media))
            linha_copia.append(linha)

    with open(arquivo2, 'w', newline='') as arq2:
        escritor = csv.writer(arq2)
        escritor.writerows(linha_copia)


# ex1_ler_arquivo('alunos.csv')
# ex2_copiar_arquivo('alunos.csv', ',', 'alunos_copia.csv')
ex2_arquivo_media('alunos.csv', ',', 'alunos_media.csv')
