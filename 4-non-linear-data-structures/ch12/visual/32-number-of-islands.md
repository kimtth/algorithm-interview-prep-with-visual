# Q32: Number of Islands

## Problem Description
Given a 2D grid of ''1''s (land) and ''0''s (water), count the number of islands. An island is surrounded by water and formed by connecting adjacent lands horizontally or vertically.

## Core Idea: DFS Flood Fill
**Approach:** For each unvisited land cell, perform DFS to mark all connected land as visited. Count how many times DFS is initiated.

## How It Works (Layman''s Terms)

Imagine: **Painting Connected Land**
- Walk through the grid cell by cell
- When you find unpainted land (''1''), start painting
- Paint spreads to all connected land cells (up, down, left, right)
- Count how many times you started painting = number of islands

Example:
```
11110      XXXXX
11010  →   XXX1X  →  Island count: 1
11000      XX000
00000      00000
```

## Visualization

👉 [Interactive Visualization (HTML)](./32-number-of-islands.html)

## Core Code Logic

```python
def numIslands(grid: List[List[str]]) -> int:
    def dfs(i, j):
        # Out of bounds or water
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return
        if grid[i][j] != ''1'':
            return

        grid[i][j] = ''0''  # Mark as visited
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == ''1'':
                dfs(i, j)
                count += 1
    return count
```

## Complexity

- **Time:** O(m × n) - visit each cell once
- **Space:** O(m × n) - recursion stack in worst case

## Key Takeaways

1. **Flood fill pattern** - mark visited to avoid revisiting
2. **4-directional neighbors** - up, down, left, right
3. **Can use BFS instead** - iterative with queue
