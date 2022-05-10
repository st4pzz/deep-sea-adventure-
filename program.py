import random # importaçao de uma biblioteca que utilizarei em umas das variaveis do jogo.
import time # importaçao de uma biblioteca que utilizarei para dar uma congelada entre uma frase/açao e outra para que o fluxo do jogo nao fique muito rapido e consequentemente dificulte a leitura e o gameplay.
from funcao_do_jogo import *
#Imagem de um mergulhador em ASCII e texto em ASCII para a introdução do game.
print()
print()
print_slow_asc(''' ...... .. ......... .. ......... ............ ............ ............ ~JPGBBGPJ^.. ......... ....
...................................................................... :YBBBBBBBGGP?:...............
......................................................................^G#BBBPPY?7777!!~.............
................................................................:. .. 5#BB5!?!~~~~^^~:~! ...........
........................................................:::^^^~~~~!??!BBBY:!?~~757^7G~:7............
.................................................::^^^~~~~~~~~~~~~7PY!GBB!.~?~~!7!!!~::7............
..............................................:^~~~~~~~~~~~~~~~~~~JG~:PBB?.:?7!!77~7!~!^ ...........
..................  .........................^~~~~~~~~~~~~~~!!7?J5BYY5YPBB?::!!~YGBGY:.....  .  ....
............ .. .:!7:  ......................^~~~~~~~~~~~7?JYYYYYBP5BBPJ5G#G?~:~#&###: ....7J^^7^...
     .. ...::::75B#&P~^:..     ......... .   .:^^~~!!!!?G5YYYYYYY5BBB##GJ~JB#BG5#&&&B:..  7#BGB#J ..
7JJY555PPGGBBB#&#####BBGP5Y?!~^:.. ....:^^~77?Y5PGGBP??5#PYYYYYYYJP##5Y5##P77J~.~JYJ^  :!YGBB#BB7 ..
:5&&########&#P?~!7J5PGB#####BBGP5Y55PGGBBBB##BBBBBBBP?J5GYYYYYYYPBBJ.  ^?GPGB55Y   .!YBBY~~!!~^ ...
  7B#######P?^.      .:^!7Y5PGB##########BBBBGGBBBBBBY77JB5YYYYYPBBJ. .   ~BBBB#?:!YGBP7: .     ....
.. ^P&##P?^.  ......7P5~... .:^!7?J?7?7!!!~!?YPBBBBBBBPJ5GGYYYJPBB? .:^7J5GBBBGBGG#GJ^. ............
... :J?^. .....   :5##&BGGP5YJ7!~^:....^!?5GBBBBBBBBB#577?5?7!JBBP?YPGBBPY?!~^:!Y5!. ...............
......  ..  ..:~!?G&#BGGBB######BBBGGPGBBBBBBBBBBBBG5Y7^:..  ~B#BGPY?!^:.    .. .. .................
....   .:^!?YPB##&#J~:..:~!7JY5PGBB#####BBBBGPYJ7~^:.  ......~?!~:.    .............................
...^!?YPB########5^ . ...    ...:^~!?JJ??!~^:..  ............    ...................................
...~G&&########P~ ...............           ........................................................
... .7B######G7. ...................................................................................
..... :JB##B?: .....................................................................................
 ...... ^55^. ...... .. ......... .. ......... .. ......... ......... .. ......... .. ......... .. .
''')
print()
time.sleep(0.8)
print_slow_asc('''
    ___                   __                                        ___    ____           __  ___              
   /   |_   _____  ____  / /___  ___________ _   ___  ____ ___     /   |  / / /_____     /  |/  /___ ______    
  / /| | | / / _ \/ __ \/ __/ / / / ___/ __ `/  / _ \/ __ `__ \   / /| | / / __/ __ \   / /|_/ / __ `/ ___/    
 / ___ | |/ /  __/ / / / /_/ /_/ / /  / /_/ /  /  __/ / / / / /  / ___ |/ / /_/ /_/ /  / /  / / /_/ / /        
/_/  |_|___/\___/_/ /_/\__/\__,_/_/   \__,_/   \___/_/ /_/ /_/  /_/  |_/_/\__/\____/  /_/  /_/\__,_/_/         
                                                                                                            ''')
