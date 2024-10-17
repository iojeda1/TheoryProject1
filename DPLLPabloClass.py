import time
import random

# DPLL SAT solver
def dpll_sat_solve(clause_set, partial_assignment):
    # If all clauses are satisfied (empty set of clauses)
    if all(any(lit in partial_assignment for lit in clause) for clause in clause_set):
        return partial_assignment

    # If there is an empty clause, return False (unsatisfiable)
    if any(not clause for clause in clause_set):
        return False

    # Unit Propagation: Assign literals from unit clauses
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

# Helper function to format the assignment result in binary
def format_assignment(assignment, num_vars):
    result = []
    for i in range(1, num_vars + 1):
        if i in assignment:
            result.append('1')
        elif -i in assignment:
            result.append('0')
        else:
            result.append('0')  # Default to 0 if unassigned
    return ','.join(result)

# Function to run DPLL on multiple test cases and collect timing
def run_dpll_tests(test_cases):
    problem_num = 1
    
    for test_case in test_cases:
        Nvars, Nclauses, LitsPerClause, Ntrials = test_case
        for _ in range(Ntrials):
            # Generate a random SAT problem (for this example, you might have a fixed set instead)
            clause_set = generate_random_sat_problem(Nvars, Nclauses, LitsPerClause)
            partial_assignment = set()

            start_time = time.time()
            result = dpll_sat_solve(clause_set, partial_assignment)
            exec_time = int((time.time() - start_time) * 1e6)  # Execution time in microseconds

            satisfiable = 'S' if result else 'U'
            
            # Format output
            if result:
                assignment_str = format_assignment(result, Nvars)
                print(f"{problem_num},{Nvars},{Nclauses},{LitsPerClause},{exec_time},{satisfiable},{assignment_str}")
            else:
                print(f"{problem_num},{Nvars},{Nclauses},{LitsPerClause},{exec_time},{satisfiable},0")

            problem_num += 1

# Function to generate random SAT problems
def generate_random_sat_problem(Nvars, Nclauses, LitsPerClause):
    clause_set = []
    for _ in range(Nclauses):
        clause = set()
        while len(clause) < LitsPerClause:
            literal = random.randint(1, Nvars)
            if random.choice([True, False]):
                literal = -literal
            clause.add(literal)
        clause_set.append(clause)
    return clause_set

# Test cases used for incremental search
test_cases = [
    (4, 10, 2, 10),
    (8, 16, 2, 10),
    (12, 24, 2, 10),
    (16, 32, 2, 10),
    (20, 40, 2, 10),
    (24, 48, 2, 10),
    (28, 56, 2, 10)
]

# Run the DPLL tests
run_dpll_tests(test_cases)
