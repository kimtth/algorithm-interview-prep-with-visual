# Problem 50: Convert Sorted Array to Binary Search Tree

## Visualization
[View Interactive Visualization](./50-sorted-array-to-bst.html)

## Problem Statement
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

## Layman's Explanation
Imagine you have a sorted list of numbers and want to build the most balanced possible tree. The trick is **divide and conquer**: always pick the middle element as the root (this ensures balance), then recursively do the same for the left half (left subtree) and right half (right subtree).

## Step-by-Step Walkthrough
1. **Base Case**: If array is empty, return null
2. **Find Middle**: mid = len(nums) // 2
3. **Create Node**: Make the middle element the root
4. **Left Subtree**: Recursively build from nums[0:mid]
5. **Right Subtree**: Recursively build from nums[mid+1:]
6. **Return**: The constructed node

## Visual Example
```
Array: [-10, -3, 0, 5, 9]

Step 1: mid=2 → root=0
        0
       
Step 2: left=[−10,−3], mid=0 → left child=-10
        0
       /
     -10
     
Step 3: right of -10 = [-3]
        0
       /
     -10
       \
       -3

Step 4: right=[5,9], mid=0 → right child=5
        0
       / \
     -10  5
       \   \
       -3   9
```

## Code Snippet
```python
def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    if not nums:
        return None

    mid = len(nums) // 2

    # 분할 정복으로 이진 검색 결과 트리 구성
    node = TreeNode(nums[mid])
    node.left = self.sortedArrayToBST(nums[:mid])
    node.right = self.sortedArrayToBST(nums[mid + 1:])

    return node
```

## Complexity Analysis
- **Time Complexity**: O(n) - each element becomes a node
- **Space Complexity**: O(log n) - recursion stack for balanced tree
