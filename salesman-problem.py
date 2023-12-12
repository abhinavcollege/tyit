#Solve traveling salesman problem using artificial intelligence technique.
from simpleai.search import SearchProblem, astar

# Define the Traveling Salesman Problem as a search problem
class TSP(SearchProblem):
    def __init__(self, cities, distances):
        self.cities = cities
        self.distances = distances
        super(TSP, self).__init__(initial_state=(cities[0],))

    def actions(self, state):
        return [city for city in self.cities if city not in state]

    def result(self, state, action):
        return state + (action,)

    def cost(self, state, action, state2):
        return self.distances[state[-1]][action]

    def is_goal(self, state):
        return len(state) == len(self.cities) and state[0] == state[-1]

# Example cities and distances (you can modify this according to your problem)
cities = ['A', 'B', 'C', 'D']
distances = {
    'A': {'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30},
}

# Create a TSP problem instance
tsp_problem = TSP(cities, distances)

# Solve the TSP using A* search
result = astar(tsp_problem)

# Display the result
if result:
    print("Optimal Path:", result.state)
    print("Optimal Cost:", result.cost)
else:
    print("No solution found.")
