def funcao1():
    print('codando em python -> paralelo 3')


if __name__ == '__main__':
    funcao1()
    print('paralelo 3 está sendo executado diretamente')
else:
    print(f'paralelo 3 foi importado, {__name__}')
