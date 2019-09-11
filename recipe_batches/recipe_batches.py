#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  max_batches = 1 #start at 1 since we encounter the return max_batches-1 before the max_batches+1
  while True:

    for key in recipe.keys():
      if(key in ingredients): #makes sure we have all ingredients required
        ingredients[key] -= recipe.get(key)
        if (ingredients[key] < 0):
          return max_batches-1 #-1 because we're already <0 (aka: negative) so we should make 1 less than what we're at.
      else: return 0 #ingredient needed for recipe not found.
    max_batches += 1

   



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))