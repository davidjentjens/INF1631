import teo1
import teo2
import tsp_reader
import networkx as nx
import matplotlib.pyplot as plt
import sys

theorem = int(sys.argv[1])
filename = sys.argv[2]
city = filename.split('/')[-1].split('.')[0]

fn = None
if theorem == 1:
  fn = teo1.teo_1
else:
  fn = teo2.teo_2

g = tsp_reader.read(open(filename).read())

for k in range(1, len(g.nodes())+1):
  f = fn(g, k)

  n = nx.Graph()

  print k
  for edge in f.edges():
    print "%d %d %d" % (edge[0], edge[1], g.edge_weight(edge))
  print

  for node in f.nodes():
    n.add_node(node)

  for edge in f.edges():
    n.add_edge(edge[0], edge[1])
  nx.draw(n)
  plt.savefig('figs/teo%d/%s-k%d.png' % (theorem, city, k))
  plt.clf()