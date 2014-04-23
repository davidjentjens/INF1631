#!/usr/bin/env python

# Implementacao do algoritmo
# O retorno eh uma lista de rounds
# Um round eh uma lista de jogos
# Um jogo eh uma tupla indicando os dois times
def tournament(k, start = 1):
    # Caso base
    if k == 1:
        return [[(start, start+1)]]

    # MOMENTO 1 - divide em dois
    
    # Recursao
    t1 = tournament(k-1, start)
    t2 = tournament(k-1, 2**(k-1)+start)

    # Unir os rounds dos dois torneios
    t = []
    for i in range(len(t1)):
        t.append(t1[i] + t2[i])

    # MOMENTO 2 - ciclo
    
    # Geracao das listas de times
    times1 = range(start, 2**(k-1)+start)
    times2 = range(2**(k-1)+start, 2**(k)+start)
    
    # z vai ser a variavel que faz o ciclo
    for z in range(len(times1)):
        # Estamos em um round
        round = []
        for i in range(len(times1)):
            # Estamos em um par dentro do ciclo
            
            # index1 eh simplesmente i
            # index2 muda de modo a fazer o ciclo no segundo grupo
            index1 = i
            index2 = (i + z) % len(times2)

            game = (times1[index1], times2[index2])
            round.append(game)

        # Adicionamos esse round ao conjunto de rounds, t
        t.append(round)

    return t
    
# Recebe uma lista que representa os rounds de um torneio, 
# i.e., recebe o retorno de tournament
def print_tournament(t):
    for round, games in enumerate(t):
        print("Round #%02d" % (round+1))
        for game, teams in enumerate(games):
            print("  Game #%02d: %d vs %d" % (game+1, teams[0], teams[1]))

if __name__ == '__main__':
    # Codigo usado para testar com diferentes valores de k
    # Uso:
    #   python 3.py k
    #     k - valor de k
    
    from time import time
    import sys

    TIME_TRESHOLD = 5
    EXEC_TRESHOLD = 5

    k = int(sys.argv[1])

    # Executa no minimo 3 vezes
    # Executa no minimo por 5 segundos
    start = time()
    execs = 0
    while not (execs > EXEC_TRESHOLD and time() - start > TIME_TRESHOLD):
        execs += 1
        tournament(k)
    end = time()
    elapsed = end - start

    print("%d & %d & %.3f s & %.6f ms \\\\" % (k, execs, elapsed, 1000*elapsed/execs))
