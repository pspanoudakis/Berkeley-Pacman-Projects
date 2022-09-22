# File: priorityQueue.py
# Author: Pavlos Spanoudakis (sdi1800184)
# Contents: PriorityQueue class and PQSort function implementations
# See 1115201800184_project0.pdf for more information.

import heapq


class PriorityQueue:
    """ Priority Queue implementation, using a min-Heap implemented with a list. """

    def __init__(self):
        self.count = 0
        self.heap = []
    
    def push(self, item, priority) -> bool:
        """ Adds the specified item in the queue, according to the specified priority. 
            In case such item already exists, no changes are made in the queue.
            Returns `True` if the item was added, `False` otherwise. """
        # Handling duplicate items:
        if item in self:
                # The item already exists, so it is not pushed in the queue.
                return False

        # There is no such item in the queue, so it must be inserted.
        # Python compares two tuples t1, t2 by comparing t1[0] and t2[0] first.
        # We want the comparisons to be made based on the priority of the items, so the first element of
        # each tuple should be the priority of the corresponding item.
        heapq.heappush(self.heap, (priority, item))
        self.count += 1
        return True

    def pushAllowDuplicates(self, item, priority):
        """
        Adds the specified item in the queue, according to the specified priority,
        without preventing duplicate items from being inserted.
        """
        heapq.heappush(self.heap, (priority, item))
        self.count += 1

    def pop(self):
        """ Removes the item with the smallest priority from the queue, and returns it. 
            In case the queue is empty, returns `None`. """
        if not self.isEmpty():
            self.count = self.count - 1
            return heapq.heappop(self.heap)[1]      # return the 2nd element of the list (the item)
        else:
            return None

    def isEmpty(self) -> bool:
        """ Returns `True` if queue is empty, `False` otherwise."""
        return self.count == 0

    def update(self, item, priority) -> None:
        """ Modifies the priority (and if needed, the position) of the specified item in the queue.
            The existing priority will be modified only if it is greater than the one specified.
            In case there is no such item in the queue, it is inserted."""
        
        # First, we have to check if the item is already in the queue, and modify its priority, if needed.
        # `for i in self.heap` is not used, because it would give us direct access to the elements
        # of the heap, which are immutable (since they are tuples). So we have to change each *node*
        # of the heap so that it refers to a *new* tuple with the updated priority.

        for i in range(0, self.count):          # we can use `self.count` as the max value of the index
            # heap[i] is a tuple. heap[i][0] is the item priority, and heap[i][1] is the item value.
            if item == (self.heap[i])[1]:
                if (self.heap[i])[0] > priority:
                    # priority must be modified at this point
                    # tuples are immutable, so we make a new tuple with the desired values
                    self.heap[i] = (priority, item)
                    heapq.heapify(self.heap)
                return        
        # If this point is reached, there is no such item in the queue.
        # We could invoke `self.push(item, priority)` here, but `self.push` will check if the
        # item is a duplicate, which would be a waste of time, since we know it is not.
        # So we push it in the queue directly.
        heapq.heappush(self.heap, (priority, item))
        self.count += 1

    def __contains__(self, item):
        """ Will be invoked in an `if <value> in PriorityQueue` situation. """
        for t in self.heap:
            if item in t:
                return True
        return False


def PQSort(elements) -> list:
    """ Returns a sorted list (in increasing order) of the elements in the specified iterable.
    In case the argument is not iterable, returns an empty list. """
    try:
        iter(elements)          # Making sure the argument is an iterable
    except TypeError:
        return []
    
    # Inseting elements in the queue
    pq = PriorityQueue()
    for e in elements:
        pq.pushAllowDuplicates(e, e)    # the value of each element is also the priority of it in the queue

    # Creating the list that will be returned
    sorted = []
    while not pq.isEmpty():
        sorted.append(pq.pop())     # elements are popped in increasing priority and as a result, in increasing value.    
    return sorted


if __name__ == '__main__':
    """ Main Method. Runs when the script is invoked from the command line. """
    x = PriorityQueue()
    x.push('Hello', 3)
    x.push('Hello', 3)
    x.push('World', 2)
    x.update('Hello', 0)
    x.push('New', 1)
    x.pop()
    x.isEmpty()
    if 'New' in x:
        print("OK")
    if'Old' in x:
        print("NOT OK")
    l = [4,2,3,1,6,10,6,9]
    new = PQSort(l)
    pass