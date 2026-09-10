import collections

class SSADestruction:
    """
    Out-of-SSA / SSA Destruction Engine.
    Replaces phi-nodes phi(x1, x2) in predecessor blocks with parallel copy operations.
    """
    def deconstruct(self, basic_blocks, phi_nodes):
        copies_added = collections.defaultdict(list)
        for bb, phis in phi_nodes.items():
            for dest, incoming in phis:
                for pred_bb, src_var in incoming:
                    copies_added[pred_bb].append(f"{dest} = {src_var}")
        return dict(copies_added)
