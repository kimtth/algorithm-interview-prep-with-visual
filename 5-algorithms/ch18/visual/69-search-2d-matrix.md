# 69. Search a 2D Matrix II

## Problem Description
Search for a target value in an m x n matrix where:
- Each row is sorted in ascending order (left to right)
- Each column is sorted in ascending order (top to bottom)

## Layman's Explanation
Imagine a chess-like grid where numbers increase as you go right AND as you go down. You're looking for a specific number.

**The Trick: Start from the Top-Right Corner!**

Why top-right? Because it's a "decision point":
- If target is **smaller** → Go LEFT (can't go right, numbers get bigger)
- If target is **bigger** → Go DOWN (can't go left, numbers get smaller)

It's like navigating a maze where at each step you can confidently eliminate a whole row or column!

**Alternative starting point:** Bottom-left corner (same logic, reversed directions)

## Algorithm Walkthrough
Given matrix:
```
[1,   4,  7, 11, 15]
[2,   5,  8, 12, 19]
[3,   6,  9, 16, 22]
[10, 13, 14, 17, 24]
[18, 21, 23, 26, 30]
```
Target: `5`

**Start at top-right: (0, 4) = 15**

**Step 1:** Position (0, 4), value = 15
- 15 > 5 → target is smaller, go LEFT
- Move to (0, 3)

**Step 2:** Position (0, 3), value = 11
- 11 > 5 → target is smaller, go LEFT
- Move to (0, 2)

**Step 3:** Position (0, 2), value = 7
- 7 > 5 → target is smaller, go LEFT
- Move to (0, 1)

**Step 4:** Position (0, 1), value = 4
- 4 < 5 → target is bigger, go DOWN
- Move to (1, 1)

**Step 5:** Position (1, 1), value = 5
- 5 == 5 → **FOUND!**

## Code Explanation
```python
def searchMatrix(self, matrix, target):
    if not matrix:
        return False
    
    # Start from top-right corner
    row = 0
    col = len(matrix[0]) - 1
    
    while row <= len(matrix) - 1 and col >= 0:
        if target == matrix[row][col]:
            return True
        elif target < matrix[row][col]:
            # Target is smaller, go left
            col -= 1
        else:  # target > matrix[row][col]
            # Target is bigger, go down
            row += 1
    
    return False
```

## Complexity Analysis
- **Time Complexity:** O(m + n) - At most m + n steps (each step eliminates a row or column)
- **Space Complexity:** O(1) - Only two variables for position

## Key Insights
1. **Corner Strategy:** Top-right or bottom-left corners are "decision points"
2. **Elimination:** Each comparison eliminates an entire row or column
3. **Why not top-left?** From top-left, both right and down increase - no clear direction!
4. **Why not binary search?** Would be O(m log n), but this O(m + n) is simpler and often faster
5. **Staircase Pattern:** The path you trace looks like descending stairs

## Visual Pattern
```
Start here ↓
[1,   4,  7, 11, ★15]  ← Go left
[2,   5,  8, 12, 19]
[3,   6,  9, 16, 22]

[1,   4,  7, ★11, 15]  ← Go left
...

[1,  ★4,  7, 11, 15]  ← Go down (4 < 5)
[2,  ★5,  8, 12, 19]  ← FOUND!
```
