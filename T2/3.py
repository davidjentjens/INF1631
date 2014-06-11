# -*- coding: utf-8 -*-

def teo_3(i, j, costs, rewards, q):
  pass

if __name__ == '__main__':
  with open('walk.in') as f:
    q = f.readline().strip()
    while q != '0':
      costs   = [map(int, f.readline().strip().split(' ')) for i in range(8)]
      rewards = [map(int, f.readline().strip().split(' ')) for i in range(8)]

      teo_3(0, 0, costs, rewards, q)

      q = f.readline().strip()
