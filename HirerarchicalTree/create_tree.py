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
    [('SR', 's')],
    [('SR', 'SR', 'SR')],
    [('DR', 'DR', 'DR'), ('TR', 'TR', 'TR')],
    [('DR', 'SR', 'd'), ('TR', 'DR', 't'), ('TR', 'TR', 'DR')],
    [('DR', 'd')], 
    [('TR', 't')]
]

def apply_rule(seq, index, rule, vkey):
    if len(rule) == 3 and index + 1 < len(seq) and seq[index].value == rule[1] and seq[index+1].value == rule[2]: 
        print("applying", rule)
        newnode = HierarchicalTree(rule[0])
        newnode.addsubtrees(seq[index], seq[index+1])
        newnode.setChord(choose_chord(seq[index].chord, seq[index+1].chord, vkey, rule[0][0].lower()))
        seq.pop(index+1)
        seq[index] = newnode
        return seq, True
    
    if len(rule) == 2 and seq[index].value == rule[1]:
        print("applying", rule)
        newnode = HierarchicalTree(rule[0])
        newnode.addsubtree(seq[index])
        newnode.setChord(seq[index].chord)
        seq[index] = newnode
        return seq, True
    
    return seq, False

def tree_build_step(seq, vkey):
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

def choose_chord(chord1, chord2, vkey, tf):
    _, _, min_distance1, _ = TIS_dist(chord1, chord1, vkey, tf)
    _, _, min_distance2, _ = TIS_dist(chord2, chord2, vkey, tf)
    if(min_distance1 < min_distance2):
        return chord1
    return chord2
