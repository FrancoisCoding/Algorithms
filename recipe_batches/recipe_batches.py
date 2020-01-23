#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):

    track = {}

    # Items function returns k,v pairs of dictionary in a list of tuples
    for k, v in ingredients.items():
        track[k] = 0
        while v >= recipe[k]:
            track[k] += 1
            v -= recipe[k]

    # Values function returns values of dictionary
    return 0 if len(ingredients) < len(recipe) else min(track.values())


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
