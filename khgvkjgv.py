import random
import time

# Set seed for consistent randomness
random.seed(42)

# Generate WFF (Well-Formed Formula)
def build_wff(Nvars, Nclauses, LitsPerClause):
    wff = []
    for _ in range(Nclauses):
        clause = []
        for _ in range(LitsPerClause):
            var = random.randint(1, Nvars)
            if random.choice([True, False]):
                var = -var
            clause.append(var)
        wff.append(clause)
    return wff

# Generate a random assignment for consistency
def generate_initial_assignment(Nvars):
    return [random.randint(0, 1) for _ in range(Nvars + 1)]

# Unit Clause Solver (from your Unit Clause code)
def unit_clause(Wff, Assignment): 
    c = True
    while c: 
        c = False
        for clause in Wff: 
            if len(clause) == 1:
                literal = clause[0]
                index = abs(literal)
                if literal > 0: 
                    Assignment[index] = 1
                else:
                    Assignment[index] = 0
                # Modify WFF by implementing unit clause rules 
                Wff2 = []
                for clause2 in Wff:
                    if literal in clause2:
                        continue 
                    elif -literal in clause2:
                        newclause = [x for x in clause2 if x != -literal]
                        if len(newclause) == 0:
                            return False, Assignment, Wff
                        else:
                            Wff2.append(newclause)
                    else: 
                        Wff2.append(clause2)
                Wff = Wff2 
                c = True 
                break 
    return True, Assignment, Wff

# Incremental Search (from your Incremental Search code)
def incremental(Wff, Nvars, Nclauses, Assignment):
    satisfiable = False
    attempts = 0 
    max_attempts = 2 ** Nvars  # 2^N max attempts
    while attempts < max_attempts:
        satisfiable = True  
        for i in range(0, Nclauses):
            clause = Wff[i]
            clauseSat = False
            for literal in clause:
                index = abs(literal)
                val = Assignment[index]
                if literal > 0 and val == 1:
                    clauseSat = True
                    break
                elif literal < 0 and val == 0:
                    clauseSat = True
                    break
            if not clauseSat:
                satisfiable = False
                break
        if satisfiable:
            return True, Assignment
        # Make small flips to generate more combinations
        flip = random.randint(1, Nvars)
        Assignment[flip] = 1 - Assignment[flip]
        attempts += 1
    return False, Assignment

# Test and compare both methods
def test_and_compare(Nvars, Nclauses, LitsPerClause):
    # Generate WFF and Initial Assignment
    wff = build_wff(Nvars, Nclauses, LitsPerClause)
    initial_assignment = generate_initial_assignment(Nvars)

    # Test Unit Clause
    unit_assignment = initial_assignment[:]
    start_time = time.time()
    satisfiable_uc, final_assignment_uc, _ = unit_clause(wff, unit_assignment)
    end_time = time.time()
    exec_time_uc = int((end_time - start_time) * 1e6)  # microseconds
    print(f"Unit Clause: Satisfiable: {satisfiable_uc}, Assignment: {final_assignment_uc}, Time: {exec_time_uc} µs")

    # Test Incremental Search
    incremental_assignment = initial_assignment[:]
    start_time = time.time()
    satisfiable_is, final_assignment_is = incremental(wff, Nvars, Nclauses, incremental_assignment)
    end_time = time.time()
    exec_time_is = int((end_time - start_time) * 1e6)  # microseconds
    print(f"Incremental Search: Satisfiable: {satisfiable_is}, Assignment: {final_assignment_is}, Time: {exec_time_is} µs")

# Run comparison on a test case
test_and_compare(Nvars=4, Nclauses=10, LitsPerClause=2)
