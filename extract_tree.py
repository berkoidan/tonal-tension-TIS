import random

from HierarchicalTree import HierarchicalTree
from apply_rule import apply_rule

def create_tree(num_nodes):
    t = HierarchicalTree('TR')
    n1 = t.addnode('TR')
    n2 = t.addnode('TR')
    
    num_terminals = 0
    while num_terminals < num_nodes:
        num_terminals = 0
        iterator = list(t.dfs())
        node_leavesnt = []
        num_leaves = 0
        index = 1
        for i in iterator:
            if i.isLeaf():
                if index == 1:
                    n_first = i
                    index = 2
                num_leaves += 1
                if i.value in ('t', 's', 'd'):
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
                    r = random.choice(node_leavesnt)
                    if r not in applied_r:
                        applied_r.append(r)
                        apply_rule(r, False)
                        k += 1
            node_leaves = list(set(node_leavesnt) - set(applied_r))
            for j in node_leaves:
                apply_rule(j, True)
    iterator = list(t.dfs())
    seq = []
    for i in iterator:
        if i.isLeaf():
            seq.append(i)
    return t, seq

num_nodes = 5

t, seq = create_tree(num_nodes)
print(t, list(map(str, seq)))

