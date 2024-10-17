import time
import random
import matplotlib.pyplot as plt

# DPLL SAT solver
def dpll_sat_solve(clause_set, partial_assignment):
    if all(any(lit in partial_assignment for lit in clause) for clause in clause_set):
        return partial_assignment

    if any(not clause for clause in clause_set):
        return False

    unit_clauses = [clause for clause in clause_set if len(clause) == 1]
    for unit_clause in unit_clauses:
        literal = next(iter(unit_clause))
        if literal not in partial_assignment and -literal not in partial_assignment:
            new_assignment = partial_assignment.copy()
            new_assignment.add(literal)
            new_clause_set = []
            for clause in clause_set:
                if literal not in clause:
                    new_clause = {lit for lit in clause if lit != -literal}
                    new_clause_set.append(new_clause)
            return dpll_sat_solve(new_clause_set, new_assignment)

    unassigned_literals = set(lit for clause in clause_set for lit in clause) - partial_assignment
    if unassigned_literals:
        literal = next(iter(unassigned_literals))
        result = dpll_sat_solve([clause for clause in clause_set if literal not in clause], partial_assignment | {literal})
        if result:
            return result
        result = dpll_sat_solve([clause for clause in clause_set if -literal not in clause], partial_assignment | {-literal})
        return result

    return False

# Function to generate random SAT problems with some unsatisfiable cases
def generate_dpll_test_case(Nvars, Nclauses, LitsPerClause, force_unsat=False):
    clause_set = []
    for _ in range(Nclauses):
        clause = set()
        while len(clause) < LitsPerClause:
            literal = random.randint(1, Nvars)
            if random.choice([True, False]):  # Randomly negate the literal
                literal = -literal
            clause.add(literal)
        clause_set.append(clause)
    
    # Optionally force an unsatisfiable formula by adding contradicting clauses
    if force_unsat:
        literal = random.randint(1, Nvars)
        clause_set.append({literal})
        clause_set.append({-literal})  # Add contradiction

    return clause_set

# Function to run DPLL on multiple test cases and collect timing
def run_dpll_tests(test_cases, force_unsat_ratio=0.2):
    results = []
    for test_case in test_cases:
        Nvars, Nclauses, LitsPerClause, Ntrials = test_case
        for _ in range(Ntrials):
            # Randomly decide whether to generate an unsatisfiable case
            force_unsat = random.random() < force_unsat_ratio
            clause_set = generate_dpll_test_case(Nvars, Nclauses, LitsPerClause, force_unsat)
            partial_assignment = set()
            start_time = time.time()
            result = dpll_sat_solve(clause_set, partial_assignment)
            exec_time = int((time.time() - start_time) * 1e6)  # Execution time in microseconds
            problem_size = Nvars * Nclauses
            satisfiable = 'S' if result else 'U'
            results.append((problem_size, exec_time, satisfiable))
    return results

# Function to plot the results
def plot_results(results, algorithm_name):
    x_yes = [r[0] for r in results if r[2] == 'S']  # Satisfiable instances
    y_yes = [r[1] for r in results if r[2] == 'S']
    x_no = [r[0] for r in results if r[2] == 'U']  # Unsatisfiable instances
    y_no = [r[1] for r in results if r[2] == 'U']

    plt.scatter(x_yes, y_yes, color='green', marker='o', label='Satisfiable')
    plt.scatter(x_no, y_no, color='red', marker='x', label='Unsatisfiable')

    plt.xlabel('Problem Size (Nvars * NClauses)')
    plt.ylabel('Execution Time (µs)')
    plt.title(f'Performance of {algorithm_name}')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

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

# Run DPLL tests and plot results (20% unsatisfiable cases)
dpll_results = run_dpll_tests(test_cases, force_unsat_ratio=0.2)
plot_results(dpll_results, "DPLL Algorithm")
