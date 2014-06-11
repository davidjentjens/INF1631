import math
from pygraph.classes.graph import graph

class City:
  def __init__(self, line):
    self.id, self.x, self.y = line.split(' ')
    self.id = int(self.id)
    self.x = float(self.x)
    self.y = float(self.y)

  def dist(self, other):
    return int(round(0.5 + math.sqrt( (self.x-other.x)**2 + (self.y-other.y)**2 )))

def read(tsp_str):
  cities = [City(line) for line in tsp_str.split("\n")]

  g = graph()

  for c in cities:
    g.add_node(c.id)

  for i in range(len(cities)):
    for j in range(i+1, len(cities)):
      distance = cities[i].dist(cities[j])
      g.add_edge((cities[i].id, cities[j].id), wt=distance)

  return g
