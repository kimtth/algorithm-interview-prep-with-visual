# Problem 53: Minimum Distance Between BST Nodes

## Visualization
[View Interactive Visualization](./53-min-distance-bst.html)

## Problem Statement
Given the root of a Binary Search Tree, return the minimum difference between the values of any two different nodes in the tree.

## Layman's Explanation
In a BST, an **in-order traversal** visits nodes in sorted order (smallest to largest). The minimum difference must be between two consecutive nodes in this sorted order. So we traverse in-order, comparing each node to the previous one, tracking the smallest gap.

## Step-by-Step Walkthrough
1. **In-order Traversal**: Visit left → node → right
2. **Track Previous**: Remember the last node's value
3. **Calculate Difference**: current.val - previous.val
4. **Update Minimum**: Keep track of smallest difference
5. **Move Forward**: Previous = current, continue traversal

## Visual Example
```
BST:
      4
     / \
    2   6
   / \
  1   3

In-order: [1, 2, 3, 4, 6]
Differences: 2-1=1, 3-2=1, 4-3=1, 6-4=2
Minimum = 1
```

## Code Snippet
```python
class Solution:
    prev = -sys.maxsize
    result = sys.maxsize

    def minDiffInBST(self, root: TreeNode) -> int:
        if root.left:
            self.minDiffInBST(root.left)

        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val

        if root.right:
            self.minDiffInBST(root.right)

        return self.result
```

## Complexity Analysis
- **Time Complexity**: O(n) - visit each node once
- **Space Complexity**: O(h) - recursion stack, where h is tree height
