
def ex1(lista):
    lista_nums = lista
    cont_pares = 0

    for nums in lista_nums:
        cont_pares += 1 if nums % 2 == 0 else 0

    print('Existem {} números pares na lista {}'.format(cont_pares, lista_nums))

def ex2():
    for letra in input('Digite uma palavra:'):
        print(letra)

def ex3(*args):
    lista1, lista2 = args
    lista_sum = []

    lista_sum = list(map(lambda x,y: x+y, lista1, lista2))

#    for pos_lista1, item_lista1 in enumerate(lista1):
#        lista_sum.append(item_lista1 + lista2[pos_lista1])

    return lista_sum

def ex4_5():
    dct_meses_dias = {
        'janeiro': 31,
        'fevereiro': 28,
        'março': 31,
        'abril': 30,
        'maio': 31,
        'junho': 30,
        'julho': 31,
        'agosto': 31,
        'setembro': 30,
        'outubro': 31,
        'novembro': 30,
        'dezembro': 31
    }
    for chave in dct_meses_dias:
        print(f'Mês {chave} tem {dct_meses_dias[chave]} dias')

ex1([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12])
ex2()
print(ex3([1, 2, 3], [4, 5, 6]))
ex4_5()
