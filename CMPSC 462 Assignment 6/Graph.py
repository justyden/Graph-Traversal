# A simple graph data structure that operates
# with nodes and can perform basic functions.

from Node import *
from collections import defaultdict
from Queue import *
from Stack import *

# The graph class.


class Graph:
    # The constructor that takes a list of tuples.
    # The tuples are then converted to the nodes and edges.
    def __init__(self, inputNodes):
        self.nodes = defaultdict(set)
        # This calls the function to create the nodes and edges of the graph.
        self.startGraph(inputNodes)

    # This adds a node if it has no edges.
    def addNode(self, inputNode):
        self.nodes[inputNode]

    # This figures out the size of the tuple and creates the nodes correctly.
    def startGraph(self, inputNodes):
        for nodes in inputNodes:
            if len(nodes) == 1:  # This means it has no edges.
                self.addNode(nodes[0])
            else:  # This means it did have an edge.
                self.createEdges(nodes[0], nodes[1])

    # This creates the edges for each node. It saves the actual node object.
    def createEdges(self, inputNode1, inputNode2):
        self.nodes[inputNode1].add(inputNode2)
        self.nodes[inputNode2].add(inputNode1)

    # This is a helper function for printEdges that correctly displays the
    # the information.
    def printEdgesHelper(self, inputValues):
        tempNodes = ""
        for i in inputValues:
            if (i == (len(inputValues) - 1)):
                tempNodes = tempNodes + str(i.number)
            else:
                tempNodes = tempNodes + str(i.number) + ", "
        tempNodes = tempNodes[:-2]
        return tempNodes

    # This all the nodes and the edges that they have. Correctly formats
    # the data.
    def printEdges(self):
        for key, values in self.nodes.items():
            print("Node " + str(key) + " : " + self.printEdgesHelper(values))

    # Calculates all the isolated nodes within the graph.
    def isolatedNodes(self):
        tempList = []
        for key in self.nodes:
            # This determines if the set is empty.
            if self.nodes[key] == set():
                tempNode = "Node " + str(key.number)
                tempList.append(tempNode)
        # Returns all nodes that have no edges connected to them.
        return tempList

    # Finds a path from a start node to an end node.
    def findPath(self, inputNode1, inputNode2, path=[]):
        # This simply adds the node to the current path.
        path = path + [inputNode1]
        # This means the node does not exist.
        if inputNode1 == None:
            return None
        # This means the path was found.
        if inputNode1 == inputNode2:
            return path
        # This is for each set associated with a node.
        for i in self.nodes[inputNode1]:
            if i not in path:
                # This creates a new path to keep searching.
                # The new inputNode1 is now each node in the set.
                search = self.findPath(i, inputNode2, path)
                # This means it existed and found it.
                if search:
                    return search
        # The path was not found.
        return None

    # Finds all paths from a start node to an end node.
    def findAllPaths(self, inputNode1, inputNode2, path=[], allPaths=[]):
        # This simply adds the node to the current path.
        path = path + [inputNode1]
        # This means the node does not exist.
        if inputNode1 == None:
            return None
        # This means the path was found.
        if inputNode1 == inputNode2:
            allPaths.append(path)
        # This is for each set associated with a node.
        for i in self.nodes[inputNode1]:
            if i not in path:
                # This creates a new path to keep searching.
                # The new inputNode1 is now each node in the set.
                search = self.findAllPaths(i, inputNode2, path, allPaths)
        # Returns all paths.
        return allPaths

    # This performs a depth first search on the graph. It returns
    # the path of every node that is connected to the input node.
    def dfs(self, inputNode, nodeList=[]):
        if inputNode == None:
            # This means the node did not exist.
            return None
        # This adds the node to the path list.
        nodeList.append(inputNode)
        # This searches each edge of the current node.
        for i in self.nodes[inputNode]:
            # This checks that the node was not already searched.
            if i not in nodeList:
                self.dfs(i, nodeList)
        # Returns the list.
        return nodeList

    # This performs a bfs on a graph. Returns the list of nodes.
    def bfs(self, inputNode, nodeList=[], nodeQueue=Queue()):
        # This means the node was not found.
        if inputNode == None:
            return None
        # This adds the current node to the queue.
        nodeQueue.enqueue(inputNode)
        # This adds the current node as visted to the list.
        nodeList.append(inputNode)
        # This makes sure there is still more nodes to check.
        while nodeQueue.size() != 0:
            # This dequeues the next node and saves it as a temporary node.
            tempNode = nodeQueue.dequeue()
            # This checks each node that is connected to the current node.
            for i in self.nodes[tempNode]:
                # Makes sure the node was not checked.
                if i not in nodeList:
                    nodeList.append(i)
                    nodeQueue.enqueue(i)
        # Returns the list.
        return nodeList

    # Checks to see if the graph is connected.
    def checkConnected(self, inputNode1):
        # This checks to make sure every node was visted.
        # This should mean the list that was returned is equal
        # to the amount of nodes in the graph.
        if len(self.bfs(inputNode1)) == len(self.nodes):
            return True
        else:
            return False


# This is a function to help display a path if it was found.
def printPath(inputPath):
    if inputPath == None:
        print("None")
    else:
        for i in range(len(inputPath)):
            inputPath[i] = "Node " + str(inputPath[i].number)
        print(inputPath)


# This functions takes into account all paths
# and displays them correctly.
def printAllPaths(inputPaths):
    if inputPaths == None:
        print("None")
    else:
        for i in range(len(inputPaths)):
            print("Path " + str(i))
            for k in range(len(inputPaths[i])):
                print("Node " + str(inputPaths[i][k]))
            print()


node0 = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)

graph1 = Graph(([node0, node1], [node0, node2],
                [node1, node3], [node2, node4],
                [node4, node1], [node5], [node6],
                [node4, node3], [node1, node6],
                [node4, node5],
                [node7], [node8], [node9]))
# graph1.createEdges(node7, node8)
# graph1.createEdges(node8, node9)
# graph1.createEdges(node9, node1)

# graph1.printEdges()
# print(graph1.isolatedNodes())
# printPath(graph1.findPath(node0, node3))
# printPath(graph1.findPath(node1, node5))
# printAllPaths(graph1.findAllPaths(node0, node3))
# printAllPaths(graph1.findAllPaths(node1, node2))
# printPath(graph1.dfs(node0))
# printPath(graph1.dfs(node4))
# printPath(graph1.bfs(node0))
# printPath(graph1.bfs(node4))
# print(graph1.checkConnected(node0))
