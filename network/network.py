def critical_place_count(graph):
    """
    For the adjacency list 'graph' return the amount of critical places.
    """

    def helper(u, visited, ap, parent, low, disc, timer):
        # Find critical point using DFS traversal
        # Count of children in current node
        children = 0

        # Mark the current node as visited
        visited[u] = True

        # Initialize discovery time and low value
        disc[u] = timer
        low[u] = timer
        timer += 1

        # Recur for all the vertices adjacent to this vertex
        for v in graph[u]:
            # If v is not visited yet, then make it a child of u
            # in DFS tree and recur for it
            if visited[v] == False:
                parent[v] = u
                children += 1
                helper(v, visited, ap, parent, low, disc, timer)

                # Check if the subtree rooted with v has a connection to
                # one of the ancestors of u
                low[u] = min(low[u], low[v])

                # u is an articulation point in following cases
                # (1) u is root of DFS tree and has two or more chilren.
                if parent[u] == -1 and children > 1:
                    ap[u] = True

                # (2) If u is not root and low value of one of its child is more
                # than discovery value of u.
                if parent[u] != -1 and low[v] >= disc[u]:
                    ap[u] = True

                    # Update low value of u for parent function calls
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

    #Initialization
    visited = [False] * len(graph)
    disc = [float("Inf")] * len(graph)
    low = [float("Inf")] * len(graph)
    parent = [-1] * len(graph)
    ap = [False] * len(graph)
    timer = 0

    for i, val in enumerate(graph):
        if visited[i] == False:
            helper(i, visited, ap, parent, low, disc, timer)

    critical = 0
    for index, val in enumerate(ap):
        if val == True:
            critical+=1
    return critical


