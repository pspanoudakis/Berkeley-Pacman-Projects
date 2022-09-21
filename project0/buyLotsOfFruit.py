# buyLotsOfFruit.py
# -----------------
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


# The fruit prices to be used by buyLotsOfFruit
fruitPrices = {'apples': 2.00, 'oranges': 1.50, 'pears': 1.75,
               'limes': 0.75, 'strawberries': 1.00}


def buyLotsOfFruit(orderList):
    """
    Returns the cost of the specified order.

    `orderList`: List of (fruit, numPounds) tuples
    """
    totalCost = 0.0

    for itr in orderList:
        if itr[0] not in fruitPrices:
            print("Error: Uknown fruit detected.")
            return None
        totalCost = totalCost + fruitPrices[ itr[0] ]* itr[1]       # Increase by cost-per-pound*pounds
    return totalCost


if __name__ == '__main__':
    """ Main Method. Runs when the script is invoked from the command line. """
    orderList = [('apples', 2.0), ('pears', 3.0), ('limes', 4.0)]
    # orderList.append(('avocado', 1.0))                        # If this is commented-out, buyLotsOfFruit will detect an error.
    print('Cost of', orderList, 'is', buyLotsOfFruit(orderList))