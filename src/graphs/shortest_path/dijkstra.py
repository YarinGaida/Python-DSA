def dijkstra_formal(graph, s):
    """
    Args:
        graph (dict): Weighted adjacency list. { 'u': [('v', weight), ...] }
        s (str): Start node.
        
    Variables from algorithm:
    lambda_val (dict): Current shortest distance from s (𝜆).
    T (set): Temporarily labeled nodes (𝓣).
    P (set): Permanently labeled nodes (𝓟).
    """

    # --- Initialization ---
    # ∀v ∈ V 𝜆(v) = ∞ ; 𝜆(s) = 0
    lambda_val = {v: float('inf') for v in graph}
    lambda_val[s] = 0

    # 𝓣 = {s} ; 𝓟 = ∅
    T = {s}
    P = set()

    print(f"--- Starting Dijkstra from {s} ---")

    # --- Main Loop ---
    # while 𝓣 ≠ ∅
    while T:
        # get v ∈ 𝓣 s.t. 𝜆(v) is minimum
        # (Finding the node with the smallest distance in the temporary set)
        v = min(T, key=lambda node: lambda_val[node])
        
        # 𝓣 = 𝓣 \ {v} ; 𝓟 = 𝓟 ∪ {v}
        # Change v from temp to permanent
        T.remove(v)
        P.add(v)
        
        print(f"Permanent Node: {v}, Distance: {lambda_val[v]}")

        # ∀e(v,u) do (Iterate over neighbors)
        # Note: In our graph structure, neighbors are (u, weight) tuples
        for u, weight in graph.get(v, []):
            
            # if u ∈ 𝓣 (u already labeled, minimize label)
            if u in T:
                # 𝜆(u) = min(𝜆(u), 𝜆(v) + w(e))
                new_dist = lambda_val[v] + weight
                if new_dist < lambda_val[u]:
                    lambda_val[u] = new_dist
            
            # else if u ∉ 𝓟 (u first time labeled)
            elif u not in P:
                # 𝜆(u) = 𝜆(v) + w(e) ; 𝓣 = 𝓣 ∪ {u}
                lambda_val[u] = lambda_val[v] + weight
                T.add(u)

    print("--- Dijkstra Complete ---")
    return lambda_val