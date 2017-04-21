import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
class Node():
    def __init__(self, id):
        self.id, self.depth, self.connected_rel = id, 1, []
    def connected(self, n):
        self.connected_rel.append(n)
    def update(self):
        for n in self.connected_rel:
            if (n.depth < self.depth +1):
                n.depth = self.depth +1
                n.update()

nodes = {}

n = int(raw_input())  # the number of relationships of influence
for i in xrange(n):
    # x: a relationship of influence between two people (x influences y)
    x, y = [int(j) for j in raw_input().split()]
    if x not in nodes:
        nodes[x] = Node(x)
    if y not in nodes:
        nodes[y] = Node(y)
    nx, ny = nodes[x], nodes[y]
    nx.connected(ny)
    nx.update()
# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
max_dep = 0 
for j in nodes.values():
    max_dep = max(j.depth, max_dep)

# The number of people involved in the longest succession of influences
print max_dep
