# search.py
# ---------
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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
	stak = util.Stack()
	visitedStates = []
	actions = []
	startState = problem.getStartState()
	stak.push((actions,startState))

	while not stak.isEmpty():
		actions, state = stak.pop()
		if problem.isGoalState(state):
			return actions
		visitedStates.append(state)

		childrenStates = problem.getSuccessors(state)
		for child in childrenStates:
			nextState = child[0]
			nextDirection = child[1]
			if nextState not in visitedStates:
				stak.push( (actions+[nextDirection], nextState) )

def breadthFirstSearch(problem):
	q = util.Queue()
	visitedStates = []
	actions = []
	startState = problem.getStartState()
	q.push((actions,startState))

	while not q.isEmpty():
		actions, state = q.pop()
		visitedStates.append(state)
		if problem.isGoalState(state):
			return actions
		childrenStates = problem.getSuccessors(state)
		for child in childrenStates:
			nextState = child[0]
			nextDirection = child[1]
			if nextState not in visitedStates:
				q.push( (actions+[nextDirection], nextState) )

def uniformCostSearch(problem):
	pq = util.PriorityQueue()
	successors ={}
	visitedStates = []
	actions = []
	cost = 0
	startState = problem.getStartState()
	pq.push((actions,startState) , cost)

	while not pq.isEmpty():
		actions, state = pq.pop()
		visitedStates.append(state)
		if problem.isGoalState(state):
			return actions
		if state in successors:
			children = successors[state]
		else:
			children = problem.getSuccessors(state)
			successors[state] = children
		childrenStates = problem.getSuccessors(state)
		for child in childrenStates:
			nextState = child[0]
			nextDirection = child[1]
			if nextState not in visitedStates:
				pq.push( (actions+[nextDirection], nextState), problem.getCostOfActions(actions+[nextDirection]) )

def iterativeDeepeningSearch(problem):
    stak = util.Stack()
    searchLimit = 1

    while True:
		visitedStates = []
		actions = []
		depth = 0
		startState = problem.getStartState()
		stak.push((actions,startState,depth))
		(actions,state,depth) = stak.pop()
		visitedStates.append(state)

		while not problem.isGoalState(state):
			children = problem.getSuccessors(state)
			for child in children:
				nextState = child[0]
				nextDirection = child[1]
				if (nextState not in visitedStates) and (depth + 1 <= searchLimit):
					stak.push((actions + [nextDirection], nextState, depth + 1))
					visitedStates.append(nextState)
			if stak.isEmpty():
				break
			(actions, state, depth) = stak.pop()

		if problem.isGoalState(state):
			return actions
		searchLimit += 1


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
