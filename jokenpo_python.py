# Crie um programa que o computador jogue jokempo com vc
import random as ran
import time

def nome_jogo():
    print('=' * 30)
    print('JOKENPÔOOOOÔ!!!!')
    print('=' * 30)


def machine_play():
    opt = [1, 2, 3]
    play = ran.choice(opt)
    return play


def result(opt1, opt2):
    global emp, playerwon, cpuwon
    if opt1 == opt2:
        emp += 1
        return 'EMPATE!!!'
    else:
        if opt1 == 1 and opt2 == 2:
            cpuwon += 1
            return 'EU VENCI!!!'
        elif opt1 == 2 and opt2 == 1:
            playerwon += 1
            return 'VOCÊ VENCEU!!!'
        elif opt1 == 1 and opt2 == 3:
            playerwon += 1
            return 'VOCÊ VENCEU!!!'
        elif opt1 == 3 and opt2 == 1:
            cpuwon += 1
            return 'EU VENCI!!!'
        elif opt1 == 3 and opt2 == 2:
            playerwon += 1
            return 'VOCÊ VENCEU!!!'
        elif opt1 == 2 and opt2 == 3:
            cpuwon += 1
            return 'EU VENCI!!!'


emp = 0
playerwon = 0
cpuwon = 0
memory = []
x = 1
print('THE JOKENPÔOOOOÔ MACHINE!!!')
player = input('Digite seu NICK e vamos jogar: ')
while x == 1:
    try:
        options = ('', 'PEDRA', 'PAPEL', 'TESOURA')
        nome_jogo()
        ctrl = int(input('[1] - PEDRA!\n[2] - PAPEL!\n[3] - TESOURA!\n[0] SAIR...\n >>>> '))
        if ctrl > 0 and ctrl <= 3:
            mply = machine_play()
            print('JOKENPÔOOOOÔ!!!!')
            time.sleep(2)
            wnr = result(ctrl, mply)
            print('Eu escolhi {} e você {}\n{}'.format(options[mply], options[ctrl], wnr))
            memory.append([ctrl, mply, wnr])
            time.sleep(2)
        elif ctrl == 0:
            x = 0
        else:
            print('VOCÊ NÃO ESCOLHEU UMA OPÇÃO VÁLIDA!!!')
    except (ValueError):
        print('VOCÊ NÃO ESCOLHEU UMA OPÇÃO VÁLIDA!!!')

comp = 'THE JOKENPÔOOOÔ MACHINE!!!'
if cpuwon > playerwon:
    winner = comp
elif cpuwon == playerwon:
    winner = 'Empatamos!!!'
else:
    winner = player
for mem in memory:
    print(mem, end='\n')
print('Foi uma disputa incrível, eu ganhei de você por {} vezes e vc ganhou de mim {} vezes\n'
      'e empatamos em {} jogadas. E no fim quem ganhou foi...\n\n {}\n'.format(cpuwon, playerwon, emp, winner.upper()))
print('Encerrando o programa....')