print()
time.sleep(0.8)
# Boas vindas ao jogador .
print_slow('\n>Bem vind@s ao jogo Aventura em Alto Mar')
print()
time.sleep(0.8)
print_slow('\n>Boa sorte para encontrar tesouros valiosos e tome cuidado para nao ficar sem oxigenio =) ')
print()
#um loop para apresentar as regras do game ao jogador , caso ele queira.
while True :
    regras = input('>Voce deseja ler as regras do jogo ? s/n :')
    if regras == 's': 
        print_slow('\n>1.Respirar:Jogo verifica se há a necessidade de reduzir o oxigênio. O oxigênio deve ser reduzido de acordo com a quantidade de tesouros que o jogador estivere carregando.Caso o oxigenio alcance o nível 0 ou menor, o jogador da vez termina a rodada e o jogo acaba.')
        print()
        time.sleep(0.8)
        print_slow('\n>2.Avançar ou Retrodecer?: No início da partida o jogador começa dentro do submarino. Depois de sair do submarino ele deve escolher continuar avançando para o fundo do mar ou voltar para o submarino.')
        print()
        time.sleep(0.8)
        print_slow('\n>3.Nadar:Jogador rola dois dados d3 (Dado de três faces.) para verificar o avanço. A soma dos dois resultados do dado d3 representa a profundidade em que o mergulhador vai nadar.')
        print()
        time.sleep(0.8)
        print_slow('\n>4.Caça ao tesouro:Neste passo o jogador pode fazer uma busca por tesouros ou decidir soltar um dos tesouros que ele carrega.')
        print()
        time.sleep(0.8)
        break
    elif regras == 'n':
        break
    else:
        print_slow('\n>Digite sim ou nao para prosseguir:')
        print()
        time.sleep(0.8)




