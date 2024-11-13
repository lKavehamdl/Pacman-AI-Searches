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
from game import Directions
from typing import List

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

    """
    there are two type of searchs:
    1-with cost search
    2-without cost search
    for both of searchs we have a fringe so we can store next states we want to explore
    """



def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    return NoCostSearch(problem, frontier=util.Stack())

def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    return NoCostSearch(problem, frontier=util.Queue())

def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    return searchWithCost(problem)

def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def searchWithCost(problem, heureistic=nullHeuristic):
    frontier= util.PriorityQueue()
    closed_set= list()
    s= (problem.getStartState(), [])
    frontier.push(s, 0)
    while not frontier.isEmpty():
        curr= frontier.pop()
        if problem.isGoalState(curr[0]):
            return curr[1]
        if curr[0] not in closed_set:
            closed_set.append(curr[0])
            curr_child= problem.getSuccessors(curr[0])
            for state in curr_child:
                if state[0] not in closed_set:
                    path= curr[1] + [state[1]]
                    if heureistic == nullHeuristic:
                        frontier.push((state[0], curr[1]+ [state[1]]), problem.getCostOfActions(path))
                    else:
                        tmp= problem.getCostOfActions(path)+ heureistic(state[0], problem)
                        frontier.push((state[0], curr[1]+ [state[1]]), tmp)

    return None 

def NoCostSearch(problem, frontier):
    """
    for NoCostSearch we search over graph from start state and add it's neighbours to the fringe for next explorations.
    in this type of search we need only states first and second member cordinations and paths
    this kind of search will only be used in BFS and DFS but the only diff is for BFS we should use a Queue for frontier 
    and for DFS we should use Stack.
    """
    closed_set= list()
    s= (problem.getStartState(), [])
    frontier.push(s)
    while not frontier.isEmpty():
        curr= frontier.pop()
        if problem.isGoalState(curr[0]):
            return curr[1]
        if curr[0] not in closed_set:
            closed_set.append(curr[0])
            curr_child= problem.getSuccessors(curr[0])
            for state in curr_child:
                if state[0] not in closed_set:
                    frontier.push((state[0], curr[1]+ [state[1]]))
    return None 


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
