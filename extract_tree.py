import random

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def create_tree(num_nodes):
    t = Node('TR')
    n1 = Node('TR')
    n2 = Node('TR')
    t.children.append(n1)
    t.children.append(n2)
    num_terminals = 0
    terminal = 0
    while num_terminals < num_nodes:
        num_terminals = 0
        iterator = depth_first_iterator(t)
        last_n = iterator[-1]
        n_first = 0
        node_leavesnt = []
        num_leaves = 0
        index = 1
        for i in iterator:
            if is_leaf(t, i):
                if index == 1:
                    n_first = i
                    index = 2
                num_leaves += 1
                if t.get(i) == 't' or t.get(i) == 's' or t.get(i) == 'd':
                    num_terminals += 1
                else:
                    node_leavesnt.append(i)
        last_n = i
        if num_terminals < num_nodes:
            if num_nodes == num_leaves:
                num_rules = 0
            else:
                num_rules = num_nodes / num_leaves
                if num_rules > num_leaves:
                    num_rules = num_leaves
            applied_r = []
            k = 1
            while k <= num_rules:
                if len(node_leavesnt) != 0:
                    r = random.randint(0, len(node_leavesnt) - 1)
                    if node_leavesnt[r] not in applied_r:
                        applied_r.append(node_leavesnt[r])
                        t = apply_rule(t, node_leavesnt[r], n_first, last_n, 0)
                        k += 1
            node_leaves = list(set(node_leavesnt) - set(applied_r))
            for j in node_leaves:
                t = apply_rule(t, j, n_first, last_n, 1)
    iterator = depth_first_iterator(t)
    seq = []
    for i in iterator:
        if is_leaf(t, i):
            seq.append(i)
    print(t.tostring())
    return t, seq

def depth_first_iterator(node):
    stack = [node]
    while stack:
        current = stack.pop()
        yield current
        stack.extend(current.children[::-1])

def is_leaf(node, i):
    return len(node.children[i].children) == 0

def apply_rule(node, j, n_first, last_n, flag):
    # Apply rule here
    return node

t, seq = create_tree(num_nodes)

def apply_rule(t, node, first, last_n, terminal):
    if t.get(node) == 'DR':
        if terminal == 1:
            r = 1
        else:
            r = random.randint(2, 3)
        if r == 1:
            t.addnode(node, 'd')
        elif r == 2:
            t.addnode(node, 'DR')
            t.addnode(node, 'DR')
        elif r == 3:
            t.addnode(node, 'SR')
            t.addnode(node, 'd')
    
    if t.get(node) == 'SR':
        if terminal == 1:
            r = 1
        else:
            r = 2
        if r == 1:
            t.addnode(node, 's')
        elif r == 2:
            t.addnode(node, 'SR')
            t.addnode(node, 'SR')
    
    if t.get(node) == 'TR':
        if first == node:
            if terminal == 1:
                r = 1
            else:
                r = random.randint(2, 3)
            if r == 1:
                t.addnode(node, 't')
            elif r == 2:
                t.addnode(node, 'TR')
                t.addnode(node, 'TR')
            elif r == 3:
                t.addnode(node, 'TR')
                t.addnode(node, 'DR')
        else:
            if last_n == node:
                if terminal == 1:
                    r = 1
                else:
                    r = random.randint(1, 3)
                if r == 1:
                    t.addnode(node, 't')
                elif r == 2:
                    t.addnode(node, 'TR')
                    t.addnode(node, 'TR')
                elif r == 3:
                    t.addnode(node, 'DR')
                    t.addnode(node, 'TR')
            else:
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

