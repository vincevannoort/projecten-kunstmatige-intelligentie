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

def genericSearchMethod(problem, fringe):
    """
    Generic Method to create DFS, BFS and UCS from.
    """
    closed = set() # will contain positions

    # add the starting position and with am empty path
    fringe.push((problem.getStartState(), [], 0, 0))

    # keep checking every option, and go depth first by poping from the list
    while not fringe.isEmpty():
        # pop from the list stack
        position, path, _, totalCost = fringe.pop()

        # continue if already closed set
        if position in closed:
            continue
        
        # check if goal state, with the position
        if problem.isGoalState(position):
            # end goal is found, so return the path taken
            return path

        # add to closed set
        closed.add(position)

        # add successors, that have not been closed yet, search for succesors by position
        # getSuccessors returns a list of tuples in the form of (successor, path, stepCost)
        successors = problem.getSuccessors(position)
        for positionSuc, actionSuc, stepCostSuc in successors:
            # if position is not in the closed list
            if (positionSuc not in closed):
                # add append next action to current path
                fringe.push((positionSuc, path + [actionSuc], stepCostSuc, totalCost + stepCostSuc))

    # if no solution is found, return a empty list
    return []

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.
    """
    # will contain tuples of (successor, path, stepCost)
    fringe = util.Stack() 

    return genericSearchMethod(problem, fringe)

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    # will contain tuples of (successor, path, stepCost)
    fringe = util.Queue() 

    return genericSearchMethod(problem, fringe)

def uniformCostSearch(problem):
    """
    Search the node of least total cost first.
    """
    # will contain tuples of (successor, path, stepCost)
    # the priority in this priorityqueue is the stepCost
    fringe = util.PriorityQueueWithFunction(lambda item: item[3]) 

    return genericSearchMethod(problem, fringe)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""

    fringe = util.PriorityQueueWithFunction(lambda item: heuristic(item[0], problem) + item[3])
    return genericSearchMethod(problem, fringe)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
