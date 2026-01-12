# ⚡ Data Structures & Algorithms in Python

> **A comprehensive collection of fundamental computer science algorithms implemented from scratch in Python.**
> This repository serves as a personal study guide for understanding algorithmic complexity, memory management, and graph theory.

## 📚 Overview
The goal of this project is to implement standard algorithms without relying on external "black-box" libraries. Each implementation focuses on code readability and strict adherence to the theoretical time complexities (Big-O).

## 🚀 Implemented Algorithms

### 1. Sorting Algorithms
- [x] **Insertion Sort** - $O(n^2)$
- [x] **Merge Sort** - $O(n \log n)$
- [x] **Quick Sort** - $O(n \log n)$
- [x] **Heap Sort** - $O(n \log n)$ (Implemented via Max-Heap)
- [ ] **Bucket Sort** *[Planned]*

### 2. Data Structures
- [x] **Linked Lists** (Singly/Doubly)
- [x] **Stacks & Queues** (FIFO/LIFO implementations)
- [x] **Binary Heaps** (Min/Max Heap, `build_max_heap`, `heapify`)
- [ ] **Binary Search Trees (BST)** *[Planned]*
- [ ] **Disjoint Set Union (Union-Find)** *[Planned]*

### 3. Graph Traversal & Search
- [x] **Breadth-First Search (BFS)** - Shortest path in unweighted graphs.
- [x] **Depth-First Search (DFS)** - Exhaustive search / Cycle detection.
- [x] **Topological Sort** - (Using DFS for DAGs).

### 4. Shortest Path Algorithms (Weighted Graphs)
- [x] **Dijkstra's Algorithm** - $O(E + V \log V)$ using Priority Queue.
- [x] **Bellman-Ford Algorithm** - Handles negative weights.
- [x] **Floyd-Warshall Algorithm** - All-pairs shortest paths ($O(V^3)$).

### 5. Minimum Spanning Trees (MST)
- [x] **Prim's Algorithm**
- [ ] **Kruskal's Algorithm** *[Planned]*

### 6. Network Flow
- [x] **Ford-Fulkerson Method**
- [x] **Edmonds-Karp Algorithm** (BFS implementation of Ford-Fulkerson).

### 7. Advanced Concepts
- [ ] **Dynamic Programming** (Knapsack, LCS) *[Planned]*
- [ ] **Greedy Algorithms** (Huffman Coding) *[Planned]*
