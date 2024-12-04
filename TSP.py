def solve_tsp(G):
    """
    This function is a greedy implementation of the traveling salesperson problem where
    the next city to visit is always the nearest unvisited neighbor.
    """
    # Initialize
    number_of_cities = len(G)
    # Will start as false since no cities have been visited
    cities_already_visited = [False] * number_of_cities
    travel_path = []
    current_city = 0 # Starts from the first node

    # Begin with starting city
    travel_path.append(current_city)
    cities_already_visited[current_city] = True

    # Iteration to visit cities
    # exclude the city we're starting from
    for visit in range(number_of_cities - 1):
        closest_neighboring_city = None
        # Initialize with infinity
        closest_city_distance = float('inf')
        # implement loop to find the nearest neighbor
        for closest_neighboring_city in range(number_of_cities):
            # Requirement 1: Edge exists and has not been visited
            if not cities_already_visited[closest_neighboring_city] and G[current_city][closest_neighboring_city] > 0:




    return