def dpll_sat_solve(clause_set, partial_assignment):
    # Check if all clauses are satisfied  
    if all(any(lit in partial_assignment for lit in clause) for clause in clause_set):  
        return partial_assignment  
    
    # Check if there is an empty clause  
    if any(not clause for clause in clause_set):  
        return False  
    
    # Unit Propagation  
    unit_clauses = [clause for clause in clause_set if len(clause) == 1]  
    for unit_clause in unit_clauses:  
        literal = next(iter(unit_clause))  # Fix this to extract the first element from the set
        if literal in partial_assignment:  
            continue  
        new_assignment = partial_assignment.copy()  
        new_assignment.add(literal)  
        new_clause_set = [clause for clause in clause_set if literal not in clause]  
        result = dpll_sat_solve(new_clause_set, new_assignment)  
        if result:  
            return result  
    
    # Branching on a new variable  
    unassigned_literals = set(lit for clause in clause_set for lit in clause) - partial_assignment  
    if unassigned_literals:  
        literal = unassigned_literals.pop()  
        result = dpll_sat_solve(clause_set, partial_assignment | {literal})  
        if result:  
            return result  
        result = dpll_sat_solve(clause_set, partial_assignment | {-literal})  
        return result  
    return False

# Test cases for DPLL
def run_dpll_tests():
    test_cases = [
        # Simple satisfiable
        ({1, 2}, {-1, 3}, {-2, 3}),
        # Simple unsatisfiable
        ({1}, {-1}),
        # Unit propagation test
        ({1}, {1, 2}, {-1, 3}, {-3, -2}),
        # Complex satisfiable
        ({1, 2}, {-1, 3}, {2, -3}, {-1, -2}),
        # Complex unsatisfiable
        ({1, 2}, {-1, 3}, {2, -3}, {-1, -2}, {-2, -3}, {3, -1}),
        # Chain implication satisfiable
        ({1, 2}, {-2, 3}, {-3, 4}, {-4, 5}),
        # Single literal clause
        ({1}, {-2}),
        # Multiple unit propagation
        ({1}, {1, 2}, {-1, -2}, {3, -2}, {-3, 1}),
        # All negative literals (satisfiable)
        ({-1, -2}, {-2, -3}, {-1, -3}),
        # Contradictory unit clauses (unsatisfiable)
        ({1}, {-1}, {2}, {-2}),
    ]
    
    for i, clause_set in enumerate(test_cases):
        print(f"\nTest Case {i+1}: CNF Clause Set: {clause_set}")
        clause_set = [set(clause) for clause in clause_set]  # Convert to set of sets
        partial_assignment = set()
        result = dpll_sat_solve(clause_set, partial_assignment)
        if result:
            print(f"Satisfying assignment: {result}")
        else:
            print("Not satisfiable")

# Run the DPLL test cases
run_dpll_tests()
