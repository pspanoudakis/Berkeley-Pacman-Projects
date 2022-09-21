### Pavlos Spanoudakis (sdi1800184)
### Project 0 on Artificial Intelligence course
## Documentation and comments on Pacman Project 0 solution & `priorityQueue.py`
***

## Task & Execution
There were 2 tasks for this introductory project:
- [Pacman Project 0](https://inst.eecs.berkeley.edu/~cs188/sp20/project0/)
- Implementation of a Priority Queue with an underlying min-Heap, using the `heapq` module.

To execute the test routine for `PriorityQueue` in `priorityQueue/priorityQueue.py`, run

    python{3.6} priorityQueue/priorityQueue.py

To execute the **autograder** for Pacman Project 0, run

    python3.6 ./autograder.py

## General Information on `PriorityQueue` class

This class implements a Priority Queue, which uses a min-Heap for maintaining
the right element order. The min-Heap is implemented using a typical Python `list`
and the `heapq` module, which "treats" a list as a Heap. `heapq.heappush` (instead
of `list.append`), `heapq.pop` (instead of `list.pop`) and `heapq.heapify` (to maintain the
heap) are used from this module.

## Helpful class methods

- We can easily check if a `PriorityQueue` is empty using `isEmpty()`. This method just
checks whether the number of elements in the queue is 0. `count` attribute is used to
keep track of that.
- `__contains__(element)` method is also implemented, allowing us
to write expressions like `if element in <PriorityQueue>:...` to check if the queue
contains element.

## Pushing elements in the Queue

Elements can be pushed in the queue using `push(item, priority)`, where
`item` is the element to be pushed, and `priority` determines the priority of the item in the queue.
The smaller the priority, the earlier the item can be popped from the queue.

`push` checks if the item already exists in the queue. In that case, nothing is inserted or modified
and `False` is returned. Otherwise, the item is inserted in the heap using `heapq.heappush`
and `True` is returned.

An important point is that both the item value and the priority
of it need to be stored. Tuples can be used to achieve that: a `(priority, item)`
`tuple` is pushed in the heap list every time. `priority` is the first element in the tuple,
because this is the main criteria we want the comparisons of the queue items to be
based on: Python compares two tuples x, y by comparing their corresponding elements.
If `x[0] > y[0]` then it is decided that x is greater (if they are equal, x[1] and y[1]
are compared etc.). Tuples are actually suggested in the `heapq` documentation, when
priority values have to be assigned alongside items.

### Time Complexity

When `push` is called, it tests whether the queue already contains `item`, which costs
O(n). If the item is eventually pushed, pushing in the heap costs O(logn). So push has
a time complexity of O(n).

## Allowing duplicates to be pushed
If we want to push a possibly duplicate item in the queue, we can use `pushAllowDuplicates`.
At does exactly what `push` does, but without checking if the specified item already exists.
It has O(logn) time complexity.

## Popping elements from the Queue

`pop()` simply checks if the queue `isEmpty()` and, if not, pops the item
with the smallest priority value using `heapq.heappop` and returns it.
If the queue is already empty, `pop()` returns `None` to indicate it.
Testing if the queue is empty costs O(1) and popping from the heap costs O(logn),
resulting to a time complexity of O(logn).

## Updating Queue elements

The priority of an element in the queue can be updated by calling
`update(existing_item, new_priority)`. If the item does exist in the queue and the
specified priority is smaller than the one stored, then the latter is updated. That
means that the tuple stored for this item must be modified. Tuples are immutable, so
the tuple is replaced by a new one: `(new_priority, existing_item)`. This is the
reason why the loop used cannot be `for i in self.heap`. It would not allow us to
modify what `self.heap` nodes refer to. So it is more suitable to use a simple index `i`,
to modify `self.heap` nodes: `self.heap[i] = <new_tuple>`. After the modification,
`heapq.heapify` is called to maintain the heap order.
If the item was not found in the queue, it is inserted with the specified priority. Someone
could just call `push` to do that, but remember: `push` will check again if the given
item is already in the queue, which would be a waste of time. So update just calls
`heapq.heappush` and increases count directly.

### Time Complexity
Whether the item given exists or not, `update` will try to find it in the queue. That will
cost O(n). If it is modified, `heapq.heapify`, which also costs O(n) is called. If the item
was not found, it is pushed, which will cost O(logn). So `update` has a time complexity
of O(n) in all occasions.

## `PQSort`

`PQSort` takes advantage of `PriorityQueue` to sort an iterable of numbers. The given
argument can be any iterable (`list`, `tuple`, `dict` or a user-defined iterable). The
function checks if this is the case, and returns an empty `list` if it is not. If the check was
successful, the argument is iterated and its elements are pushed in a `PriorityQueue`.
Since the items are simply numbers, their value is also their priority as well. Finally,
they are popped from it and inserted in a list which is returned. We know that every
time we call `pop`, the item with the smallest priority will be returned, which in our
case, will be the smallest number. So by just popping from the queue and appending
the returned item to the list, we will have our numbers sorted in increasing order.

### Time Complexity

Checking if the argument is an iterable costs O(1).
Each element is pushed using `pushAllowDuplicates`, which costs O(logn) for n items.
Finally, popping from the queue will cost O(logn) n times. So the time complexity of
`PQSort` is O(nlogn).

## Development & Testing

Developed and tested in Windows 10 and WSL Ubuntu 20.04, using Visual Studio
Code, running a Python 3.6.12 interpreter. It has been tested in DIT Lab Ubuntu
16.04 environment, using Python 3.6.12 as well.
`PriorityQueue` is also compatible with Python 3.8.2 (and later versions).