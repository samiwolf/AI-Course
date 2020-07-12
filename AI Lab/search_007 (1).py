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


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def is_visited(x, visitedStates):
	return x in visitedStates

def aStarSearch(problem, heuristic=nullHeuristic):
    visitedStates= []
    pq = None
    startState = None
    startState = problem.getStartState()
    pq = util.PriorityQueue()
    zero = 0
    pq.push((startState,[],zero),zero)    
    
    while pq.isEmpty() == False:
        aa = pq.pop()
        x = aa[0]
        y = aa[1]
        z = aa[2]
        if problem.isGoalState(x):
            return y
          
        if not x in visitedStates:
            for child in problem.getSuccessors(x):
		c0 = child[0]
		c1 = child[1]
		c2 = child[2]
                if not is_visited(c0, visitedStates):
			temp = y + [c1]
			temp2 = z + c2
                    	next_node = (c0, temp, temp2)
                    	pq.push(next_node, z + c2 + heuristic(c0,problem))
            visitedStates.append(x)

    return []


def bestFirstSearch(problem, heuristic=nullHeuristic):
	
	pq=util.PriorityQueue()
	startState= None
	startState = problem.getStartState()
	pq.push(startState,heuristic(startState,problem))
	visitedStates = []
	parent = {}
	path = []
	parent[startState] = -56
	
	while not pq.isEmpty():
		aa=pq.pop()
		visitedStates.append(aa)
		
		if problem.isGoalState(aa):
			getPath(aa,parent, path)
			break
			
		for child in problem.getSuccessors(aa):
			c0 = child[0]
			c1 = child[1]
			if c0 not in visitedStates:
				parent[c0] = (aa, c1)
				pq.push(c0,heuristic(c0,problem))				
	
	return path

def getPath(state,parent,path):
    if parent[state]==-56:
        return
    getPath(parent[state][0],parent,path)
    path.append(parent[state][1])

