from final_measures.TIS_dist import TIS_dist

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
