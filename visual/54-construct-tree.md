# Problem 54: Construct Binary Tree from Preorder and Inorder Traversal

## Visualization
[View Interactive Visualization](./54-construct-tree.html)

## Problem Statement
Given two integer arrays preorder and inorder where preorder is the preorder traversal and inorder is the inorder traversal of the same tree, construct and return the binary tree.

## Layman's Explanation
Think of it as a puzzle: **Preorder** tells you "who's the root" (first element is always root). **Inorder** tells you "who's on the left vs right" (everything before root in inorder is left subtree, everything after is right subtree). We use divide and conquer - find root from preorder, split inorder, recursively build subtrees.

## Step-by-Step Walkthrough
1. **Get Root**: First element of preorder is the root
2. **Find Split**: Locate root in inorder array
3. **Left Subtree**: Elements before root in inorder
4. **Right Subtree**: Elements after root in inorder
5. **Recurse**: Build left and right subtrees with remaining preorder elements
6. **Return**: Constructed node

## Visual Example
```
preorder = [3, 9, 20, 15, 7]
inorder  = [9, 3, 15, 20, 7]

Step 1: root = 3 (first of preorder)
Step 2: In inorder: [9] | 3 | [15, 20, 7]
                    left    right
Step 3: Build left with preorder[1:2], inorder[0:1]
Step 4: Build right with preorder[2:], inorder[2:]

Result:
      3
     / \
    9  20
      /  \
     15   7
```

## Code Snippet
```python
def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    if inorder:
        # 전위 순회 결과는 중위 순회 분할 인덱스
        index = inorder.index(preorder.pop(0))

        # 중위 순회 결과 분할 정복
        node = TreeNode(inorder[index])
        node.left = self.buildTree(preorder, inorder[0:index])
        node.right = self.buildTree(preorder, inorder[index + 1:])

        return node
```

## Complexity Analysis
- **Time Complexity**: O(n²) due to index() lookup; can be O(n) with hashmap
- **Space Complexity**: O(n) for recursion and storing tree
