# -*- coding: utf-8 -*-
"""Project 1: MED with Alignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1r_dJDOuiy1hZMOttqrs_E6bPbehvQguz
"""

def minEdit(seq1, seq2, substitution_cost=2):
  size_x = len(seq1) + 1
  size_y = len(seq2) + 1
  matrix = np.zeros((size_x, size_y), dtype=int)
  for x in range(size_x):
    matrix [x, 0] = x
  for y in range(size_y):
    matrix [0, y] = y
    
  for x in range(1, size_x):
    for y in range(1, size_y):
      if seq1[x-1] == seq2[y-1]:
        d = 0
      else:
        d = substitution_cost
      matrix[x,y] = min(
        matrix[x-1,y] + 1,
        matrix[x-1,y-1] + d,
        matrix[x,y-1] + 1
      )

  print (matrix)
  a = alignment(seq1, seq2, matrix)
  print("\nPath:",a)
  return (matrix[size_x - 1, size_y - 1])

def alignment(word1, word2, array):

    new_w1 = []
    new_w2 = []
    w1 = [char for char in word1]
    w2 = [char for char in word2]
    row = len(w1)
    col = len(w2)
    trace = [[row, col]]

    while True:
        if w1[row - 1] == w2[col - 1]:
            cost = 0
        else:
            cost = 2

        a = array[row - 1][col]
        b = array[row - 1][col - 1]
        c = array[row][col - 1]
        d = array[row][col]
        if d == b + cost:
            trace.append([row - 1, col - 1])
            new_w1 = [w1[row - 1]] + new_w1
            new_w2 = [w2[col - 1]] + new_w2
            row, col = row - 1, col - 1
        else:
            if d == a + 1:
                trace.append([row - 1, col])
                new_w1 = [w1[row - 1]] + new_w1
                new_w2 = ["-"] + new_w2
                row, col = row - 1, col
            elif d == c + 1:
                trace.append([row, col - 1])
                new_w1 = ["-"] + new_w1
                new_w2 = [w2[col - 1]] + new_w2
                row, col = row, col - 1

        if col == 0 and row == 0:
            print("\nAlignment:")
            print("",new_w1,"\n",new_w2)
            return trace

import numpy as np
import time

s1 = "intention"
s2 = "execution"
print("Word 1:","'",s1,"'","|Word 2:","'",s2,"'")
print("\nMatrix of distances:")
start = time.time()
d = minEdit(s1, s2, substitution_cost=2)
end = time.time()
print("\nMinimum edit distance cost:", d)
print("\nTime: %.4f" %(end - start))

