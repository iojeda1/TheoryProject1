def backtrack_search(Wff, Assignment, Index):
   
    if Index == len(Assignment):
        return inc_search(Wff, Assignment)
 
    Assignment[Index] = 0
    if backtrack_search(Wff, Assignment, Index + 1):
        return True
    
    Assignment[Index] = 1
    if backtrack_search(Wff, Assignment, Index + 1):
        return True

    return False

def inc_search(Wff, Assignment): 
   
    for clause in Wff:
        satisfied = False
        for literal in clause:
            Index = abs(literal)
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
    result = backtrack_search(Wff, Assignment, 1)
    if result:
        print(f"Satisfiable: {Assignment[1:]}")  
    else:
        print("Unsatisfiable")
Wff2 = [[1, 2], [1, 3], [2, 3]]
Assignment2 = [0, 0, 0, 0]  # Assignment array with 0 as a placeholder at index 0

test_case(Wff2,Assignment2)
