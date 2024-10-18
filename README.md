# Project01 Readme: Team Isabel_Phoebe_Pablo

## Team Information

- **Team Name**: Isabel_Phoebe_Pablo
- **Team Members**:
  - Phoebe Huang (chuang26)
  - Pablo Oliva Quintana (polivaqu)
  - Isabel Ojeda (iojeda)

## Project Overview: DumbSAT

1. **Sub-projects**:
   - Implementing a polynomial time 2-SAT solver (DPLL algorithm)
   - Incremental search through possible solutions
   - Unit clause propagation in the algorithm
   - Combining incremental search and unit clause propagation

2. **Success**: Successful in our opinion.

3. **Time Spent**: Approx. 12 hours per person over 5 days.

4. **GitHub Repository**: [TheoryProject1](https://github.com/iojeda1/TheoryProject1.git)

## Included Files

### Code Files

| File Name                                  | Description                                                                                      |
|--------------------------------------------|--------------------------------------------------------------------------------------------------|
| `DumbSAT_DPLL_Final_Isabel_Phoebe_Pablo.py`| Implements DPLL algorithm to check satisfiability of wff formulas.                                |
| `DumbSAT_IS_Isabel_Phoebe_Pablo.py`        | Implements incremental search to check satisfiability of wff formulas.                            |
| `DumbSAT_UnitClause_Isabel_Phoebe_Pablo.py`| Implements unit clause algorithm to check satisfiability of wff formulas.                         |

### Test Files

The following test cases are included in each code file as functions:

- `[[1, -2], [-1, 2]]`
- `[[1, 2], [-1, 2], [1, -2]]`
- `[[1, 2, 3], [-1, -2], [2, -3], [1, 2]]`
- `[[1, 2], [1, -2], [2, 3], [-1, 3], [-3, -2]]`
- `[[1], [-1]]`

### Output Files

| File Name                                  | Description                                                                                      |
|--------------------------------------------|--------------------------------------------------------------------------------------------------|
| `dpll_results_Isabel_Phoebe_Pablo.csv`     | Results from the DPLL algorithm. Contains wff formula, satisfiability, assignment, and execution time. |
| `incremental_results_Isabel_Phoebe_Pablo.csv` | Results from the incremental search algorithm.                                                    |
| `unit_results_Isabel_Phoebe_Pablo.csv`     | Results from the unit clause algorithm.                                                           |

### Plots

1. **Graph 1: DPLL Algorithm Performance**
   - This graph shows the performance of the DPLL algorithm in terms of execution time as the complexity of the wff formulas increases. It highlights how the algorithm handles both satisfiable and unsatisfiable cases.
   - ![Graph 1](https://github.com/your-username/your-repository/blob/main/graph1.png)

2. **Graph 2: Incremental Search Performance**
   - This graph illustrates the performance of the incremental search algorithm. It compares the execution times across different test cases, showcasing its volatility, particularly in larger, unsatisfiable problems.
   - ![Graph 2](https://github.com/your-username/your-repository/blob/main/graph2.png)

3. **Graph 3: Unit Clause Algorithm Performance**
   - This graph compares the efficiency of the unit clause algorithm in terms of time taken to solve satisfiable and unsatisfiable cases. It demonstrates the algorithm’s quick simplification of problems using unit propagation.
   - ![Graph 3](https://github.com/your-username/your-repository/blob/main/graph3.png)

## Programming Languages and Libraries

- **Language**: Python
- **Libraries**: `time`, `random`, `string`, `csv`

## Key Data Structures

1. **DPLL**: Sets and lists.
2. **Incremental Search**: Lists.
3. **Unit Clause**: Lists.

## General Operation of Code (for each subproject)

### Incremental Search
- The code begins with an initial truth assignment where each variable is randomly assigned either true or false. The algorithm checks if the current assignment satisfies all clauses in the wff formula. It iterates through each clause and checks if at least one clause in the literal evaluates to True. If the formula is not satisfied, the algorithm randomly flips the value of a single variable. This repeats for a max 2^Nvars number of attempts and ends when a satisfying assignment is found or after reaching the maximum number of attempts.

### Unit Clause Propagation
- The unit clause function searches for unit clauses in the formula. When a unit clause is found (clause with one literal), it forces the truth value of that literal (if it is positive, the variable is set to True; if it is negative, it is set to False). Once a literal truth value is determined by a unit clause, the formula is simplified by removing clauses containing the literal are removed (as they are satisfied) and clauses containing the negation of the literal have that negated literal removed (since it is falsified). The process repeats until no more unit clauses are found. After simplification, if the formula is still not fully solved, the check function iterates through all possible assignments for the remaining variables using brute force. The algorithm checks if a satisfying assignment exists, prints whether the formula is satisfiable or unsatisfiable, and displays the assignment of variables. 

### DPLL Algorithm
- If all clauses are satisfied with the current variable assignment, the solver returns the assignment as the solution. If any clause is empty, the solver returns unsatisfiable. Then, unit propagation is checked and implemented. If no unit clauses are found, the solver selects an unassigned literal and recursively tries to either assume that the literal is true, or backtrack and assume the literal is false. This checks all solutions until a satisfiable result is found or the formula is proven unsatisfiable. 


## Test Cases

We used the following test cases to validate correctness:

- `[[1, -2], [-1, 2]]`
- `[[1, 2], [-1, 2], [1, -2]]`
- `[[1, 2, 3], [-1, -2], [2, -3], [1, 2]]`
- `[[1, 2], [1, -2], [2, 3], [-1, 3], [-3, -2]]`
- `[[1], [-1]]`

We used these test cases because they range from simple 2-literal formulas to more complex 3-literal problems with a mix of positive and negative literals. We ran these problems by hand as well to check their correctness. The assignments can be different as there can be more than one satisfying assignment. The final case confirms that the solver can identify unsatisfiable problems. Together, these tests validate the correctness of the algorithm. All three codes give the same result, further showing they handle the formulas correctly. 


## Code Development

We split the projects between all of us, so each person did one. We did little by little every day and merged everything together once we knew our scripts worked with basic test cases. We then created graphing scripts to make sure our codes worked properly. In each script, we took advantage of the use of functions and python libraries to simplify the process. We also followed the professor’s DumbSAT code through our own development. The code development was rough, and some projects were harder than others, but we believe we were able to figure it out in the end as a team. Even though one person was in charge of each, we all helped each other when needed. 


## Results

- **Unit Clause SAT Solver**: emerges as the fastest and most efficient overall. Its use of unit propagation allows it to quickly simplify problems, leading to much lower execution times, especially for satisfiable cases, and it remains effective even as the problem size grows.
- **DPLL**: while a more sophisticated algorithm with backtracking, performs well for satisfiable instances but starts to show significant performance degradation with unsatisfiable cases as problem size increases, making it a good middle-ground solution. 
- **Incremental Search**: the slowest of the three, particularly for larger, unsatisfiable problems, due to its brute-force nature and lack of advanced pruning techniques. Incremental search is volatile, sometimes it performs very well and surpasses unit clauses on time, however other times it performs very badly.


## Team Organization

The team was organized in a way that implemented both individual work and team work. Each person took charge of one of the projects and dove into deeply understanding its prompt. When we needed help, we helped each other develop our code, as well as explain any theoretical parts when needed. When graphing, we did everything together and made sure to meet many days to keep each other updated on the process. 


## Reflection

We would have taken more time to read all of the instructions and understand what the problem we were trying to solve is. Sometimes, Computer Science students rush too much on getting started to code, however it is utterly important to understand what the algorithm is set to do, how it should be done, and ultimately for example, guidelines such as test cases, inputs, outputs, etc. 


## Additional Material: N/A
