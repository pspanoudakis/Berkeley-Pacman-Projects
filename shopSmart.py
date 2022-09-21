# shopSmart.py
# ------------
# Revision: Pavlos Spanoudakis (sdi1800184)
#------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

from __future__ import print_function
import shop


def shopSmart(orderList, fruitShops):
    """
    Returns the shop from `fruitShops` where the specified order costs less.

    `orderList`: List of (fruit, numPound) tuples

    `fruitShops`: List of FruitShops
    """
    try:
        # Select the first shop as the default cheapest option
        bestChoice = fruitShops[0]
    except IndexError:
        # The shops list is empty
        return None

    # Find the cost of the order in the first shop
    minCost = sum( [ fruitShops[0].getCostPerPound(item[0])*item[1] for item in orderList ] )
    for itr in fruitShops[1:]:
        currCost = sum( [ itr.getCostPerPound(item[0])*item[1] for item in orderList ] )
        if currCost < minCost:
            # If another shop is cheaper, select it as the best option.
            bestChoice = itr
            minCost = currCost   

    return bestChoice


if __name__ == '__main__':
    """ Main Method. Runs when the script is invoked from the command line. """
    orders = [('apples', 1.0), ('oranges', 3.0)]
    dir1 = {'apples': 2.0, 'oranges': 1.0}
    shop1 = shop.FruitShop('shop1', dir1)
    dir2 = {'apples': 1.0, 'oranges': 5.0}
    shop2 = shop.FruitShop('shop2', dir2)
    shops = [shop1, shop2]
    
    print("For orders ", orders, ", the best shop is", shopSmart(orders, shops).getName())
    orders = [('apples', 3.0)]
    print("For orders: ", orders, ", the best shop is", shopSmart(orders, shops).getName())

    shops.clear()
    # We should check: if `shops` is empty, shopSmart returns `None`, so invoking getName() will raise an AttributeError:
    try:
        print("For orders: ", orders, ", the best shop is", shopSmart(orders, shops).getName())
    except AttributeError:
        print("For orders ", orders, ", the best shop is None.")
