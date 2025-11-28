# Problem 46: Merge Two Binary Trees

## Visualization
[View Interactive Visualization](./46-merge-two-binary-trees.html)

## Problem Statement
Given two binary trees, merge them into a new binary tree. The merge rule is: if two nodes overlap, sum their values; otherwise, use the non-null node.

## Layman's Explanation
Imagine laying two transparent tree diagrams on top of each other. Where both have a node, you add the numbers together. Where only one has a node, you just use that node. It's like combining two family trees where some branches exist in both and others only in one.

## Step-by-Step Walkthrough
1. **Base Case**: If either tree is null, return the other tree
2. **Create New Node**: Sum values from both trees: t1.val + t2.val
3. **Recursively Merge Left**: Merge t1.left with t2.left
4. **Recursively Merge Right**: Merge t1.right with t2.right
5. **Return**: The newly merged node

## Visual Example
```
Tree1:      Tree2:       Merged:
    1           2            3
   / \         / \          / \
  3   2       1   3        4   5
 /             \   \      / \   \
5               4   7    5   4   7
```

## Code Snippet
```python
def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
    if t1 and t2:
        node = TreeNode(t1.val + t2.val)
        node.left = self.mergeTrees(t1.left, t2.left)
        node.right = self.mergeTrees(t1.right, t2.right)
        return node
    else:
        return t1 or t2
```

## Complexity Analysis
- **Time Complexity**: O(min(m, n)) - visit overlapping nodes
- **Space Complexity**: O(min(h1, h2)) - recursion stack for overlapping height
