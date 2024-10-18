# DPLL 
# Theory of Computing Project01
# Isabel Ojeda, Phoebe Huang, Pablo Oliva Quintana 
import time
import csv

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

# Function to test DPLL with manual test cases and return results for CSV
def test_dpll_wff(num):
    clause_set, Nvars, Nclauses = dpll_test_cases(num)
    partial_assignment = set()
    start_time = time.time()
    result = dpll_sat_solve(clause_set, partial_assignment, Nvars)
    exec_time = int((time.time() - start_time) * 1e6)  # Execution time in microseconds

    if result:
        assignment_str = format_assignment(result, Nvars)
        sat_result = "Satisfiable"
    else:
        assignment_str = 'N/A'
        sat_result = "Unsatisfiable"
    
    return {
        "Test Case": num,
        "WFF": clause_set,
        "SAT Result": sat_result,
        "Assignment": assignment_str,
        "Execution Time (microseconds)": exec_time
    }
    
# Function to run all manual test cases and gather results for CSV
def run_dpll_tests():
    results = []
    start_time = time.time()  # Start timer for total execution time
    for num in range(1, 5+1):  # Running 5 test cases
        result = test_dpll_wff(num)
        results.append(result)
    total_exec_time = int((time.time() - start_time) * 1e6)  # Total execution time in microseconds
    return results, total_exec_time

# Run DPLL tests and capture the results
results, total_exec_time = run_dpll_tests()

# Now write results to a CSV file
with open('dpll_results.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Test Case", "WFF", "SAT Result", "Assignment", "Execution Time (microseconds)"])  # Write header
    for result in results:
        writer.writerow([result["Test Case"], result["WFF"], result["SAT Result"], result["Assignment"], result["Execution Time (microseconds)"]])
    
    # Add total execution time as the final row
    writer.writerow(["Total", "N/A", "N/A", "N/A", total_exec_time])

# Print confirmation message
print(f"DPLL results successfully written into 'dpll_results.csv', including Total Execution Time: {total_exec_time} microseconds")

