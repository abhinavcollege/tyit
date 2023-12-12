#Solve constraint satisfaction problem
from simpleai.search import CspProblem, backtrack, min_conflicts

# Define the Map Coloring CSP
def map_coloring_constraint(variables, values):
    # Check if adjacent regions have different colors
    return values[0] != values[1]

# Define the variables (regions) and their domains (possible colors)
variables = ('WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T')
domains = dict((v, ['red', 'green', 'blue']) for v in variables)

# Define the constraints (adjacent regions must have different colors)
constraints = [
    (('WA', 'NT'), map_coloring_constraint),
    (('WA', 'SA'), map_coloring_constraint),
    (('SA', 'NT'), map_coloring_constraint),
    (('SA', 'Q'), map_coloring_constraint),
    (('NT', 'Q'), map_coloring_constraint),
    (('SA', 'NSW'), map_coloring_constraint),
    (('Q', 'NSW'), map_coloring_constraint),
    (('SA', 'V'), map_coloring_constraint),
    (('NSW', 'V'), map_coloring_constraint),
]

# Create a CSP problem instance
map_coloring_problem = CspProblem(variables, domains, constraints)

# Solve the CSP using Backtracking
result_backtrack = backtrack(map_coloring_problem)
print("Solution using Backtracking:", result_backtrack)

# Solve the CSP using Min Conflicts
result_min_conflicts = min_conflicts(map_coloring_problem, iterations_limit=100)
print("Solution using Min Conflicts:", result_min_conflicts)
