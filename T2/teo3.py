# -*- coding: utf-8 -*-

class Path:
  def __init__(self, list, costs, rewards):
    self.pos_list = list
    self.cost = get_for_list(costs, list)
    self.prize = get_for_list(rewards, list)

  def __repr__(self):
    return self.pos_list.__repr__()[:-1] + ", C=%d, P=%d]\n" % (self.cost, self.prize)

  def last(self):
    return self.pos_list[-1]

  def append_new(self, final, costs, rewards):
    new_list = self.pos_list[:]
    new_list.append(final)
    return Path(new_list, costs, rewards)

def find_neighbors(pos):
  naive = [(pos[0]-1, pos[1]-1), (pos[0]-1, pos[1]), (pos[0]-1, pos[1]+1),
          (pos[0],   pos[1]-1),                     (pos[0],   pos[1]+1),
          (pos[0]+1, pos[1]-1), (pos[0]+1, pos[1]), (pos[0]+1, pos[1]+1)]
  return [n for n in naive if n[0]>=0 and n[1]>=0 and n[0]<8 and n[1]<8]

def get(matr, pos):
  return matr[pos[0]][pos[1]]

def get_for_list(matr, pos_list):
  return sum([get(matr, pos) for pos in pos_list[1:]])

def teo_3(pos, costs, rewards, q):
  paths = {}

  neighbors = find_neighbors(pos)
  paths[0] = [Path([pos, neighbor], costs, rewards) for neighbor in neighbors if get(costs, neighbor) <= q]

  k = 1
  paths[1] = []

  while len(paths[k-1]) != 0:
    for path in paths[k-1]:
      neighbors = find_neighbors(path.last())
      useless = False
      for neighbor in neighbors:
        if (path.cost + get(costs, neighbor)) <= q:
          useless = True
          new_path = path.append_new(neighbor, costs, rewards)
          paths[k].append(new_path)

      if useless:
        paths[k-1].remove(path)

    print "k = %d" %k 
    print paths[k]
    if k == 20:
      break

    k = k + 1
    paths[k] = []



if __name__ == '__main__':
  with open('walk.in') as f:
    q = f.readline().strip()
    while q != '0':
      costs   = [map(int, f.readline().strip().split(' ')) for i in range(8)]
      rewards = [map(int, f.readline().strip().split(' ')) for i in range(8)]

      teo_3((0, 0), costs, rewards, q)
      break
      q = f.readline().strip()
