# Problem 49: Minimum Height Trees

## Visualization
[View Interactive Visualization](./49-minimum-height-trees.html)

## Problem Statement
Given a tree with n nodes labeled 0 to n-1, find all roots that minimize the tree's height. Return a list of their labels.

## Layman's Explanation
Imagine you have a network of connected points, and you need to pick the best "center" to minimize how far you have to travel to reach the farthest point. The trick is to **peel off leaves layer by layer** - like peeling an onion. The nodes left at the center (1 or 2 nodes) are your minimum height tree roots.

## Step-by-Step Walkthrough
1. **Build Graph**: Create adjacency list from edges
2. **Find Initial Leaves**: Nodes with only one connection
3. **Peel Leaves**: Remove current leaves, update neighbor degrees
4. **New Leaves**: Neighbors that now have only one connection
5. **Repeat**: Continue until 1-2 nodes remain
6. **Result**: Remaining nodes are the roots of minimum height trees

## Visual Example
```
Initial:        After removing     Final:
    0              leaves:         
    |                              
    1-2-3          1-2             2
    |                              
    4                              

Leaves: [0, 3, 4]  Leaves: [1]    Root: [2]
```

## Code Snippet
```python
def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
    if n <= 1:
        return [0]

    # 양방향 그래프 구성
    graph = collections.defaultdict(list)
    for i, j in edges:
        graph[i].append(j)
        graph[j].append(i)

    # 첫 번째 리프 노드 추가
    leaves = []
    for i in range(n + 1):
        if len(graph[i]) == 1:
            leaves.append(i)

    # 루트 노드만 남을 때까지 반복 제거
    while n > 2:
        n -= len(leaves)
        new_leaves = []
        for leaf in leaves:
            neighbor = graph[leaf].pop()
            graph[neighbor].remove(leaf)
            if len(graph[neighbor]) == 1:
                new_leaves.append(neighbor)
        leaves = new_leaves

    return leaves
```

## Complexity Analysis
- **Time Complexity**: O(n) - each node processed once
- **Space Complexity**: O(n) - for the graph adjacency list
