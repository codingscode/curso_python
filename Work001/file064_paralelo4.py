import file064_paralelo3


def funcao2():
    file064_paralelo3.funcao1()


if __name__ == '__main__':
    funcao2()
    print('paralelo 4 está sendo executado diretamente')
else:
    print(f'paralelo 4 foi importado, {__name__}')
