### Pavlos Spanoudakis (sdi1800184)
## Project 2 on Artificial Intelligence class
## Notes & Documentation on Pacman Project 2
***

### Execution

To execute the **autograder** for [Pacman Project 2](https://inst.eecs.berkeley.edu/~cs188/sp20/project2/), run

    python3.6 ./autograder.py

You can also see a **GUI execution** using one of the possible alternatives in the task page.

### Question 1 (Reflex Agent)

`ReflexAgent`'s `evaluationFunction` takes into account:
- Whether a ghost is at the new position or next to it (because if there is ghost next to it,
it could possibly move there in its next turn). In that case, the function returns −∞
to prevent the pacman from getting there (the greater the return value,
the better the new state is considered to be)
- Whether there is food currently at the new position.
In that case, +∞ is returned to make the pacman get there (in a greedy criteria)
- The distance from the nearest fod dot. In case none of the above senarios is true,
the function finds the distance between the new position and the nearest dot,
`minDist` and returns **`-minDist`** (so that the smaller distance is considered better)

### Question 2 (Minimax)

Implemented using `MinimaxAgent` methods `getAction`, `minValue` and `maxValue`.
They all follow the lecture algorithms.

`minValue` takes the current depth and the current agent index as aditional arguments.
If `minValue` makes another `minValue` call, it increases the agent index
(so that the next ghost plays next). If a `maxValue` call is made,
`minValue` increases the depth (the depth should be increased every time
MAX plays in order to pass the `autograder`).

`maxValue` takes the current depth as aditional argument.
There is no need for the agent index, since MAX (pacman) knows the first ghost
(with index = 1) will play next.

`getAction` calls `minValue` with depth = 0 and index = 1 (the first ghost plays next)
and returns the action that led to the biggest result.

### Question 3 (Alpha-Beta Pruning)

Implemented using `AlphaBetaAgent` methods `getAction`, `minValue` and `maxValue`.
They all follow the lecture algorithms, but without pruning in equality,
as asked [here](https://inst.eecs.berkeley.edu/~cs188/sp20/project2/#question-3-5-points-alpha-beta-pruning).

`getAction`, `maxValue` and `minValue` work exactly like in Question 2,
with the addition of `a` and `b` as arguments.

### Question 4 (Expectimax)

Implemented using `ExpectimaxAgent` methods `getAction`, `maxExpect` and `chanceExpect`.

`chanceExpect` works like `minValue` in terms of the given arguments (depth, agent index).
Each ghost chooses its moves randomly, so `chanceExpect` returns
the average value returned by the succesor states.

### Question 5 (Better Evaluation Function)

`betterEvaluationFunction` takes into account:
- Whether currentGameState is a losing or winning state
(returns a really small or really big number respectively)
- Whether a non-scared ghost is next to this position or not
(treats the state as a losing state)
- The total distance between this position and all the food dots.
The function finds the total distance of all the dots from the current state,
multiplies it with a penalty and adds the result to the returned value.
- The total distance between this position and all the capsules.
The function finds the total distance of all the capsules from the current state,
multiplies it with a penalty and adds the result to the returned value.
- The total distance between this position and all the scared ghosts.
A penalty is also given for the distance from the scared ghosts,
since they should be treated as food by the pacman.
- The game score.

The returned value is a linear combination af all the above.

The greater the distances from food dots, capsules and ghosts,
the least will be the returned value.  

The logic behind this is that pacman should be trying to eat them
(in a greedy but not out-of control way) because if the pacman is not moving or
is not eating anything, the score is decreased and that should be prevented.

The penalties and bonuses are defined at the beggining and can easily be modified.
Their values have occured experimentally.

### Development & Testing
Developed in WSL Ubuntu 20.04, using Visual Studio Code, running a Python 3.6.12 interpreter.
Succesfully passes the autograder in DIT Lab Ubuntu 16.04, running Python 3.6.12 interpreter as well.
