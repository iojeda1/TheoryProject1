# DPLL 
import time

# DPLL SAT solver with improved variable tracking and backtracking
def dpll_sat_solve(clause_set, assignment, num_vars):
    # If all clauses are satisfied, return the assignment
    if all(any(lit in assignment for lit in clause) for clause in clause_set):
        return assignment

    # If any clause is empty (unsatisfied), return False
    if any(not clause for clause in clause_set):
        return False

    # Perform unit propagation
    unit_clauses = [clause for clause in clause_set if len(clause) == 1]
    for unit_clause in unit_clauses:
        literal = next(iter(unit_clause))  # Get the single literal from the unit clause
        if literal not in assignment and -literal not in assignment:
            new_assignment = assignment.copy()
            new_assignment.add(literal)
            new_clause_set = []
            for clause in clause_set:
                if literal not in clause:
                    new_clause = [lit for lit in clause if lit != -literal]
                    new_clause_set.append(new_clause)
            return dpll_sat_solve(new_clause_set, new_assignment, num_vars)

    # Choose a literal to branch on
    unassigned_literals = {lit for clause in clause_set for lit in clause if lit not in assignment and -lit not in assignment}
    if unassigned_literals:
        literal = next(iter(unassigned_literals))
        # Try assigning the literal positively
        new_assignment = assignment.copy()
        new_assignment.add(literal)
        result = dpll_sat_solve([clause for clause in clause_set if literal not in clause], new_assignment, num_vars)
        if result:
            return result
        # Backtrack and try assigning the literal negatively
        new_assignment = assignment.copy()
        new_assignment.add(-literal)
        return dpll_sat_solve([clause for clause in clause_set if -literal not in clause], new_assignment, num_vars)

    return False

# Helper function to convert assignment set to a binary array for output
def format_assignment(assignment, num_vars):
    result = [0] * num_vars
    for lit in assignment:
        if lit > 0:
            result[lit - 1] = 1
        elif lit < 0:
            result[abs(lit) - 1] = 0
    return result

# Function to define manual test cases for DPLL, now using list instead of set
def dpll_test_cases(num):
    if num == 1:
        # Test Case 1: (x1 OR NOT x2) AND (NOT x1 OR x2)
        clause_set = [[1, -2], [-1, 2]]  # Changed to list
        Nvars = 2
        Nclauses = 2
        return clause_set, Nvars, Nclauses
    elif num == 2:
        # Test Case 2: (x1 OR x2) AND (NOT x1 OR x2) AND (x1 OR NOT x2)
        clause_set = [[1, 2], [-1, 2], [1, -2]]  # Changed to list
        Nvars = 2
        Nclauses = 3
        return clause_set, Nvars, Nclauses
    elif num == 3:
        # Test Case 3: (x1 OR x2 OR x3) AND (NOT x1 OR NOT x2) AND (x2 OR NOT x3) AND (x1 OR x2)
        clause_set = [[1, 2, 3], [-1, -2], [2, -3], [1, 2]]  # Changed to list
        Nvars = 3
        Nclauses = 4
        return clause_set, Nvars, Nclauses
    elif num == 4:
        # Test Case 4: (x1 OR x2) AND (x1 OR NOT x2) AND (x2 OR x3) AND (NOT x1 OR x3) AND (NOT x3 OR NOT x2)
        clause_set = [[1, 2], [1, -2], [2, 3], [-1, 3], [-3, -2]]  # Changed to list
        Nvars = 3
        Nclauses = 5
        return clause_set, Nvars, Nclauses
    elif num == 5:
        # Test Case 5: Contradictory clauses (x1) AND (NOT x1)
        clause_set = [[1], [-1]]  # Changed to list
        Nvars = 1
        Nclauses = 2
        return clause_set, Nvars, Nclauses

# Function to test DPLL with manual test cases
def test_dpll_wff(num):
    clause_set, Nvars, Nclauses = dpll_test_cases(num)
    partial_assignment = set()
    start_time = time.time()
    result = dpll_sat_solve(clause_set, partial_assignment, Nvars)
    exec_time = int((time.time() - start_time) * 1e6)  # Execution time in microseconds
    
    print(f"Test Case {num}: (wff form): {clause_set}")
    if result:
        assignment_str = format_assignment(result, Nvars)
        print(f"SAT Result: Satisfiable")
        print(f"Assignment: {assignment_str}")
    else:
        print(f"SAT Result: Unsatisfiable")
    
    print(f"Execution Time: {exec_time} µs\n")

# Function to run all manual test cases for DPLL
def run_dpll_manual_tests():
    for num in range(1, 6):
        test_dpll_wff(num)

# Run the manual test cases
run_dpll_manual_tests()