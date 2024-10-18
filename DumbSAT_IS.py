import time
import random
import csv

# Incremental SAT solver
def incremental(Wff, Nvars, Nclauses, Assignment):
    satisfiable = False
    attempts = 0 
    max_attempts = 2**Nvars  # 2^N max attempts
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


def test_cases(num):
    if num == 1:
        wff = [[1, -2], [-1, 2]]
        Nvars = 2
        Nclauses = 2
        return wff, Nvars, Nclauses
    elif num == 2:
        wff = [[1, 2], [-1, 2], [1, -2]]
        Nvars = 2
        Nclauses = 3
        return wff, Nvars, Nclauses
    elif num == 3:
        wff = [[1, 2, 3], [-1, -2], [2, -3], [1, 2]]
        Nvars = 3
        Nclauses = 3
        return wff, Nvars, Nclauses
    elif num == 4:
        wff = [[1, 2], [1, -2], [2, 3], [-1, 3], [-3, -2]]
        Nvars = 3
        Nclauses = 5
        return wff, Nvars, Nclauses
    elif num == 5:
        wff = [[1], [-1]]
        Nvars = 1
        Nclauses = 2
        return wff, Nvars, Nclauses

def run_incremental_test(num):
    wff, Nvars, Nclauses = test_cases(num)
    Assignment = [random.randint(0, 1) for _ in range(Nvars + 1)]  # Random initial assignment
    start_time = time.time()
    satisfiable, final_assignment = incremental(wff, Nvars, Nclauses, Assignment)
    exec_time = int((time.time() - start_time) * 1e6)  # Execution time in microseconds
    sat_result = "Satisfiable" if satisfiable else "Unsatisfiable"
    
    return {
        "Test Case": num,
        "WFF": wff,
        "SAT Result": sat_result,
        "Assignment": final_assignment[1:],  # Omit the 0th element (index 0 isn't used)
        "Execution Time (microseconds)": exec_time
    }

def run_incremental_tests():
    results = []
    start_time = time.time()  # Start timer for total execution time
    for num in range(1, 6):  # Running 5 test cases
        result = run_incremental_test(num)
        results.append(result)
    total_exec_time = int((time.time() - start_time) * 1e6)  # Total execution time in microseconds
    return results, total_exec_time

# Run Incremental SAT tests and capture the results
results, total_exec_time = run_incremental_tests()

# Now write results to CSV
with open('incremental_results.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Test Case", "WFF", "SAT Result", "Assignment", "Execution Time (microseconds)"])  # Write header
    for result in results:
        writer.writerow([result["Test Case"], result["WFF"], result["SAT Result"], result["Assignment"], result["Execution Time (microseconds)"]])
    
    # Add total execution time as the final row
    writer.writerow(["Total", "N/A", "N/A", "N/A", total_exec_time])

# Print confirmation
print(f"Incremental Search Results Successfully Written into 'incremental_results.csv', including Total Execution Time: {total_exec_time} microseconds")
