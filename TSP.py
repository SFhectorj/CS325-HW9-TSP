def solve_tsp(G):
    """
    This function is a greedy implementation of the traveling salesperson problem where
    the next city to visit is always the nearest unvisited neighbor.
    """
    # Initialize
    number_of_cities = len(G)
    cities_already_visited =
    travel_path = []
    current_city = 0 # Starts from the first node

    # Begin with starting city
    travel_path.append(current_city)
    cities_already_visited[current_city] = True


    return