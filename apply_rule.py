def apply_rule(t, node, terminal):
    import random
    
    if t[node] == 'DR':
        if terminal == 1:
            r = 1
        else:
            r = random.randint(2, 4)
        
        if r == 1:
            t.addnode(node, 'd')
        elif r == 2:
            t.addnode(node, 'DR')
            t.addnode(node, 'DR')
        elif r == 3:
            t.addnode(node, 'SR')
            t.addnode(node, 'd')
        elif r == 4:
            t.addnode(node, 'SR')
            t.addnode(node, 'd')
    
    if t[node] == 'SR':
        if terminal == 1:
            r = 1
        else:
            r = 2
        
        if r == 1:
            t.addnode(node, 's')
        elif r == 2:
            t.addnode(node, 'SR')
            t.addnode(node, 'SR')
    
    if t[node] == 'TR':
        if terminal == 1:
            r = 1
        else:
            r = random.randint(2, 4)
        
        if r == 1:
            t.addnode(node, 't')
        elif r == 2:
            t.addnode(node, 'TR')
            t.addnode(node, 'TR')
        elif r == 3:
            t.addnode(node, 'DR')
            t.addnode(node, 'TR')
        elif r == 4:
            t.addnode(node, 'TR')
            t.addnode(node, 'DR')

