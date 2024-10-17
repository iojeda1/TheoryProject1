import random
import time
import matplotlib.pyplot as plt

# Incremental SAT solver
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
        # make small flips to generate more combinations
        flip = random.randint(1, Nvars)
        Assignment[flip] = 1 - Assignment[flip]
        attempts += 1
    return False, Assignment

# Function to build random Wff
def build_wff(Nvars, Nclauses, LitsPerClause):
    wff = []
    for i in range(1, Nclauses + 1):
        clause = []
        for j in range(1, LitsPerClause + 1):
            var = random.randint(1, Nvars)
            if random.randint(0, 1) == 0:
                var = -var
            clause.append(var)
        wff.append(clause)
    return wff

def test_wff(wff, Nvars, Nclauses):
    Assignment = [random.randint(0, 1) for x in range(Nvars + 1)]
    start = time.time()  # Start timer
    SatFlag, final_assignment = incremental(wff, Nvars, Nclauses, Assignment)
    end = time.time()  # End timer
    exec_time = int((end - start) * 1e6)  
    return exec_time, SatFlag

# Function to run multiple test cases and collect results
def run_tests(test_cases):
    results = []
    for case in test_cases:
        Nvars, Nclauses, LitsPerClause, Ntrials = case
        for _ in range(Ntrials):
            wff = build_wff(Nvars, Nclauses, LitsPerClause)
            exec_time, SatFlag = test_wff(wff, Nvars, Nclauses)
            results.append((Nvars * Nclauses, exec_time, SatFlag))
    return results

def plot_results(results):
    x_yes = [r[0] for r in results if r[2]]  # Satisfiable instances
    y_yes = [r[1] for r in results if r[2]]
    x_no = [r[0] for r in results if not r[2]]  # Unsatisfiable instances
    y_no = [r[1] for r in results if not r[2]]

    plt.figure(figsize=(10, 6)) 
    plt.scatter(x_yes, y_yes, color='green', marker='o', label='Satisfiable')
    plt.scatter(x_no, y_no, color='red', marker='x', label='Unsatisfiable')

    plt.xlabel('Problem Size (Nvars * Nclauses)')
    plt.ylabel('Execution Time (µs)')
    plt.title('Problem Size vs Execution Time for Incremental SAT Solver')
    plt.legend()

    plt.grid(True)  
    plt.tight_layout()  
    plt.show() 

test_cases = [
    (4, 10, 2, 10),
    (8, 16, 2, 10),
    (12, 24, 2, 10),
    (16, 32, 2, 10),
    (20, 40, 2, 10),
    (24, 48, 2, 10),
    (28, 56, 2, 10)
]
results = run_tests(test_cases)
plot_results(results)