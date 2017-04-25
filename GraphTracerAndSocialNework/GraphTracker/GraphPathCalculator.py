################################################
# Path Calculator.
# Author: Jeremy.
# 
# Descrption: 
#   This application is designed to automatically calculate best route (path)
#   based on the graph infromation from input file.
# 
# Data Structure:
#   A class is defined representing a node in graph. It includes an attribute
#   called neighbors containing all neighbor nodes and corresponding edge cost.
#   Each node class contains a method called search. A dest node will be
#   searched when 
#
#
# Components:
#   1. Read graph information from input file.
#   2. Calculate path with minimum costs between input node and any other
#      nodes in the graph.
################################################
import copy
import sys

# Graph shortest path calculator.
class PathCalculator:

    # Constructor.
    def __init__(self):
        self.nodes = list()

    # Read graph infromation from external file.
    def importGraph(self, filePath):
        self.nodes = list()
        file = open(filePath, "r")
        lines = file.readlines()

        for line in lines:
            # Line of the external file: source + dest + cost.
            contents = line.strip("\n").split("\t")

            # Check if the first node exist
            node1 = self.getNodeByName(contents[0])
            if (node1 == None):
                node1 = Node(contents[0])
                self.nodes.append(node1)

            # Check if the second node exist
            node2 = self.getNodeByName(contents[1])
            if (node2 == None):
                node2 = Node(contents[1])
                self.nodes.append(node2)
            
            cost = contents[2]

            # Add neighbor information
            node1.addNeighbor(node2, cost)
            node2.addNeighbor(node1, cost)

        # Sort the list
        self.nodes.sort(key = lambda x : x.name)

    # Search for all the shortest path to all the other nodes in the graph.
    def searchForPath(self, sourceNodeName):
        for node in self.nodes:
            if node.name == sourceNodeName:
                self.searchForPathHelper(node)

    def searchForPathHelper(self, sourceNode):
        for targetNode in self.nodes:
            print("from " + sourceNode.name + " to " + targetNode.name)
            (path, dist) = sourceNode.search(targetNode)
            print("  " + " Path is ", end = "")
            print(path, end = "")
            print("   " + " Distance is ", end = "")
            print(dist)

    def getNodeByName(self, name):
        for node in self.nodes:
            if (node.name == name):
                return node
        return None

    def printNodeAndNeighbors(self):
        for node in self.nodes:
            print(node.name)
            self.printNeighbors(node.neighbors)

    def printNeighbors(self, neighbors):
            for key in neighbors.keys():
                print((key.name), neighbors[key])

# Node class representing a node in a graph
class Node:

    # Constructor.
    def __init__(self, name):
        self.name = name
        self.neighbors = dict()
        self.neighbors[self] = 0

    def __eq__(self, anotherNode):
        if isinstance(self, type(anotherNode)):
            return self.name == anotherNode.name
        return False;

    def __hash__(self):
        return hash(self.name)

    # Add neighbor node.
    def addNeighbor(self, neighbor, cost):
            self.neighbors[neighbor] = cost

    # Search for the path to destination node with minium cost. 
    def search(self, dest):
        (path, cost)= self.searchHelper(dest, list())
        return ([self.name] + path, cost)

    # Search helper method.
    # The path argument is set to get rid of repeat route.
    def searchHelper(self, dest, route):

        if (len(self.neighbors.keys()) == 0):
            return (None, sys.maxsize)

        if (self.name == dest.name):
            return ([], 0)

        tempPathAndCost = list()
        for key in self.neighbors.keys():
            if (key.name in route): continue
            newList = copy.deepcopy(route)
            newList.append(key.name)
            (path, cost) = key.searchHelper(dest, newList)
            if (path != None):
                tempPathAndCost.append(([key.name] + path, cost + int(self.neighbors[key])))

        if len(tempPathAndCost) == 0:
            return (None, sys.maxsize)

        return min(tempPathAndCost, key = lambda t : t[1])

# Test function
def test():
    filePath = input("Please enter file path for graph information:") # Type in Graph.txt
    calculator = PathCalculator()
    calculator.importGraph(filePath)
    while (1):
        sourceNode = input("Please enter the source node name:")
        calculator.searchForPath(sourceNode)

test()




