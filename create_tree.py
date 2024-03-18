import random

def create_tree(num_nodes, t):
    num_terminals = 0
    terminal = 0
    while num_terminals < num_nodes:
        num_terminals = 0
        iterator = t.depthfirstiterator()
        last_n = iterator[-1]
        node_leavesnt = []
        num_leaves = 0
        index = 1
        for i in iterator:
            if t.isleaf(i):
                num_leaves += 1
                if t.get(i) == 't' or t.get(i) == 's' or t.get(i) == 'd':
                    num_terminals += 1
                else:
                    node_leavesnt.append(i)
        if num_terminals < num_nodes:
            if num_nodes == num_leaves:
                num_rules = 0
            else:
                num_rules = num_nodes // num_leaves
                if num_rules > num_leaves:
                    num_rules = num_leaves
            applied_r = []
            k = 1
            while k <= num_rules:
                if len(node_leavesnt) != 0:
                    r = random.randint(0, len(node_leavesnt) - 1)
                    if node_leavesnt[r] not in applied_r:
                        applied_r.append(node_leavesnt[r])
                        t = apply_rule(t, node_leavesnt[r], 0)
                        k += 1
            node_leaves = list(set(node_leavesnt) - set(applied_r))
            for j in node_leaves:
                t = apply_rule(t, j, 1)
    iterator = t.depthfirstiterator()
    seq = []
    for i in iterator:
        if t.isleaf(i):
            seq.append(t.get(i))
    return t, seq

