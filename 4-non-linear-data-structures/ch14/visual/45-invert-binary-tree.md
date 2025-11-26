# Problem 45: Invert Binary Tree

## Visualization
[View Interactive Visualization](./45-invert-binary-tree.html)

## Problem Statement
Given the root of a binary tree, invert the tree, and return its root. Inverting means swapping left and right children at every node.

## Layman's Explanation
Imagine looking at a tree in a mirror - everything left becomes right and vice versa. We recursively flip each node's children. It's like saying "swap your hands" to everyone in a family photo, starting from the kids and working up to the grandparents.

## Step-by-Step Walkthrough
1. **Base Case**: If node is null, return null
2. **Recursive Invert**: First invert right subtree, then invert left subtree
3. **Swap**: Assign inverted right to left, inverted left to right
4. **Return**: Return the current node with swapped children
5. **Result**: The entire tree is now mirrored

## Visual Example
```
Before:           After:
     4                4
   /   \            /   \
  2     7    →     7     2
 / \   / \        / \   / \
1   3 6   9      9   6 3   1
```

## Code Snippet
```python
def invertTree(self, root: TreeNode) -> TreeNode:
    if root:
        root.left, root.right = \
            self.invertTree(root.right), self.invertTree(root.left)
        return root
    return None
```

## Complexity Analysis
- **Time Complexity**: O(n) - visit every node once
- **Space Complexity**: O(h) - recursion stack, where h is tree height
