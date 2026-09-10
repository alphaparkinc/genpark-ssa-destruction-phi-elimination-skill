from client import SSADestruction

def main():
    print("=== Testing SSA Destruction & Phi Elimination ===")
    ssa = SSADestruction()

    phis = {
        "merge_block": [
            ("val_phi", [("block_true", "val_1"), ("block_false", "val_2")])
        ]
    }
    copies = ssa.deconstruct({}, phis)
    print("Copies inserted at predecessor blocks:", copies)
    assert copies["block_true"] == ["val_phi = val_1"]
    assert copies["block_false"] == ["val_phi = val_2"]
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
