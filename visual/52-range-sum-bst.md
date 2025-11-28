# Problem 52: Range Sum of BST

## Visualization
[View Interactive Visualization](./52-range-sum-bst.html)

## Problem Statement
Given the root of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

## Layman's Explanation
Imagine a tree where numbers are organized (smaller left, larger right). You want the sum of all values between low and high. Instead of checking every node, we can be smart: if a node's value is too small, skip its left subtree (all smaller). If too large, skip its right subtree (all larger). This is the power of BST properties!

## Step-by-Step Walkthrough
1. **Base Case**: If node is null, return 0
2. **Check Range**: Is current value between low and high?
3. **Include/Exclude**: Add value if in range, else 0
4. **Recurse Left**: Add sum from left subtree
5. **Recurse Right**: Add sum from right subtree
6. **Optimization**: Skip subtrees that can't have valid values

## Visual Example
```
BST:           Range: [7, 15]
      10
     /  \
    5    15        Nodes in range: 10, 15, 7
   / \     \       Sum = 10 + 15 + 7 = 32
  3   7     18

Skip: 3 (too small), 18 (too large)
```

## Code Snippet
```python
def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
    if not root:
        return 0

    return (root.val if L <= root.val <= R else 0) + \
           self.rangeSumBST(root.left, L, R) + \
           self.rangeSumBST(root.right, L, R)
```

## Complexity Analysis
- **Time Complexity**: O(n) worst case, but typically less due to pruning
- **Space Complexity**: O(h) - recursion stack, where h is tree height
