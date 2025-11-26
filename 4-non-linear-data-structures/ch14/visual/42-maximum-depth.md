# Q42: Maximum Depth of Binary Tree

## Problem Description
Given the root of a binary tree, return its maximum depth. Maximum depth is the number of nodes along the longest path from root to the farthest leaf.

## Core Idea: Recursive DFS
**Approach:** The depth of a tree = 1 + max(depth of left subtree, depth of right subtree).

## How It Works (Layman''s Terms)

Imagine: **Measuring Tree Height**
- Ask left child: "How tall are you?"
- Ask right child: "How tall are you?"
- My height = 1 + taller child''s height
- Leaf nodes have height 1, empty nodes have height 0

Example:
```
    3
   / \
  9  20
    /  \
   15   7
```
- Depth of node 9: 1
- Depth of node 15, 7: 1
- Depth of node 20: 1 + max(1, 1) = 2
- Depth of node 3: 1 + max(1, 2) = 3

## Visualization

👉 [Interactive Visualization (HTML)](./42-maximum-depth.html)

## Core Code Logic

```python
def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))
```

BFS alternative:
```python
def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0
    depth = 0
    queue = deque([root])
    while queue:
        depth += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
    return depth
```

## Complexity

- **Time:** O(n) - visit each node once
- **Space:** O(h) - recursion depth equals tree height

## Key Takeaways

1. **Classic tree recursion** - solve for subtrees, combine results
2. **Base case** - empty tree has depth 0
3. **BFS alternative** - count levels instead of recursive depth
