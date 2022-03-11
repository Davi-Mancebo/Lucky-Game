from time import sleep
from random import randint

comecar = ''
escolha = ' '
n1 = 0

txt = "JOGO DA SORTE/GAME OF LUCKY"
c = txt.center(50, " ")
print("-=" * 25)
print(c)
print("-=" * 25)

while True:
    lingua = str(input("What language do you want for the game?([P]ortuguês/[E]nglish) ")).strip().upper()[0]
    if lingua == 'P' or lingua == 'E':
        break
    else:
        print('Digite apenas P ou E\nJust type P or E\n')
        sleep(1.5)
# Acima fica a função para a seleção da lingua do game

if lingua == "E":
    print("""This game is very simple, you will select value from 1 to 5 and play against the computer,
if you choose the same computer number you win, if not you lose""")
    for c in range(1, 5):
        print('.', end=' ')
        sleep(2)
    print('\n')
    while True:
        while True:
            n1 = int(input('type a number of 1-5: '))
            if n1 > 5:
                print('Enter a number equal to or less than 5\n')
                sleep(1)
            elif n1 < 1:
                print('Enter a number greater than or equal to 1\n')
                sleep(1)
            else:
                break

        print('this will be a test of lucky!')
        for c in range(1, 5):
            print('.', end=' ')
            sleep(0.5)
        alea = randint(1, 5)

        print(f'\nThe computer choose {alea}, and you choose {n1}')
        sleep(1)

        if n1 == alea:
            print('You win!!')
        else:
            print('Computer Win!!')

        while escolha not in 'YN':
            escolha = str(input('\nPlay again? [Y/N]')).strip().upper()[0]

        if escolha == 'N':
            break
        print('=-' * 30)

        escolha = ' '  # necessario para código funcionar#

    print('\nThanks For play!')
else:
    print("""Este jogo é muito simples, você selecionará o valor de 1 a 5 e jogará contra o computador,
se você escolher o mesmo número de computador você ganha, se não você perde""")
    for c in range(1, 5):
        print('.', end=' ')
        sleep(2)
    print('\n')
    while True:
        while True:
            n1 = int(input('digite um numero inteiro de 1-5: '))
            if n1 > 5:
                print('Digite um numero igual ou inferior a 5\n')
                sleep(1)
            elif n1 < 1:
                print('Digite um numero superior ou igual a 1\n')
                sleep(1)
            else:
                break

        print('isso sera um teste de sorte')
        for c in range(1, 5):
            print('.', end=' ')
            sleep(0.5)
        alea = randint(1, 5)

        print(f'\nO computador tirou {alea}, e você escolheu {n1}')
        sleep(1)

        if n1 == alea:
            print('você venceu!!')
        else:
            print('Computador venceu!!')

        while escolha not in 'SN':
            escolha = str(input('\nDeseja continuar? [Sim/Não] ')).strip().upper()[0]

        if escolha == 'N':
            break
        print('=-' * 30)

        escolha = ' '  # necessario para código funcionar#

    print('\nobrigado por participar!')
