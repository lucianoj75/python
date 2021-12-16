
def ex1():
    while True:
        try:
            vlr_monetario = float(input('Informe um valor monetário para diminuição em 15%:'))
            break
        except ValueError:
            print('Entre com valor numérico. Use ponto para valor decimal.')

    print('O novo valor é: {}'.format(vlr_monetario * 0.85))

def ex2():
    while True:
        try:
            idade = int(input('Digite sua idade:'))
            if not(idade in range(0,51)):
                print('Idade inválida. Informe entre 0 e 50.')
            else:
                break
        except ValueError:
            print('Entre com valor numérico.')

    while True:
        try:
            salario = float(input('Digite seu salário:'))
            if salario <= 0:
                print('Informe valor maior que zero.')
            else:
                break
        except ValueError:
            print('Entre com valor numérico. Use ponto para decimais.')

    while True:
        sexo = input('Digite seu sexo:')
        if not(sexo.upper() in ['M', 'F', 'OUTRO']):
            print('Sexo inválido. (M;F;Outro)')
        else:
            break

def ex3():
    lst_perguntas = [
        'Mora perto da vítima?',
        'Já trabalhou com a vítima?',
        'Teleonou para a vítima?',
        'Esteve no local do crime?',
        'Devia para a vítima?'
    ]
    ponto = 0

    for pergunta in lst_perguntas:
        while True:
            resposta = input(pergunta)
            if not(resposta.upper() in ['SIM','NÃO']):
                print('Responda com Sim ou Não. Não enrole!!!')
            else:
                break
        ponto += 1 if resposta.upper() == 'SIM' else False

    if ponto == 5:
        print('Vc é assassino.')
    elif ponto in [3,4]:
        print('Vc é cúmplice.')
    elif ponto == 2:
        print('Vc é suspeito.')
    else:
        print('Ok, liberado.')

def ex4():
    for mult in range(1,11):
        print('9*{}={}'.format(mult,9*mult))

print('*EXERCÍCIO 1*')
ex1()

print('*EXERCÍCIO 2*')
ex2()

print('*EXERCÍCIO 3*')
ex3()

print('*EXERCÍCIO 4*')
ex4()
