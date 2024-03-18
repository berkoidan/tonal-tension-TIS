import numpy as np
import pandas as pd

# Bach Chorale
print('e1-bach')
e1 = np.array([[60, 64, 67, 72], [59, 62, 67, 74], [58, 60, 64, 67], [57, 60, 65, 69], [55, 59, 62, 67], [60, 64, 67, 72]])
np.savetxt('e1-Bach.csv', e1, delimiter=',')

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def add_node(parent, value):
    node = Node(value)
    parent.children.append(node)
    return node

# Create tree
root = Node('TR')
n1 = add_node(root, 'TR')
n2 = add_node(root, 'TR')
n3 = add_node(n1, 'TR')
n4 = add_node(n1, 'DR')
n22 = add_node(n2, 't')
n5 = add_node(n3, 'TR')
n6 = add_node(n3, 'DR')
n7 = add_node(n5, 't')
n8 = add_node(n6, 'd')
n9 = add_node(n4, 'DR')
n10 = add_node(n4, 'DR')
n11 = add_node(n9, 'd')
n12 = add_node(n10, 'SR')
n13 = add_node(n10, 'd')
n14 = add_node(n12, 's')

# Convert tree to string
def tree_to_string(node):
    result = node.value + '\n'
    for child in node.children:
        result += tree_to_string(child)
    return result

tree_string = tree_to_string(root)
print(tree_string)

mkey = [60, 62, 64, 65, 67, 69, 71]  # CMajor
mode = 1

# Perform main analysis
def main_analysis(e1, tree, mkey, mode):
    # Perform analysis here
    vs = np.array([1, 2, 3, 4, 5])  # Placeholder values
    vl = np.array([6, 7, 8, 9, 10])  # Placeholder values
    return vs, vl

vs, vl = main_analysis(e1, root, mkey, mode)
vTIS = vs.T
vLerdahl = vl.T

# Save results to CSV files
np.savetxt('vTIS.csv', vTIS, delimiter=',')
np.savetxt('vLerdahl.csv', vLerdahl, delimiter=',')

