
def ex1(lista):
    lista_nums = lista
    cont_pares = 0

    for nums in lista_nums:
        cont_pares += 1 if nums % 2 == 0 else 0

    print('Existem {} números pares na lista {}'.format(cont_pares, lista_nums))


ex1([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12])
