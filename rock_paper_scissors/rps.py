#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  if n == 0: return [[]]
  
  def another_round(n, result):
    if n == 0: return result
    newResult = []
    for i in range(len(result)):
      newResult.append([*result[i], 'rock'])
      newResult.append([*result[i], 'paper'])
      newResult.append([*result[i], 'scissors'])
    return another_round(n-1, newResult)



  return another_round(n-1, [['rock'], ['paper'], ['scissors']])


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')