começa_jogo = True #variavel booleano para começar o loop do game.
while começa_jogo: # começo do loop
    #definindo as variaveis iniciais 
    oxigenio = 25
    profundidade = 1
    lista_tesouros = []
    contador_rodada = 1
    tesouros = 0
    qtd_niveis_avança = 0
    print_slow('\n>Voce esta dentro do submarino !') # o jogador começa o jogo dentro do submarino.
    print()
    time.sleep(0.8)
    input('\n>Digite (a) para avançar:') # ele precisa sair do submarino para começar a rodada.
    print()
    time.sleep(0.8)
    print_slow('\n>Voce saiu do submarino !') # agora a primeira rodada do jogo ira começar.
    print()
    time.sleep(0.8)
    loop_jogo = True # variavel booleano para começar o loop das rodadas e das açoes do personagem.
    while loop_jogo:
        print_slow(f'\n>RODADA {contador_rodada}') # imprime as rodadas em que o personagem se encontra.
        print()
        resumo_da_rodada(oxigenio,profundidade,lista_tesouros)
        input('\nPressione enter para respirar :')
        print()
        time.sleep(0.8)
        fase_respirar(oxigenio,lista_tesouros)
        oxigenio -= len(lista_tesouros)
        if oxigenio > 0 and oxigenio <= 1: # se a quantidade de oxigenio for pouca, é impresso uma mensagem dizendo que o oxigenio esta acabando e a proxima rodada do jogo sera a ultima que o personagem ira jogar.
            print_slow('\n>O oxigenio esta acabando !!!')
            print()
            time.sleep(0.8)
            print_slow('\n>Esta é a ultima rodada do jogo ! Boa sorte mergulhador')
            print()
            time.sleep(0.8)
        elif oxigenio <= 0:  #se o oxigenio for menor ou igual a 0 : significa que o oxigenio acabou e consequentemente, o jogo acabou. Sao apresentadas ao jogador a quantidade de tesouros que ele terminou e o valor dos tesouros, tambem é impressa a opçao de reiniciar o game ou nao.
            time.sleep(0.8)
            print_slow('\n>ACABOU O SEU OXIGENIO MERGULHADOR , PORTANTO O JOGO ACABOU!!!')
            print()
            print_slow(f'Voce terminou o jogo com {len(lista_tesouros)} tesouros e os valores dos tesouros que voce coletou foram : {lista_tesouros}')
            print()
            input('\n>Pressione enter para reiniciar o jogo ')
            print()
            break
        avançar_ou_retroceder = input('\n>Pressione (a) para avançar e (r) para retroceder :').lower() # funcao para o personagem escolher se ele quer avançar ou retornar.
        print()
        time.sleep(0.8)
        if avançar_ou_retroceder == 'a': # caso ele escolha avançar, sao rolados os dois dados aleatoriamente em um valor entre 1 e 3.
            Dado_1 = random.randint(1,3)
            Dado_2 = random.randint(1,3)
            if len(lista_tesouros) == 0:
                qtd_niveis_avança = Dado_1 + Dado_2
            else:
                qtd_niveis_avança = Dado_1 + Dado_2 - len(lista_tesouros)
            profundidade += qtd_niveis_avança
            if profundidade >= 32: # se ele ultrapassar o limite de profundidade do jogo, ele retorna ao ultimo nivel e continua o jogo normalmente.
                profundidade = 32
                rolar_dados_avançar(Dado_1,Dado_2,profundidade,qtd_niveis_avança)
                print_slow('Voce chegou no nivel maximo de profundidade mergulhador, voce precisa retornar.')
                print()
            else:
                rolar_dados_avançar(Dado_1,Dado_2,profundidade,qtd_niveis_avança)
            if Dado_1 + Dado_2 <= len(lista_tesouros):
                rolar_dados_que_pena(lista_tesouros,Dado_1,Dado_2)
                time.sleep(0.8)
        elif avançar_ou_retroceder == 'r':# caso ele escolha avançar, sao rolados os dois dados aleatoriamente em um valor entre 1 e 3.
            Dado_1 = random.randint(1,3)
            Dado_2 = random.randint(1,3)
            if len(lista_tesouros) == 0:
                qtd_niveis_avança = Dado_1 + Dado_2
            else:
                qtd_niveis_avança = Dado_1 + Dado_2 - len(lista_tesouros)
            profundidade -= qtd_niveis_avança
            if profundidade <= 0 and len(lista_tesouros) > 0: # se a variavel profundidade atingir o valor (0) ou menos, significa que o personagem chegou no submarino , sao apresentados o numero de tesouros que ele terminou e o valor dos tesouros , o jogo acaba e a opcao de reiniciar o game é apresenada.
                print_slow('\n>PARABENS MERGULHADOR !! Voce chegou no submarino ! ')
                print()
                time.sleep(0.8)
                print_slow(f'Voce terminou o jogo com {tesouros} tesouros e seus tesouros sao : {lista_tesouros}')
                print()
                time.sleep(0.8)
                print_slow('\n>O JOGO ACABOU!!!')
                print()
                input('\n>Pressione enter para reiniciar o jogo :')
                print()
                break
            elif profundidade <= 0 and len(lista_tesouros) == 0: # o personagem nao pode retornar ao submarino sem tesouros , entao é impressa uma frase dizendo isso.
                print_slow('Voce nao pode retornar ao submarino sem tesouros mergulhador, por favor continue jogando.')
                print()
                profundidade = 1
            elif profundidade >0 and profundidade <= 32 :
                if Dado_1 + Dado_2 > len(lista_tesouros) :
                    rolar_dados_retroceder(Dado_1,Dado_2,profundidade,qtd_niveis_avança)
                elif Dado_1 + Dado_2 <= len(lista_tesouros):
                    rolar_dados_que_pena(lista_tesouros,Dado_1,Dado_2)
                    time.sleep(0.8)
        nova_rodada_ou_vasculhar = input('\n>Pressione (i) para iniciar uma nova rodada ou (v) para vasculhar o fundo do mar :') # funcao para perguntar ao personagem se ele quer iniciar uma nova rodada e avançar/retornar ou vasculhar o fundo do mar.
        print()
        time.sleep(0.8)
        # a variavel tesouros é definida a partir do nivel de profundidade em que o personagem se encontra.
        if 1 <= profundidade <= 8:
            tesouros = random.randint(0,3)
        elif 9 <= profundidade <= 16:
            tesouros = random.randint(4,7)
        elif 17 <= profundidade <= 24:
            tesouros = random.randint(8,11)
        elif 25 <= profundidade <= 32:
            tesouros = random.randint(12,15)
        if nova_rodada_ou_vasculhar == 'v':# se o personagem escolher vasculhar, é impressa uma mensagem informando o valor do tesouro que ele encontrou e se ele quer coletar o tesouro ou nao.
            time.sleep(0.8)
            print_slow(f'\n>Voce encontrou um tesouro que vale {tesouros}')
            print()
            coleta_tesouro = input('\nPressione (c) para coletar o tesouro ou (enter) para continuar o jogo :')
            print()
            if coleta_tesouro == 'c' :
                if len(lista_tesouros) >= 0 and len(lista_tesouros) < 4:
                    lista_tesouros.append(tesouros)
                    print_slow('\nVoce coletou o tesouro ! iniciando nova rodada...')
                    print()
                elif len(lista_tesouros) == 4:# o personagem nao pode coletar tesouros se ele ja estiver carregando 4 tesouros , por isso ele obrigatoriamente precisa soltar algum de seus tesouros para coletar um novo.
                    print_slow(f'\n>Voce ja possui 4 tesouros, por isso, voce precisa soltar algum de seus tesouros para coletar um novo.')
                    print()
                    print_slow(f'\n>Seus tesouros sao : {lista_tesouros}')
                    print()
                    valores_tesouros = int(input('\n>Indique qual tesouro deseja soltar:'))
                    print()
                    lista_tesouros.remove(valores_tesouros)
                    print_slow(f'\n>Voce soltou o tesouro de valor ({valores_tesouros})')
                    print()
                    lista_tesouros.append(tesouros)
                    print_slow('\nVoce coletou o tesouro ! iniciando nova rodada...')
                    print()
                    time.sleep(0.8)
            else:
                print_slow('\nVoce escolheu nao coletar o tesouro ! iniciando nova rodada... ')  
                print()      
            time.sleep(0.8)
        elif nova_rodada_ou_vasculhar == 'i':
            print_slow('\n>Iniciando nova rodada... ')
        contador_rodada += 1