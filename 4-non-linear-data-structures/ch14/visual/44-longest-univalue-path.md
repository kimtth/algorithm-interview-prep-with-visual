# Problem 44: Longest Univalue Path

## Visualization
[View Interactive Visualization](./44-longest-univalue-path.html)

## Problem Statement
Given the root of a binary tree, return the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

## Layman's Explanation
Imagine a family tree where everyone has a favorite color. You want to find the longest chain of relatives who all share the SAME favorite color. At each person, you check: "Does my child have the same color as me?" If yes, you can extend the path through them. We use **DFS** and only count edges where parent and child match.

## Step-by-Step Walkthrough
1. **DFS from Leaves**: Process children before parents
2. **Check Left Child**: If left.val == node.val, path_left = 1 + left_result
3. **Check Right Child**: If right.val == node.val, path_right = 1 + right_result
4. **Update Longest**: path_left + path_right is the longest path through this node
5. **Return to Parent**: Return max(path_left, path_right) for parent to use
6. **Track Maximum**: Keep updating the global maximum

## Visual Example
```
Tree:
       5
      / \
     4   5
    / \   \
   1   1   5

At node 5 (right child): path = 0 (no children match)
At node 5 (right of root): right matches! path = 1
At node 5 (root): right child matches! path through root = 0 + 1 + 1 = 2

Longest Univalue Path = 2 (5→5→5)
```

## Code Snippet
```python
def longestUnivaluePath(self, root: TreeNode) -> int:
    result: int = 0

    def dfs(node: TreeNode) -> int:
        if node is None:
            return 0

        # 존재하지 않는 노드까지 DFS 재귀 탐색
        left = dfs(node.left)
        right = dfs(node.right)

        # 현재 노드가 자식 노드와 동일한 경우 거리 1 증가
        if node.left and node.left.val == node.val:
            left += 1
        else:
            left = 0
        if node.right and node.right.val == node.val:
            right += 1
        else:
            right = 0

        # 왼쪽과 오른쪽 자식 노드 간 거리의 합 최대값이 결과
        result = max(result, left + right)
        # 자식 노드 상태값 중 큰 값 리턴
        return max(left, right)

    dfs(root)
    return result
```

## Complexity Analysis
- **Time Complexity**: O(n) - visit every node once
- **Space Complexity**: O(h) - recursion stack, where h is tree height
