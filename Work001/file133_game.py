
from file133_models.calcular import Calcular


def main() -> None:
    pontos: int = 0
    jogar(pontos)


def jogar(pontos: int) -> None:
    dificuldade: int = int(input('Informe o nível de dificuldade desejado [1, 2, 3 ou 4]: '))
    calc: Calcular = Calcular(dificuldade)

    print('Informe o resultado para a seguinte operação: ')
    calc.mostrar_operacao()

    resultado: int = int(input())
    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Você tem {pontos} ponto(s).')

    continuar: int = int(input('Deseja continuar no jogo? [1 - sim, 0 - não] '))

    if continuar:
        jogar(pontos)
    else:
        print(f'Você finalizou com {pontos} ponto(s).')
        print('Até a próxima')


if __name__ == '__main__':
    main()

"""

Informe o nível de dificuldade desejado [1, 2, 3 ou 4]: 1
Informe o resultado para a seguinte operação: 
10 + 9 = ? 
19
Resposta correta!
10 + 9 = 19
Você tem 1 ponto(s).
Deseja continuar no jogo? [1 - sim, 0 - não] 1
Informe o nível de dificuldade desejado [1, 2, 3 ou 4]: 2
Informe o resultado para a seguinte operação: 
36 - 31 = ? 
5
Resposta correta!
36 - 31 = 5
Você tem 2 ponto(s).
Deseja continuar no jogo? [1 - sim, 0 - não] 1
Informe o nível de dificuldade desejado [1, 2, 3 ou 4]: 3
Informe o resultado para a seguinte operação: 
705 * 435 = ? 
1325
Resposta errada!
705 * 435 = 306675
Deseja continuar no jogo? [1 - sim, 0 - não] 0
Você finalizou com 2 ponto(s).
Até a próxima
1--------------
2--------------

Process finished with exit code 0


"""

print('1--------------')
print('2--------------')