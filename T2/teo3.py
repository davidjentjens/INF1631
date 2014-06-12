# -*- coding: utf-8 -*-

def teo_3(costs, rewards, energy):
  # Salvaguarda
  if energy < 0:
    raise ValueError("Invalid energy!!")

  # Dict cujas chaves sao tuplas (posicao, energia) e cujos valores
  # sao tuplas contendo o premio maximo que o rei consegue coletar
  # comecando da posicao dada, com dada energia disponivel, e parando na 
  # posicao 0 com 0 energia, e o caminho para tal
  memo = {}

  # Caso base -- q=0
  memo[(0, 0)] = (0, [0])
  for v in range(1, 64):
    memo[(v, 0)] = None

  # Hipotese indutiva e passo indutivo -- preencher a tabela
  # Para cada coluna de energia
  for q in range(1, energy+1):
    # Para cada vertice nessa coluna
    for v in range(64):
      # custo_vizinho e a coluna em que vamos olhar
      custo_vizinho = q - costs[v]
      vizinhos = find_neighbors(v)
      if custo_vizinho < 0:
        memo[(v, q)] = None
      else:
        # Filtra as celulas -- somente se nao for impossivel (not None)
        # e pega a tupla (premio, caminho) delas
        tuplas = [memo[(vizinho, custo_vizinho)] for vizinho in vizinhos if not memo[(vizinho, custo_vizinho)] == None]
        if len(tuplas) > 0:
          # O melhor_vizinho e o que tem maior premio
          melhor_vizinho = max(tuplas, key=lambda x: x[0])
          # O novo_premio e o premio do melhor vizinho somado ao do vertice em questao
          novo_premio = melhor_vizinho[0] + rewards[v]
          # O novo_caminho e o caminho do melhor vizinho acrescido do vertice em questao
          novo_caminho = melhor_vizinho[1][:] + [v]
          memo[(v, q)] = (novo_premio, novo_caminho)
        else:
          memo[(v, q)] = None

  # Com a tabela em maos, vamos encontrar o caminho comecando em 0
  # que obtenha o maior premio possivel, utilizando qualquer quantidade
  # de energia menor que a fornecida
  maior = 0
  for q in range(energy, -1, -1):
    x = memo[(0, q)]
    if x != None and x[0] > maior:
      maior = x[0]
      inst = x + (q,)
  return inst


def find_neighbors(pos):
  x = pos/8
  y = pos%8

  naive = [(x-1, y-1), (x-1, y), (x-1, y+1),
           (x,   y-1),           (x,   y+1),
           (x+1, y-1), (x+1, y), (x+1, y+1)]
  filtered = [n for n in naive if n[0]>=0 and n[1]>=0 and n[0]<8 and n[1]<8]

  return map(lambda pos: pos[0]*8+pos[1], filtered)



if __name__ == '__main__':
  # Codigo usado para testar 
  # Uso:
  #   python 3.py

  import sys
  from time import time

  EXECS_PER_LOOP = 100
  TIME_THRESHOLD = 5

  # Ler o arquivo de entrada
  problems = []
  with open('walk.in') as f:

    # Ler o 
    q = int(f.readline().strip())
    while q != 0:
      costs   = sum([map(int, f.readline().strip().split(' ')) for i in range(8)], [])
      rewards = sum([map(int, f.readline().strip().split(' ')) for i in range(8)], [])

      problems.append({'energy': q, 'costs': costs, 'rewards': rewards})

      # Next
      q = int(f.readline().strip())

  # USED TO MEASURE TIME
  # for n, problem in enumerate(problems):
  #   # Executa EXECS_PER_LOOP vezes a cada vez, ate passar de TIME_THRESHOLD segundos
  #   start = time()
  #   execs = 0
  #   while time() - start < TIME_THRESHOLD:
  #       execs += EXECS_PER_LOOP
  #       for i in range(EXECS_PER_LOOP):
  #         solution = teo_3(problem['costs'], problem['rewards'], problem['energy'])
  #   end = time()
  #   elapsed = end - start

  #   print("num = %d" % n)
  #   print("time/exec = %.6f ms" % (1000*elapsed/execs))
  #   print

  for problem in problems:
    solution = teo_3(problem['costs'], problem['rewards'], problem['energy'])
    print solution[0]
    print solution[2]
    print q
    print ' '.join(str(x) for x in solution[1])
