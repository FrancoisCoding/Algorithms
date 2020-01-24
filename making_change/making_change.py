#!/usr/bin/python

import sys


cache = []


def making_change(amount, denominations):
    if amount == 0:
        return 1
    if amount < 0:
        return 0
    cache = [0] * (amount + 1)
    cache[0] = 1
    for coin in denominations:
        for higher_amount in range(coin, amount + 1):
            previous_amount = higher_amount - coin
            new_amount = cache[previous_amount]
            if not previous_amount and (higher_amount+1) % 5 == 0 and coin is not 1:
                new_amount = new_amount + 1
            cache[higher_amount] += new_amount
        print(cache)
    return cache[amount]


if __name__ == "__main__":
        # Test our your implementation from the command line
        # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
