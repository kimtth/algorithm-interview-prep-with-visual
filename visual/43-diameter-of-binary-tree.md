# Problem 43: Diameter of Binary Tree

## Visualization
[View Interactive Visualization](./43-diameter-of-binary-tree.html)

## Problem Statement
Given the root of a binary tree, return the length of the diameter of the tree. The diameter is the length of the longest path between any two nodes in the tree. This path may or may not pass through the root.

## Layman's Explanation
Think of it like finding the longest walking path in a park's tree-shaped trail system. Starting from any point, what's the farthest you can walk? The trick is that at each intersection (node), the longest path going through it equals the distance to the farthest point on the left PLUS the distance to the farthest point on the right. We use **DFS** to compute heights from the bottom up, tracking the maximum diameter as we go.

## Step-by-Step Walkthrough
1. **DFS Approach**: Start from leaves and work up
2. **At Each Node**: Calculate left subtree height and right subtree height
3. **Update Diameter**: The path through this node = left_height + right_height + 2 (edges)
4. **Return Height**: Return max(left, right) + 1 to parent
5. **Track Maximum**: Keep a global variable to track the longest path seen

## Visual Example
```
Tree:
       1
      / \
     2   3
    / \
   4   5

At node 2: left_height=0 (node 4), right_height=0 (node 5)
          path through 2 = 0 + 0 + 2 = 2
At node 1: left_height=1 (from 2), right_height=0 (from 3)
          path through 1 = 1 + 0 + 2 = 3

Diameter = 3 (path: 4→2→1→3 or 5→2→1→3)
```

## Code Snippet
```python
def diameterOfBinaryTree(self, root: TreeNode) -> int:
    self.longest: int = 0

    def dfs(node: TreeNode) -> int:
        if not node:
            return -1
        # 왼쪽, 오른쪽의 각 리프 노드까지 탐색
        left = dfs(node.left)
        right = dfs(node.right)

        # 가장 긴 경로
        self.longest = max(self.longest, left + right + 2)
        # 상태값
        return max(left, right) + 1

    dfs(root)
    return self.longest
```

## Complexity Analysis
- **Time Complexity**: O(n) - visit every node once
- **Space Complexity**: O(h) - recursion stack, where h is tree height
