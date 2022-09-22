### Pavlos Spanoudakis (sdi1800184)
## Project 1 on Artificial Intelligence class
## Notes & Documentation on Pacman Project 1
***

### Execution

To execute the **autograder** for [Pacman Project 1](https://inst.eecs.berkeley.edu/~cs188/sp20/project1/), run

    python3.6 ./autograder.py

You can also see a **GUI execution** for a particular agent & maze:

    python pacman.py -l mediumMaze -p SearchAgent

All possible alternatives are listed in the task page.

### Question 1 (Depth-First Search)

This is implemented in the `depthFirstSearch` function in `search.py`.

The function is based on the lecture algorithm, but with a slight modification:
A state node is checked for **goal state** when it is about to be **expanded**,
not when it is **produced** by the parent node, as described in the lecture,
since the `autograder.py` test would fail in that case.
As asked, the algorithm follows *graph-search*, chekcing whether each successor state
is already stored in the *frontier*.

### Question 2 (Breadth-First Search)

`breadthFirstSearch` function in `search.py` also follows the *graph-search* lecture code,
with the exception of the modification noted above.

### Question 3 (Uniform Cost Search)

Implemented in the `uniformCostSearch` function in `search.py`.

Here, things change when a successor state is already in the frontier:
In that case we find the cost of the new path, and if the stored path is more expensive,
we update it.

A tricky part is when we have such a case. A state is a tuple `(position, path)`.
A successor that is already in the gueue, is stored with a different path than the one found when expanding.
So just `update((state,new_path), new_cost)` will not work properly,
because the element will not be found in the `PriorityQueue`.
So we manually change it first by **reconstructing** the `PriorityQueue` node.
This requires internally handling the `PriorityQueue`, through `heap`,
which is not the most elegant solution, but it seemed to be the only choice.

### Question 4 (A-Star Search)

This is implemented in the `aStarSearch` function in `search.py`,
which is identical with `uniformCostSearch`, but this time the cost of each state
in the `PriorityQueue` contains the **heuristic** value for this state.
To make things simpler, we use an `evalFunction` to do that and get the total sum.

### Question 5 (Corners Problem)

The `cornersProblem` class methods `getStartState`, `isGoalState` and `getSuccessors`
are implemented as asked. Each state of the problem is a **tuple** `(position, visitedCorners)`,
where `visitedCorners` is also a **tuple** with 4 elements, one for each corresponding corner
of `self.corners`. An element is `True` if the corner has been visited, `False` otherwise.
In a *goal state*, all 4 elements have to be `True`.

### Question 6 (Corners Problem Heuristic)

The `cornersHeuristic` in `searchAgents.py` works as follows:
- Find the distance between the current position and all the unvisited corners,
using the information stored in the current state and the problem.
- Return the maximum of the distances found.

This heuristic is admissible, since all the corners will be visited in the end.
As a result, we will eventually follow a path from the current position
to the corner with the maximum distance, which will not be cheaper
than the Manhattan Distance calculated.

### Question 7 (Food Heuristic)

Implemented in `foodHeuristic` in `searchAgents.py`.

To estimate the potential cost between a state and a goal state, the heuristic works as follows:  
- First, find the **2 food dots** with the biggest *Manhattan Distance*.
If there is only one dot, 0 will be found, as expected.
- Second, calculate the distance between the current position and each of the 2 dots found.
Choose the **smaller**.
- Return the **sum** of those two.

The logic behind this is the following:
- The total solution path distance will definitely contain the maximum distance between two dots,
since we have to visit both of them.
- And it will also contain the minimum distance between the current position and one of them,
since we will eventually visit one of them first.

As a result, the heuristic will never overestimate the cost to the goal state.  
*"And what if only one food dot is left?"*  
In that case, 0 is found in the first step, and then we just calculate the distance between
the current position and the dot, which is an admissible result.

### Question 8 (Path to closest dot)

The `AnyFoodSearchProblem` class `isGoalState` method is implemented as hinted.
In this problem we just try to reach a food dot, so we check if there is a food dot
in the current position and return `True` or `False` accordingly.
To solve the *Closest Dot Problem*, the `findPathToClosestDot` function is implemented.
We simply need to use an appropriate search function. In this case it is `breadthFirstSearch`,
since it finds the "narrowest" possible solution, which in our case is the closest
from the starting position (since all edges/actions have the same cost in the Pacman Maze).

***
Developed and extensively tested in Windows 10 (Python 3.6.8) and WSL Ubuntu 20.04 (Python 3.6.12),  
using Visual Studio Code. Successfully tested in DIT Lab Ubuntu 16.04 (Python 3.6.12) as well.
