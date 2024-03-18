from chord_operations.chord_qual import chord_qual
from chord_operations.midi2chroma import midi2chroma
from chord_operations.normal_fft import normal_fft
from final_measures.TIS_dist import TIS_dist


def TIS_surface(t_dist, mdom, m2, pnode, skey, tf):
    m2 = m2 % 12
    m2 = sorted(m2)
    mdom = mdom % 12
    mdom = sorted(mdom)
    c2 = midi2chroma(m2)
    cdom = midi2chroma(mdom)
    
    t2, mod_c2 = normal_fft(c2)
    tdiss = abs(chord_qual(t2))
    tdiss = 1 - tdiss
    
    tloc1, tloc2, tloc3, tloc = TIS_dist(cdom, c2, skey, tf)
    
    p_i = t_dist.getparent(pnode)
    tinh = 0
    while p_i != 0:
        tinh = tinh + t_dist.get(p_i)
        p_i = t_dist.getparent(p_i)
    
    ls = [tloc1, tloc2, tloc3, tloc] + tinh
    return ls

