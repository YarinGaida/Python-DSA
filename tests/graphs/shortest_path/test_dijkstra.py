from src.graphs.shortest_path.dijkstra import dijkstra_formal

def test_dijkstra():
    print("\n--- Testing Dijkstra's Algorithm ---")
    
    # Weighted Graph representation:
    # 'Node': [('Neighbor', Weight), ...]
    weighted_graph = {
        'A': [('B', 4), ('C', 2)],      # A מחובר ל-B (משקל 4) ול-C (משקל 2)
        'B': [('C', 5), ('D', 10)],     
        'C': [('E', 3)],                
        'D': [('F', 11)],
        'E': [('D', 4)],                # הדרך הקצרה ל-D תעבור דרך כאן!
        'F': []
    }
    
    # We expect the path A -> C -> E -> D
    # Cost calculation:
    # A->C = 2
    # C->E = 3 (Total 5)
    # E->D = 4 (Total 9)
    # (Direct path A->B->D would be 4+10 = 14, which is worse)

    distances = dijkstra_formal(weighted_graph, s='A')
    
    print("\nFinal Distances (lambda):", distances)
    
    assert distances['D'] == 9
    assert distances['C'] == 2
    assert distances['A'] == 0
    
    print("Test Passed: Shortest paths calculated correctly.")

if __name__ == "__main__":
    test_dijkstra()