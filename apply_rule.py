from HierarchicalTree import HierarchicalTree


def apply_rule(node, terminal):
    import random
    
    if node.value == 'DR':
        if terminal:
            return node.addnode('d')            
        
        r = random.randint(2, 4)        
        
        if r == 2:
            return node.addnode('DR'), node.addnode('DR')
        elif r == 3:
            return node.addnode('SR'), node.addnode('d')
        elif r == 4:
            return node.addnode('SR'), node.addnode('d')
    
    if node.value == 'SR':
        if terminal:
            return node.addnode('s')
        
        return node.addnode('SR'), node.addnode('SR')
    
    if node.value == 'TR':
        if terminal:
            return node.addnode('t')            
        r = random.randint(2, 4)       
        
        if r == 2:
            return node.addnode('TR'), node.addnode('TR')
        elif r == 3:
            return node.addnode('DR'), node.addnode('TR')
        elif r == 4:
            return node.addnode('TR'), node.addnode('DR')


import random

t = HierarchicalTree("TR")

for i in range(400):
    apply_rule(t.randomLeaf(), random.random() < 0.3)

leaves = list(t.leaves())
for leaf in leaves:
    apply_rule(leaf, True)

print(list(map(str, t.leaves())))