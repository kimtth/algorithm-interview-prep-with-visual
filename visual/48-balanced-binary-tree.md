# Problem 48: Balanced Binary Tree

## Visualization
[View Interactive Visualization](./48-balanced-binary-tree.html)

## Problem Statement
Given a binary tree, determine if it is height-balanced. A height-balanced tree is one where the left and right subtrees of every node differ in height by no more than 1.

## Layman's Explanation
Imagine a tree where no branch is "too heavy" on one side. At every fork (node), if you measure the depth on the left side and right side, they should be nearly equal (differ by at most 1). We check this from the bottom up using DFS - if we find ANY imbalanced spot, we return -1 as a signal that the whole tree is unbalanced.

## Step-by-Step Walkthrough
1. **Base Case**: Empty node has height 0
2. **Recursive Check**: Get left subtree height, get right subtree height
3. **Imbalance Detection**: If either child returns -1, propagate -1 up
4. **Height Difference**: If |left - right| > 1, return -1 (imbalanced)
5. **Return Height**: If balanced, return max(left, right) + 1
6. **Final Answer**: Tree is balanced if final result ≠ -1

## Visual Example
```
Balanced:          Unbalanced:
    3                  1
   / \                  \
  9  20                  2
    /  \                  \
   15   7                  3

Heights differ       Right side is
by at most 1         too deep (3 vs 0)
```

## Code Snippet
```python
def isBalanced(self, root: TreeNode) -> bool:
    def check(root):
        if not root:
            return 0

        left = check(root.left)
        right = check(root.right)
        
        # 높이 차이가 나는 경우 -1, 이외에는 높이에 따라 1 증가
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1

    return check(root) != -1
```

## Complexity Analysis
- **Time Complexity**: O(n) - visit each node once
- **Space Complexity**: O(h) - recursion stack, where h is tree height
