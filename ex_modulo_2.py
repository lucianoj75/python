
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
    for pos_lista1, item_lista1 in enumerate(lista1):
        lista_sum.append(item_lista1 + lista2[pos_lista1])
    return lista_sum


# ex1([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12])
#ex2()
print(ex3([1, 2, 3], [4, 5, 6]))
