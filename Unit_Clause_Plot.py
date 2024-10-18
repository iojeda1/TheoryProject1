import random
import time
import matplotlib.pyplot as plt

# Unit clause simplification function
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
                # modify wff by implementing unit clause rules
                Wff2 = []
                for clause2 in Wff:
                    if literal in clause2: # skip clauses with literal
                        continue
                    elif -literal in clause2: # if -literal, do not append it to our new wff
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

# Check satisfiability
def check(Wff, Nvars, Nclauses, Assignment):
    Satisfiable, Assignment, Wff = unit_clause(Wff, Assignment)
    if not Satisfiable: return False
    if not Wff: return True

    Satisfiable=False
    while (Assignment[Nvars+1]==0):
        for i in range(0, Nclauses):
            Clause = Wff[i]
            Satisfiable=False
            for j in range(0, len(Clause)):
                Literal = Clause[j]
                if Literal > 0: Lit = 1
                else: Lit = 0
                VarValue = Assignment[abs(Literal)]
                if Lit == VarValue:
                    Satisfiable=True
                    break
            if Satisfiable == False: break
        if Satisfiable == True: break
        for i in range(1, Nvars+2):
            if Assignment[i] == 0:
                Assignment[i] = 1
                break
            else:
                Assignment[i] = 0
    return Satisfiable

# Function to build a wff
def build_wff(Nvars, Nclauses, LitsPerClause):
    wff = []
    for i in range(1, Nclauses+1):
        clause = []
        for j in range(1, LitsPerClause+1):
            var = random.randint(1, Nvars)
            if random.randint(0, 1) == 0: var = -var
            clause.append(var)
        wff.append(clause)
    return wff

# Test a single wff
def test_wff(wff, Nvars, Nclauses):
    Assignment = list((0 for x in range(Nvars+2)))
    start = time.time()
    SatFlag = check(wff, Nvars, Nclauses, Assignment)
    end = time.time()
    exec_time = int((end-start)*1e6)
    return exec_time, SatFlag


def run_tests(test_cases):
    results = []
    for case in test_cases:
        Nvars, Nclauses, LitsPerClause, Ntrials = case
        for _ in range(Ntrials):
            wff = build_wff(Nvars, Nclauses, LitsPerClause)
            exec_time, SatFlag = test_wff(wff, Nvars, Nclauses)
            results.append((Nvars * Nclauses, exec_time, SatFlag))
    return results

# Plot the results
def plot_results(results):
    x_yes = [r[0] for r in results if r[2]]  #Satisfiable
    y_yes = [r[1] for r in results if r[2]]
    x_no = [r[0] for r in results if not r[2]]  #Unsatisfiable
    y_no = [r[1] for r in results if not r[2]]

    plt.scatter(x_yes, y_yes, color='green', marker='o', label='Satisfiable')
    plt.scatter(x_no, y_no, color='red', marker='x', label='Unsatisfiable')

    plt.xlabel('Problem Size (Nvars * Nclauses)')
    plt.ylabel('Execution Time (µs)')
    plt.title('Problem Size vs Execution Time for SAT Solver')
    plt.legend()
    plt.show()

test_cases = [
    (2, 4, 2, 10),
    (3, 6, 2, 10),
    (4, 8, 2, 10),
    (5, 10, 2, 10),
    (6, 12, 2, 10),
    (7, 14, 2, 10),
    (8, 16, 2, 10),
    (9, 18, 2, 10),
    (10, 20, 2, 10),
    (11, 22, 2, 10),
    (12, 24, 2, 10),
    (13, 26, 2, 10),
    (14, 28, 2, 10),
    (15, 30, 2, 10)
]

results_filled = run_tests(test_cases)
plot_results(results_filled)