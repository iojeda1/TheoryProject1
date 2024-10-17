def dpll_sat_solve(clause_set, partial_assignment):
    # If all clauses are satisfied (empty set of clauses)
    if all(any(lit in partial_assignment for lit in clause) for clause in clause_set):
        return partial_assignment

    # If there is an empty clause, return False (unsatisfiable)
    if any(not clause for clause in clause_set):
        return False

    # Unit Propagation
    unit_clauses = [clause for clause in clause_set if len(clause) == 1]
    for unit_clause in unit_clauses:
        literal = next(iter(unit_clause))  # Get the single literal from the unit clause
        if literal not in partial_assignment and -literal not in partial_assignment:
            new_assignment = partial_assignment.copy()
            new_assignment.add(literal)

            # Apply the literal to the clause set
            new_clause_set = []
            for clause in clause_set:
                if literal not in clause:
                    # Remove the negation of the literal from the clause
                    new_clause = {lit for lit in clause if lit != -literal}
                    new_clause_set.append(new_clause)
            return dpll_sat_solve(new_clause_set, new_assignment)

    # Choose a literal to branch on
    unassigned_literals = set(lit for clause in clause_set for lit in clause) - partial_assignment
    if unassigned_literals:
        literal = next(iter(unassigned_literals))
        
        # Try assigning the literal True (add literal to the assignment)
        result = dpll_sat_solve([clause for clause in clause_set if literal not in clause], partial_assignment | {literal})
        if result:
            return result
        
        # Try assigning the literal False (add -literal to the assignment)
        result = dpll_sat_solve([clause for clause in clause_set if -literal not in clause], partial_assignment | {-literal})
        return result

    # Return False if no satisfying assignment was found
    return False

# Example test cases for DPLL
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

