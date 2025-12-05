# pragma_core_test.py

import hashlib
from pragma_core import PragmaDiagnostic

def run_test():
    print("\n=== PRAGMA-CORE SELF-TEST ===\n")

    input_data = "self-test-input"
    logic_data = "logic-v1"

    input_hash = hashlib.sha256(input_data.encode()).hexdigest()
    logic_hash = hashlib.sha256(logic_data.encode()).hexdigest()
    expected_output = hashlib.sha256((input_hash + logic_hash).encode()).hexdigest()

    diag = PragmaDiagnostic(system_id="CORE-TEST")

    I = diag.assess_integrity(input_hash, expected_output, logic_hash)
    E = diag.assess_efficiency(1800, 48, {"cycles": 2000, "memory": 64})
    C = diag.assess_coherence("NO CONTRADICTIONS")

    result = diag.generate_pragmatic_score()

    print("Integrity:", I)
    print("Efficiency:", E)
    print("Coherence:", C)
    print("\nFinal Score:", result["pragmatic_score"])
    print("Practitioner:", result["is_practitioner"])

    return result

if __name__ == "__main__":
    run_test()