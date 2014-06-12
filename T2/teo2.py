# -*- coding: utf-8 -*-

from pygraph.classes.graph import graph
from pygraph.algorithms.accessibility import connected_components

def teo_2(g, k):
  # Salvaguarda
  if k > len(g.nodes()):
    raise ValueError('FORBIDDEN: K > |V|')
  if k <= 0:
    raise ValueError('FORBIDDEN: K <= 0')

  # Caso base
  if k == 1:
    forest = graph()
    for node in g.nodes():
      forest.add_node(node)
    return forest

  # Hipotese indutiva
  forest = teo_2(g, k-1)

  # Enquanto ainda houverem componentes conexos
  # que nao satisfazem a condicao
  while True:
    # Atualiza a lista de componentes, pois pode ter
    # mudado durante a adicao
    cc = _transform_cc(connected_components(forest))
    
    # Seleciona um que tenha comprimento < k
    selected_component = None
    for component in cc:
      if len(component) < k:
        selected_component = component
        break

    # Se nao conseguiu selecionar, significa que todos
    # satisfazem comprimento >= k, e podemos parar o while
    if selected_component == None:
      break

    # Caso haja um selecionado, selecionar a aresta de menor
    # peso que tenha somente um dos vertices em selected_component
    edges = g.edges()
    used_edges = forest.edges()
    unused_edges = [e for e in edges if e not in used_edges]
    neighbor_edges = [e for e in unused_edges if e[0] in selected_component]

    min_edge = min(neighbor_edges, key=lambda e: g.edge_weight(e))
    forest.add_edge(min_edge)

  return forest


def _transform_cc(cc):
  """
  The "connected components" structure returned
  by the function in pygraph is a dict mapping each
  node to an id.
  We'll make a new structure which is a list of lists
  of nodes that are in the same connected component.
  """
  inv_map = {}
  for k, v in cc.iteritems():
    inv_map[v] = inv_map.get(v, [])
    inv_map[v].append(k)
  return inv_map.values()


if __name__ == '__main__':
  # Codigo usado para testar com diferentes valores de x, y, e k
  # Uso:
  #   python teo2.py k arq.tsp
  #     k - o parâmetro K do teorema
  #     arq.tsp - arquivo contendo uma tupla (id, x, y) por linha
       
  import tsp_reader
  import sys
  from time import time

  EXECS_PER_LOOP = 1
  TIME_THRESHOLD = 5

  k = int(sys.argv[1])
  tsp_file = sys.argv[2]
  tsp_str = open(tsp_file).read()
  g = tsp_reader.read(tsp_str)

  if k == -1:
    k = len(g.nodes())

  if k > len(g.nodes()):
    raise ValueError('FORBIDDEN: K > |V|')

  # Executa EXECS_PER_LOOP vezes a cada vez, ate passar de TIME_THRESHOLD segundos
  start = time()
  execs = 0
  while time() - start < TIME_THRESHOLD:
      execs += EXECS_PER_LOOP
      for i in range(EXECS_PER_LOOP):
          f = teo_2(g, k)
  end = time()
  elapsed = end - start

  print("k = %d" % k)
  print("file = %s" % tsp_file)
  print("time/exec = %.6f ms" % (1000*elapsed/execs))
  print
