# -*- coding: utf-8 -*-

from pygraph.classes.graph import graph
from pygraph.algorithms.accessibility import connected_components
from random import randrange

def teo_2(g, k):
  # Salvaguarda
  if k > len(g.nodes()):
    raise ValueError('FORBIDDEN: K > |V|')

  # Caso base
  if k == 1:
    forest = graph()
    for node in g.nodes():
      forest.add_node(node)
    return forest

  # Hipótese indutiva
  forest = teo_2(g, k-1)

  # Enquanto ainda houverem componentes conexos
  # que não satisfazem a condição
  while True:
    # Atualiza a lista de componentes, pois pode ter
    # mudado durante a adição
    cc = _transform_cc(connected_components(forest))
    
    # Seleciona um que tenha comprimento < k
    selected_component = None
    for component in cc:
      if len(component) < k:
        selected_component = component
        break

    # Se não conseguiu selecionar, significa que todos
    # satisfazem comprimento >= k, e podemos parar o while
    if selected_component == None:
      break

    # Caso haja um selecionado, selecionar a aresta de menor
    # peso que tenha somente um dos vértices em selected_component
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
  g = graph()
  n = 20

  for i in range(1, n):
    g.add_node(i)
  for i in range(1, n):
    for j in range(i, n):
      g.add_edge((i, j), wt=randrange(1000))

  f = teo_2(g, 3)

  print "Edges"
  print [(e[0], e[1], g.edge_weight(e)) for e in g.edges()]
  print
  print "Forest"
  print [(e[0], e[1], g.edge_weight(e)) for e in f.edges()] 
  print "connected_components"
  print _transform_cc(connected_components(f))
