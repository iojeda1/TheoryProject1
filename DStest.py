def backtrack_search(Wff, Assignment, Index):
    """
    Recursive backtracking SAT solver that checks for a satisfying assignment.
    
    :param Wff: The well-formed formula (list of clauses)
    :param Assignment: Current variable assignment (list of 0s or 1s)
    :param Index: The current index of the variable being assigned
    :return: True if a satisfying assignment is found, False otherwise
    """
    # If we've assigned all variables, check if the formula is satisfied
    if Index == len(Assignment):
        return inc_search(Wff, Assignment)
 
# Try assigning 0 (False) to the current variable
    Assignment[Index] = 0
    if backtrack_search(Wff, Assignment, Index + 1):
        return True
    
    # Try assigning 1 (True) to the current variable
    Assignment[Index] = 1
    if backtrack_search(Wff, Assignment, Index + 1):
        return True
    
    # If neither assignment works, backtrack
    return False

def inc_search(Wff, Assignment): 
    """
    Checks if the current assignment satisfies all clauses in the WFF.
    
    :param Wff: The well-formed formula (list of clauses)
    :param Assignment: Current variable assignment (list of 0s or 1s)
    :return: True if the assignment satisfies the WFF, False otherwise
    """
    for clause in Wff:
        satisfied = False
        for literal in clause:
            Index = abs(literal)
            # Check literal satisfaction
            if (literal < 0 and Assignment[Index] == 0): #or (literal > 0 and Assignment[Index] == 1):
                satisfied = True
                break
            elif (literal > 0 and Assignment[Index] == 1):
                satisfied = True
                break
        if not satisfied:
            return False
    return True

def test_case(Wff, Assignment):
    """
    Tests the satisfiability of a given WFF and prints the result.
    
    :param Wff: The well-formed formula (list of clauses)
    :param Assignment: Initial variable assignment (list of 0s or 1s)
    """
    result = backtrack_search(Wff, Assignment, 1)
    if result:
        print(f"Satisfiable: {Assignment[1:]}")  # Exclude the 0th index placeholder
    else:
        print("Unsatisfiable")

# Example test case
Wff2 = [[1, 2], [1, 3], [2, 3]]
Assignment2 = [0, 0, 0, 0]  # Assignment array with 0 as a placeholder at index 0

test_case(Wff2,Assignment2)