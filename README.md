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

| File/Folder Name         | Description                                                                                      |
|--------------------------|--------------------------------------------------------------------------------------------------|
| `DumbSAT_DPLL_Final_Isabel_Phoebe_Pablo.py`   | Implements DPLL algorithm to check satisfiability of wff formulas.                               |
| `DumbSAT_IS_Isabel_Phoebe_Pablo.py`           | Implements incremental search to check satisfiability of wff formulas.                           |
| `DumbSAT_UnitClause_Isabel_Phoebe_Pablo.py`   | Implements unit clause algorithm to check satisfiability of wff formulas.                        |
| `dpll_results_Isabel_Phoebe_Pablo.csv`        | Contains results for DPLL algorithm tests.                                                       |
| `incremental_results_Isabel_Phoebe_Pablo.csv` | Contains results for incremental search algorithm tests.                                         |
| `unit_results_Isabel_Phoebe_Pablo.csv`        | Contains results for unit clause algorithm tests.                                                |

## Programming Languages and Libraries

- **Language**: Python
- **Libraries**: `time`, `random`, `string`, `csv`

## Key Data Structures

1. **DPLL**: Sets and lists.
2. **Incremental Search**: Lists.
3. **Unit Clause**: Lists.

## Code Operation

### Incremental Search
- Randomly assigns truth values to variables, checks if the formula is satisfied, and flips variables if necessary. Repeats until a solution is found or a set number of attempts is reached.

### Unit Clause Propagation
- Identifies unit clauses and forces truth values. Simplifies the formula by removing satisfied clauses and handling negated literals. Brute force is used for any remaining variables.

### DPLL Algorithm
- Uses recursive backtracking with unit propagation to check satisfiability. If all clauses are satisfied, the solution is returned.

## Test Cases

We used the following test cases to validate correctness:

- `[[1, -2], [-1, 2]]`
- `[[1, 2], [-1, 2], [1, -2]]`
- `[[1, 2, 3], [-1, -2], [2, -3], [1, 2]]`
- `[[1, 2], [1, -2], [2, 3], [-1, 3], [-3, -2]]`
- `[[1], [-1]]`

These cases cover simple 2-literal formulas and more complex 3-literal problems with a mix of positive and negative literals. The tests confirmed that our algorithms correctly handle satisfiability and unsatisfiability.

## Code Development

We split the project evenly:
- Each member worked on one sub-project.
- We collaborated during testing and graphing, ensuring consistency and correctness.

## Results

- **Unit Clause SAT Solver**: Fastest and most efficient, especially for larger, satisfiable cases.
- **DPLL**: Good middle-ground performance but slows for unsatisfiable cases.
- **Incremental Search**: Most volatile, performing well in some cases but poorly in others.

## Team Organization

Each team member focused on one sub-project but helped one another as needed. We collaborated for graphing and final testing.

## Reflection

If we did this again, we would spend more time understanding the problem and test case guidelines before starting to code.

## Additional Material: N/A
