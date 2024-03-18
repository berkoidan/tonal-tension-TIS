from chord_operations.midi2chroma import midi2chroma
from final_measures.TIS_dist import TIS_dist
from study_stability import study_stability

def recursive_tree(t, vkey):
    if t.chord:
        return
    if t.isLeaf():
        raise Exception("Leaf should have chords set in them")
    for child in t.children:
        recursive_tree(child, vkey)
        
    t.chord = t.children[0].chord
    if len(t.children) == 1:
        return
    
    _, _, min_distance, _ = TIS_dist(t.chord, t.chord, vkey, t.value[0].lower())
    for child in t.children:
        _, _, dist, _ = TIS_dist(child.chord, child.chord, vkey, t.value[0].lower())
        if dist <= min_distance:
            min_distance = dist
            t.chord = child.chord
    
    
def recursive_tree2(t, t2, node, index, chords):
    print(t, t2, node, index, chords)
    n_children = node.children
    if not node.isleaf():
        for i in n_children:
            t2, index = recursive_tree(t, t2, i, index, chords)
    if t.isleaf(n):
        t2 = t2.set(n, str(index))
        index += 1
    else:
        if t.get(n) == 'SR':
            if len(n_children) == 1:
                t2 = t2.set(n, str(t2.get(n_children[0])))
            else:
                n_stable = study_stability(t2, n_children, n, chords)
                t2 = t2.set(n, str(n_stable))
        else:
            if t.get(n) == 'DR':
                if len(n_children) == 1:
                    t2 = t2.set(n, str(t2.get(n_children[0])))
                else:
                    if t.get(n_children[0]) == 'SR':
                        t2 = t2.set(n, str(t2.get(n_children[1])))
                    else:
                        n_stable = study_stability(t2, n_children, n, chords)
                        t2 = t2.set(n, str(n_stable))
            else:
                if t.get(n) == 'TR':
                    if len(n_children) == 1:
                        t2 = t2.set(n, str(t2.get(n_children[0])))
                    else:
                        if t.get(n_children[0]) == 'TR':
                            if t.get(n_children[1]) == 'TR':
                                n_stable = study_stability(t2, n_children, n, chords)
                                t2 = t2.set(n, str(n_stable))
                            else:
                                t2 = t2.set(n, str(t2.get(n_children[1])))
                        else:
                            t2 = t2.set(n, str(t2.get(n_children[1])))
    return t2, index

