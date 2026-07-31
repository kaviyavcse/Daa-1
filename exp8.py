import heapq

INF = float('inf')

class Node:
    """Class representing a state space tree node in Branch and Bound."""
    def __init__(self, parent_matrix, path, level, i, j, cost):
        self.path = list(path)
        if level != 0:
            self.path.append(j)
        
        self.level = level
        self.vertex = j
        self.cost = cost
        
        # Copy parent matrix
        n = len(parent_matrix)
        self.matrix = [row[:] for row in parent_matrix]
        
        # Change rows and columns to INF for visited edges
        if level != 0:
            # Set row i and col j to INF
            for k in range(n):
                self.matrix[i][k] = INF
                self.matrix[k][j] = INF
            # Set reverse edge to INF to avoid early returning
            self.matrix[j][0] = INF

    def __lt__(self, other):
        # Priority Queue orders nodes by lower bound (cost)
        return self.cost < other.cost


def reduce_matrix(mat):
    """
    Reduces rows and columns of a matrix and returns total reduction cost.
    """
    n = len(mat)
    cost = 0
    m = [row[:] for row in mat]

    # Row reduction
    for i in range(n):
        row_min = min(m[i])
        if row_min != INF and row_min > 0:
            cost += row_min
            m[i] = [x - row_min if x != INF else INF for x in m[i]]

    # Column reduction
    for j in range(n):
        col_min = min(m[i][j] for i in range(n))
        if col_min != INF and col_min > 0:
            cost += col_min
            for i in range(n):
                if m[i][j] != INF:
                    m[i][j] -= col_min

    return m, cost


def tsp_branch_and_bound(cost_matrix, n):
    """
    Solves TSP using Least Cost Branch and Bound (LCBB).
    """
    pq = []

    # Reduce initial cost matrix
    initial_matrix, initial_cost = reduce_matrix(cost_matrix)

    # Root state (start at city 0)
    root = Node(initial_matrix, [0], 0, -1, 0, initial_cost)
    heapq.heappush(pq, root)

    best_cost = INF
    best_path = []

    while pq:
        # Extract node with smallest cost bound
        curr = heapq.heappop(pq)

        # Prune if cost bound exceeds best known complete cost
        if curr.cost >= best_cost:
            continue

        # If all cities visited, add return path to starting city (0)
        if curr.level == n - 1:
            curr.path.append(0)
            if curr.cost < best_cost:
                best_cost = curr.cost
                best_path = curr.path
            continue

        # Branching to unvisited cities
        for child_city in range(n):
            if curr.matrix[curr.vertex][child_city] != INF:
                # Reduce child's matrix
                child_matrix, child_red_cost = reduce_matrix(curr.matrix)
                
                # Total cost for child node
                node_cost = (
                    curr.cost 
                    + curr.matrix[curr.vertex][child_city] 
                    + child_red_cost
                )

                if node_cost < best_cost:
                    child_node = Node(
                        curr.matrix, 
                        curr.path, 
                        curr.level + 1, 
                        curr.vertex, 
                        child_city, 
                        node_cost
                    )
                    # Pass the reduced matrix to child
                    child_node.matrix, _ = reduce_matrix(child_node.matrix)
                    heapq.heappush(pq, child_node)

    return best_path, best_cost


# --- Program Execution ---
if __name__ == "__main__":
    # 5-city cost matrix
    cost = [
        [INF, 10,  8,  9,  7],
        [ 10, INF, 10,  5,  6],
        [  8, 10, INF,  8,  9],
        [  9,  5,  8, INF,  6],
        [  7,  6,  9,  6, INF]
    ]
    
    n = len(cost)
    cities = ['A', 'B', 'C', 'D', 'E']

    # Display Cost Matrix
    print("5-City TSP - Cost Matrix:")
    print(f'{"":>4}', ' '.join(f'{c:>5}' for c in cities))
    for i, row in enumerate(cost):
        r = ['INF' if x == INF else str(x) for x in row]
        print(f'{cities[i]:>4}', ' '.join(f'{v:>5}' for v in r))

    # Solve using Branch and Bound
    best_path, best_cost = tsp_branch_and_bound(cost, n)

    # Output Results
    print(f'\nOptimal Tour: {" -> ".join(cities[i] for i in best_path)}')
    print(f'Minimum Cost: {best_cost}')
    
    print(f'\nPath verification:')
    for i in range(n):
        u, v = best_path[i], best_path[i+1]
        print(f'  {cities[u]} -> {cities[v]}: cost = {cost[u][v]}')
