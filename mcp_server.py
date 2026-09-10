import sys
import json
from client import SSADestruction

ssa = SSADestruction()

def handle_call(name, arguments):
    if name == "deconstruct":
        phis = arguments["phi_nodes"]
        return ssa.deconstruct({}, phis)
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_call(req.get("name"), req.get("arguments", {}))
            print(json.dumps({"id": req.get("id"), "result": res}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()

if __name__ == "__main__":
    main()
