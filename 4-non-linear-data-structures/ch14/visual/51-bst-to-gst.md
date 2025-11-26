# Problem 51: Binary Search Tree to Greater Sum Tree

## Visualization
[View Interactive Visualization](./51-bst-to-gst.html)

## Problem Statement
Given the root of a Binary Search Tree, convert it to a Greater Sum Tree where every node's new value equals the original value plus the sum of all values greater than it in the BST.

## Layman's Explanation
In a BST, values on the right are always greater. So if we traverse **right → node → left** (reverse in-order), we visit nodes from largest to smallest. As we go, we keep a running sum. Each node's new value becomes: original + sum of all previously visited (larger) nodes.

## Step-by-Step Walkthrough
1. **Reverse In-order**: Visit right subtree first
2. **Accumulate**: Add current node's value to running sum
3. **Update Node**: Set node's value to the running sum
4. **Visit Left**: Then process left subtree
5. **Result**: Each node now has sum of itself + all greater values

## Visual Example
```
Original BST:          Greater Sum Tree:
      4                      30
     / \                    /  \
    1   6                  36   21
   / \ / \                / \  / \
  0  2 5  7              36 35 26 15
       \   \                  \   \
        3   8                 33   8

Visit order: 8→7→6→5→4→3→2→1→0
Running sum:  8→15→21→26→30→33→35→36→36
```

## Code Snippet
```python
class Solution:
    val: int = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        # 중위 순회 노드 값 누적
        if root:
            self.bstToGst(root.right)
            self.val += root.val
            root.val = self.val
            self.bstToGst(root.left)

        return root
```

## Complexity Analysis
- **Time Complexity**: O(n) - visit each node once
- **Space Complexity**: O(h) - recursion stack, where h is tree height
