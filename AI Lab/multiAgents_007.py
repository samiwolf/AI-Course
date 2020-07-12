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
import sys
from game import Agent

BIG = sys.maxint
class ReflexAgent(Agent):
    """
      A reflex agent chooses an move at each choice point by examining
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
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, move) for move in legalMoves]
        bestScore = max(scores)
        indexes = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(indexes) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, move):
        successorGameState = currentGameState.generatePacmanSuccessor(move)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        total_food = currentGameState.getFood().count()
        ln = len(newFood.asList())
        dist = calculate_distance(ln, total_food, newFood, newPos)
        for ghost in newGhostStates:
            plus = calculate(ghost, newPos)
            dist += plus
        return -dist

def calculate(ghost, newPos):
    md = manhattanDistance(ghost.getPosition(), newPos)
    poww = 2 - md
    plus = 4 ** poww
    return plus	

def calculate_distance(ln, total_food, newFood, newPos):
    dist = 20000
    if ln == total_food:
        for x in newFood.asList():
            d = manhattanDistance(x,newPos)
            if d < dist:
                dist = d
    else:
        dist = 0
    return dist	

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
        
def getResultStates(legalMoves, gameState):
    l = []
    for move in legalMoves:
        x = gameState.generateSuccessor(0,move)
        l.append(x)
    return l

def getResultStates2(legalMoves, gameState, ghostIndex):
    l = []
    for move in legalMoves:
        x = gameState.generateSuccessor(ghostIndex, move) 
        l.append(x)
    return l
    
        
class MinimaxAgent(MultiAgentSearchAgent):
    def getAction(self, gameState):
    	
    	legalMoves=gameState.getLegalActions(0)
        
        resultStates= getResultStates(legalMoves, gameState)
        
        scores=[]
        for state in resultStates:
			scores.append(self.minimizer(0,state,1))
    	bestScore = max(scores)
    	
    	indexes = []
    	for index in range(len(scores)):
            if scores[index]==bestScore:
                indexes.append(index)
    	
    	return legalMoves[random.choice(indexes)]
    	
    	
    def maximizer(self,currentDepth,gameState):
    	
    	if(self.depth==currentDepth or gameState.isLose() or gameState.isWin()):
    		return self.evaluationFunction(gameState)
        legalMoves=gameState.getLegalActions(0)
        resultStates= getResultStates(legalMoves, gameState)
        scores=[]
        for state in resultStates:
            x = self.minimizer(currentDepth,state,1)
            scores.append(x)
    	return max(scores)
    	
    def minimizer(self,currentDepth,gameState,ghostIndex):
    	
    	if(self.depth==currentDepth or gameState.isLose() or gameState.isWin()):
    		return self.evaluationFunction(gameState)    	
    		
    	legalMoves=gameState.getLegalActions(ghostIndex)
    	resultStates=getResultStates2(legalMoves, gameState, ghostIndex)
        if (ghostIndex>=gameState.getNumAgents()-1):
            scores=[]
            for state in resultStates:
                x = self.maximizer(currentDepth+1,state)
                scores.append(x) 
    	else:
            scores=[]
            for state in resultStates:
                x = self.minimizer(currentDepth,state, ghostIndex+1)
                scores.append(x)
    	return min(scores)
    
class AlphaBetaAgent(MultiAgentSearchAgent):

    def getAction(self, gameState):
        max_value, act = self.minimax(gameState, self.index, 0, -BIG, BIG)
        return act

    def minimax(self, state, agent, depth, alpha, beta):
        total_agent = state.getNumAgents()
        x = agent % total_agent
        if (x == 0) and (depth == self.depth):
            return self.evaluationFunction(state), None
        if x == 0:
            return self.maxi(state, x, depth, alpha, beta)
        return self.mini(state, x, depth, alpha, beta)

    def mini(self, state, agent, depth, alpha, beta):
        legalMoves = state.getLegalActions(agent)
        minn = BIG
        minn_action = None
        if len(legalMoves) == 0:
            return self.evaluationFunction(state), None

        for move in legalMoves:
            successor_state = state.generateSuccessor(agent, move)
            ans, act = self.minimax(successor_state, agent + 1, depth, alpha, beta)
            if ans < minn:
                minn_action = move
                minn = ans
            if minn < alpha:
                return minn, minn_action
            beta = min(beta, minn)

        return minn, minn_action

    def maxi(self, state, agent, depth, alpha, beta):
        legalMoves = state.getLegalActions(agent)
        maxx = -BIG
        maxx_action = None

        if len(legalMoves) == 0:
            return self.evaluationFunction(state), None

        for move in legalMoves:
            successor_state = state.generateSuccessor(agent, move)
            ans, act = self.minimax(successor_state, agent + 1, depth + 1, alpha, beta)
            if ans > maxx:
                maxx_action = move
                maxx = ans
            if maxx > beta:
                return maxx, maxx_action
            alpha = max(alpha, maxx)

        return maxx, maxx_action

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax move using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction


			
			
