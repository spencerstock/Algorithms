#!/usr/bin/python

import argparse

def find_max_profit(prices):
  max_profit = None
  for i in range(len(prices)): #If we tracked min_price_so_far we could get rid of a for loop and replace with an if statement
    for j in range(i+1,len(prices)):
      if (max_profit == None or prices[j]-prices[i] > max_profit):
        max_profit = prices[j]-prices[i]
      
  return max_profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))