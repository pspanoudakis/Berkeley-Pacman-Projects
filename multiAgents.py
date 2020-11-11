# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util


from game import Agent

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        currentFood = currentGameState.getFood()
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        ghostPositions = successorGameState.getGhostPositions()
        for p in ghostPositions:
            # If a ghost is at the new position or next to it
            if p == newPos or util.manhattanDistance(p, newPos) == 1:
                # Don't go there
                return(float('-inf'))
            # If there is food in the new position
            elif currentFood[newPos[0]][newPos[1]]:
                # There is no ghost there or next to it,
                # so go there and eat the dot
                return float('inf')
        
        # Pacman is not in immediate danger in the new position, but there is no food there
        # Now estimating the nearest food dot:
        minDist = float('inf')
        food = currentFood.asList()
        for f in food:
            dist = util.manhattanDistance(f, newPos)
            if dist < minDist:
                minDist = dist
        
        # We return -minDist, because the higher value is better,
        # and a state near a food dot is more preferable.
        return -minDist

def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        actions = gameState.getLegalActions(0)
        maxResult = float('-inf')
        for a in actions:
            successor = gameState.generateSuccessor(0,a)
            currentResult = self.minValue(successor, 0, 1)
            if currentResult > maxResult:
                maxResult = currentResult
                maxAction = a
        return maxAction        

    def minValue(self, gameState, currDepth, currAgent):
        if gameState.isWin() or gameState.isLose() or currDepth == self.depth:
            return self.evaluationFunction(gameState)
        actions = gameState.getLegalActions(currAgent)
        successors = []
        for a in actions:
            successors.append( gameState.generateSuccessor(currAgent, a) )
        agents = gameState.getNumAgents()
        if currAgent < agents - 1:
            return min( [self.minValue(s, currDepth, currAgent + 1) for s in successors] )
        else:
            return min( [self.maxValue(s, currDepth + 1) for s in successors] )
    
    def maxValue(self, gameState, currDepth):
        if gameState.isWin() or gameState.isLose() or currDepth == self.depth:
            return self.evaluationFunction(gameState)
        actions = gameState.getLegalActions(0)
        successors = []
        for a in actions:
            successors.append( gameState.generateSuccessor(0, a) )
        return max( [self.minValue(s, currDepth, 1) for s in successors] )

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        actions = gameState.getLegalActions(0)
        maxResult = float('-inf')
        a = float('-inf')
        b = float('inf')
        for action in actions:
            successor = gameState.generateSuccessor(0, action)
            currentResult = self.minValue( successor, 0, 1, a, b )
            if currentResult > maxResult:
                maxResult = currentResult
                maxAction = action
                a = max( (a, currentResult) )
        return maxAction

    def maxValue(self, gameState, currDepth, a, b):
        if gameState.isWin() or gameState.isLose() or currDepth == self.depth:
            return self.evaluationFunction(gameState)
        actions = gameState.getLegalActions(0)
        maxValue = float('-inf')
        for action in actions:
            successor = gameState.generateSuccessor(0, action)
            maxValue = max( (maxValue, self.minValue(successor, currDepth, 1, a, b)) )
            if maxValue > b:
                return maxValue
            a = max( (a,maxValue) )
        return maxValue

    def minValue(self, gameState, currDepth, currAgent, a, b):
        if gameState.isWin() or gameState.isLose() or currDepth == self.depth:
            return self.evaluationFunction(gameState)
        actions = gameState.getLegalActions(currAgent)
        minValue = float('inf')
        agents = gameState.getNumAgents()
        for action in actions:
            successor = gameState.generateSuccessor(currAgent, action)
            if currAgent < agents - 1:
                minValue = min( (minValue, self.minValue(successor, currDepth, currAgent + 1, a, b)) )
            else:
                minValue = min( (minValue, self.maxValue(successor, currDepth + 1, a, b)) )
            if minValue < a:
                return minValue
            b = min( (b,minValue) )
        return minValue

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        actions = gameState.getLegalActions(0)
        maxAction = 'Stop'
        maxResult = float('-inf')
        for a in actions:
            successor = gameState.generateSuccessor(0,a)
            currentResult = self.chanceExpect(successor, 0, 1)
            if currentResult > maxResult:
                maxResult = currentResult
                maxAction = a
        return maxAction
    
    def maxExpect(self, gameState, currDepth):
        if gameState.isWin() or gameState.isLose() or currDepth == self.depth:
            return self.evaluationFunction(gameState)
        actions = gameState.getLegalActions(0)
        successors = []
        for a in actions:
            successors.append( gameState.generateSuccessor(0, a) )
        return max( [self.chanceExpect(s, currDepth, 1) for s in successors] )

    def chanceExpect(self, gameState, currDepth, currAgent):
        if gameState.isWin() or gameState.isLose() or currDepth == self.depth:
            return self.evaluationFunction(gameState)
        actions = gameState.getLegalActions(currAgent)
        successors = []
        for a in actions:
            successors.append( gameState.generateSuccessor(currAgent, a) )
        if currAgent < gameState.getNumAgents() - 1:
            return sum( [self.chanceExpect(s, currDepth, currAgent + 1 ) for s in successors ] )/len(successors)
        else:
            return sum( [self.maxExpect(s, currDepth + 1 ) for s in successors ] )/len(successors)

def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    winBonus    =  999999999999
    foodPenalty   =  -500
    scaredPenalty = -1000
    losePenalty = -999999999999
    # Useful info
    foodGrid = currentGameState.getFood()
    food = foodGrid.asList()
    #currentPosition = currentGameState.getPacmanPosition()
    #currentFood = currentGameState.getFood()
    #currentGhostStates = currentGameState.getGhostStates()
    #ghostPositions = currentGameState.getGhostPositions()
    score = currentGameState.getScore() * 1000
    evalValue = 0
    if currentGameState.isLose():
        evalValue += losePenalty
    elif currentGameState.isWin():
        evalValue += winBonus   

    scaredLeft = 0
    foodLeft = 0
    position = currentGameState.getPacmanPosition()
    ghostPositions = currentGameState.getGhostPositions()
    leftTimeScared = [ghostState.scaredTimer for ghostState in currentGameState.getGhostStates()]
    for p in range(len(ghostPositions)):
        if leftTimeScared[p] > 0:
            # treat it as food
            scaredLeft += 1
            evalValue += scaredPenalty
        if util.manhattanDistance(ghostPositions[p], position) == 1:
            # Don't go there
            evalValue += losePenalty

    return evalValue + score

# Abbreviation
better = betterEvaluationFunction
