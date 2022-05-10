import sys
import time
def print_slow_asc(str): # funçao que pega a arte que fiz pelo ASCII e imprime ela de pouco em pouco e nao de uma vez só.
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.001)
def print_slow(str): # funçao que pega uma frase e imprime ela de pouco em pouco e nao de uma vez só.
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02)
def resumo_da_rodada(oxigenio,profundidade,lista_tesouros): # funcao que imprime o resumo de cada rodada do jogo: indicando o oxigenio, profundidade , a quantidade de tesouros e o valor dos tesouros que o personagem está em cada rodada.
    print_slow(f'''\n
    >RESUMO DA RODADA:
    >O nível do oxigenio está em {oxigenio}
    >Voce esta no nivel {profundidade} de profundidade
    >Voce esta com {len(lista_tesouros)} tesouros.
    >Seus tesouros sao : {lista_tesouros}
    ''')
    print()
def fase_respirar(oxigenio,lista_tesouros):# funcao que imprime a fase em que o personagem precisa respirar: indicando o nivel do oxigenio que ele estava ate a rodada atual, o tanto que ele consumiu (dependente da quantidade de tesouros que carrega) na rodada e consequentemente o oxigenio da rodada atual (anterior - consumiu).
    print_slow(f'''\n
    >O nível do oxigenio está em {oxigenio}
    >Voce consumiu {len(lista_tesouros)} de oxigenio nesta rodada !
    >O nivel atual de oxigenio esta em {oxigenio - len(lista_tesouros)}
    ''')
    print()
def rolar_dados_avançar(Dado1,Dado2,profundidade,qtd_niveis_avança):# funcao que imprime a quantidade de casas que o personagem ira avançar: depende do valor dos dois dados que sao rolados aleatoriamente, e a quantidade de casas que ele ira avançar corresponde a soma dos dois dados subtraido da quantidade de tesouros que ele carrega.
    print_slow(f'''\n
    >Voce está avançando para o fundo do mar ! 
    >Os dados foram rolados e voce tirou Dado 1: ({Dado1}) Dados 2: ({Dado2}) 
    >Voce andou {qtd_niveis_avança} nesta rodada e agora voce esta na profundidade {profundidade}
    ''')
    print()
def rolar_dados_que_pena(lista_tesouros,Dado1,Dado2):# funcao que imprime quando a soma dos dois dados rolados aleatoriamente é menor ou igual a quantidade de tesouros que o personagem carrega, ou seja, o personagem nao conseguira avançar nem retornar.
    print_slow(f'''\n
    >Que pena ! 
    >Voce nao conseguiu andar nessa rodada ! Voce esta carregando {len(lista_tesouros)} tesouros e voce tirou {Dado1 + Dado2} na soma dos dados
    ''')
    print()
def rolar_dados_retroceder(Dado1,Dado2,profundidade,qtd_niveis_avança): # funcao que imprime a quantidade de casas que o personagem ira retornar : depende do valor dos dois dados que sao rolados aleatoriamente, e a quantidade de casas que ele ira retornar corresponde a soma dos dois dados subtraido da quantidade de tesouros que ele carrega.
    print_slow(f'''\n
    >Voce está voltando para o submarino ! 
    >Os dados foram rolados e voce tirou Dado 1: ({Dado1}) Dados 2: ({Dado2}) 
    >Voce andou {qtd_niveis_avança} nesta rodada e agora voce esta na profundidade {profundidade}
    ''')
    print()
    