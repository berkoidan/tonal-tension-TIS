from Chord import Chord
from HirerarchicalTree.HierarchicalTree import HierarchicalTree
from final_measures.TIS_base import TIS
from final_measures.TIS_dist import TIS_dist

def find_harmonic_function(chord, vkey):
    dist = [TIS.angular_rel(vkey[0], chord, vkey[1]),
            TIS.angular_rel(vkey[0], chord, vkey[2]),
            TIS.angular_rel(vkey[0], chord, vkey[3])]
    
    harmf = ('t','d','s')[dist.index(min(dist))]
    leaf = HierarchicalTree(harmf)
    leaf.setChord(chord)
    return leaf

RULES = [
    [('t', 't', 's', 't')],
    [('SR', 's')],
    [('SR', 'SR', 'SR')],
    [('DR', 'DR', 'DR'), ('TR', 'TR', 'TR')],
    [('DR', 'SR', 'd'), ('TR', 'TR', 'DR')],
    [('DR', 'd')], 
    [('TR', 'DR', 't')],
    [('TR', 't')],
    [('TR', 'TR', 'SR')],
]

def apply_rule(seq, index, rule, vkey):
    root_value = rule[0]
    children_values = tuple(rule[1:])
    
    max_index = index + len(children_values)
    
    if max_index > len(seq):
        return seq, False
    
    children = seq[index:max_index]
    
    if tuple(map(lambda child: child.value, children)) == children_values:
        # print("applying", root_value, '->', children_values)
        newnode = HierarchicalTree(root_value)
        newnode.addsubtrees(children)
        newnode.setChord(choose_chord(list(map(lambda child: child.chord, children)), vkey, root_value[0].lower()))
        del seq[index+1:max_index]
        seq[index] = newnode
        return seq, True
    
    return seq, False

def tree_build_step(seq, vkey):
    # print(list(map(lambda node: node.value, seq)))
    middle_i = len(seq) // 2
    for ruleset in RULES:
        for i in range(len(seq)):
            stepdiff = ((i + 1) // 2) * (1 if i % 2 == 0 else - 1)
            for rule in ruleset:
                seq, applied = apply_rule(seq, middle_i + stepdiff, rule, vkey)
                if applied:
                    return seq
    print("Tree:", list(map(str, seq)))
    print("Seq:", list(map(lambda node: node.value, seq)))
    raise Exception("Could not apply rule")

def create_tree(chords, vkey):    
    seq = list(map(lambda chord: find_harmonic_function(chord, vkey), chords))
  
    while len(seq) > 1:
        seq = tree_build_step(seq, vkey)
    
    return seq[0], list(seq[0].leaves())

def choose_chord(chords, vkey, tf):
    dists = list(map(lambda chord: TIS_dist(chord, chord, vkey, tf)[2], chords))
    return chords[dists.index(min(dists))]    
