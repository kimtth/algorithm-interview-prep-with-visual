# Problem 47: Serialize and Deserialize Binary Tree

## Visualization
[View Interactive Visualization](./47-serialize-deserialize.html)

## Problem Statement
Design an algorithm to serialize a binary tree to a string, and deserialize the string back to the original tree structure.

## Layman's Explanation
Imagine you need to save a tree structure to a text file and later rebuild it exactly. **Serialization** is like writing down a recipe for the tree - we use BFS to visit nodes level by level, marking empty spots with '#'. **Deserialization** is following that recipe to reconstruct the tree, using a queue to connect parents with their children.

## Step-by-Step Walkthrough
### Serialize:
1. Use BFS queue starting with root
2. For each node, append its value; for null, append '#'
3. Add children to queue (even if null for tracking)
4. Join all values with spaces

### Deserialize:
1. Split string into tokens
2. Create root from first value
3. Use queue to track parent nodes
4. For each parent, assign next two tokens as left/right children
5. Add non-null children to queue

## Visual Example
```
Tree:          Serialized:
    1          "# 1 2 3 # # 4 5"
   / \
  2   3
     / \
    4   5

Deserialize: Read tokens, build level by level
```

## Code Snippet
```python
def serialize(self, root: TreeNode) -> str:
    queue = collections.deque([root])
    result = ['#']
    while queue:
        node = queue.popleft()
        if node:
            queue.append(node.left)
            queue.append(node.right)
            result.append(str(node.val))
        else:
            result.append('#')
    return ' '.join(result)

def deserialize(self, data: str) -> TreeNode:
    if data == '# #':
        return None
    nodes = data.split()
    root = TreeNode(int(nodes[1]))
    queue = collections.deque([root])
    index = 2
    while queue:
        node = queue.popleft()
        if nodes[index] is not '#':
            node.left = TreeNode(int(nodes[index]))
            queue.append(node.left)
        index += 1
        if nodes[index] is not '#':
            node.right = TreeNode(int(nodes[index]))
            queue.append(node.right)
        index += 1
    return root
```

## Complexity Analysis
- **Time Complexity**: O(n) for both serialize and deserialize
- **Space Complexity**: O(n) for storing the serialized string and queue
