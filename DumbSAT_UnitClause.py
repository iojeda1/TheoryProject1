# Unit Clause 
# Theory of Computing Project01
# Isabel Ojeda, Phoebe Huang, Pablo Oliva Quintana 

import time
import random
import string
import csv

def unit_clause(Wff,Assignment): 
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

def check(Wff,Nvars,Nclauses,Assignment):
# Run thru all possibilities for assignments to wff
# Starting at a given Assignment (typically array of Nvars+1 0's)
# At each iteration the assignment is "incremented" to next possible
# At the 2^Nvars+1'st iteration, stop - tried all assignments

    # call unit clause function to simplify before doing brute force solution
    Satisfiable, Assignment, Wff = unit_clause(Wff, Assignment)
    if not Satisfiable: return False 
    if not Wff: return True 
    Satisfiable=False
    while (Assignment[Nvars+1]==0):
        # Iterate thru clauses, quit if not satisfiable
        for i in range(0,Nclauses): #Check i'th clause
            Clause=Wff[i]
            Satisfiable=False
            for j in range(0,len(Clause)): # check each literal
                Literal=Clause[j]
                if Literal>0: Lit=1
                else: Lit=0
                VarValue=Assignment[abs(Literal)] # look up literal's value
                if Lit==VarValue:
                    Satisfiable=True
                    break
            if Satisfiable==False: break
        if Satisfiable==True: break # exit if found a satisfying assignment
        # Last try did not satisfy; generate next assignment)
        for i in range(1,Nvars+2):
            if Assignment[i]==0:
                Assignment[i]=1
                break
            else: Assignment[i]=0
    return Satisfiable
    
def build_wff(Nvars,Nclauses,LitsPerClause):
    wff=[]
    for i in range(1,Nclauses+1):
        clause=[]
        for j in range(1,LitsPerClause+1):
            var=random.randint(1,Nvars)
            if random.randint(0,1)==0: var=-var
            clause.append(var)
        wff.append(clause)
    return wff

def test_cases(num):
    if num == 1:
        # Test Case 1: (x1 OR NOT x2) AND (NOT x1 OR x2)
        # Expected: Satisfiable, e.g., x1 = True, x2 = True
        wff = [[1, -2], [-1, 2]]
        Nvars = 2
        Nclauses = 2
        return wff, Nvars, Nclauses
    elif num == 2:
        # Test Case 2: (x1 OR x2) AND (NOT x1 OR x2) AND (x1 OR NOT x2)
        # Expected: Satisfiable
        wff = [[1, 2], [-1, 2], [1, -2]]
        Nvars = 2
        Nclauses = 3
        return wff, Nvars, Nclauses
    elif num == 3:
        # Test Case 3: (x1 OR x2 OR x3) AND (NOT x1 OR NOT x2) AND (x2 OR NOT x3) AND (x1 OR x2)
        # Expected: Satisfiable
        wff = [[1, 2, 3], [-1, -2], [2, -3], [1,2]]
        Nvars = 3
        Nclauses = 3
        return wff, Nvars, Nclauses
    elif num == 4:
        # Test Case 4: (x1 OR x2) AND (x1 OR NOT x2) AND (x2 OR x3) AND (NOT x1 OR x3) AND (NOT x3 OR NOT x2)
        # Expected: Satisfiable 
        wff = [[1, 2], [1, -2], [2, 3], [-1, 3], [-3, -2]]
        Nvars = 3
        Nclauses = 5
        return wff, Nvars, Nclauses
    elif num == 5:
        wff = [[1], [-1]]
        Nvars = 1
        Nclauses = 2
        return wff, Nvars, Nclauses


def test_wff(num):
    wff, Nvars, Nclauses = test_cases(num)
    Assignment = list((0 for x in range(Nvars+2)))
    start = time.time()  # Start timer
    SatFlag = check(wff, Nvars, Nclauses, Assignment)
    end = time.time()  # End timer
    exec_time = int((end - start) * 1e6)  # Convert to microseconds
    
    result = {
        "Test Case": num,
        "WFF": wff,
        "SAT Result": 'Satisfiable' if SatFlag else 'Unsatisfiable',
        "Assignment": Assignment[1:Nvars+1] if SatFlag else 'N/A',
        "Execution Time (microseconds)": exec_time
    }
    
    return result

def run_cases():
    results = []
    start = time.time()  # Start timer
    for num in range(1, 6):
        result = test_wff(num)
        results.append(result)  # Append result for each test case
    end = time.time()  # End timer
    exec_time = int((end - start) * 1e6)
    
    return results, exec_time

# Run test cases and save results to a CSV file
results, total_exec_time = run_cases()

# Now write results to CSV
with open('unit.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Test Case", "WFF", "SAT Result", "Assignment", "Execution Time (microseconds)"])  # Write header
    for result in results:
        writer.writerow([result["Test Case"], result["WFF"], result["SAT Result"], result["Assignment"], result["Execution Time (microseconds)"]])

# Optional: print total execution time
print("Results succesfully written into unit.csv")

