# Problem 56: Implement Trie (Prefix Tree)

## Visualization
[View Interactive Visualization](./56-implement-trie.html)

## Problem Statement
Implement a trie (prefix tree) with insert, search, and startsWith methods.

## Layman's Explanation
A **Trie** (pronounced "try") is like a family tree for words. Each node represents a character, and paths from root to leaves spell out words. It's super efficient for:
- **Insert**: Walk down creating nodes as needed
- **Search**: Walk down checking if path exists AND ends at a complete word
- **StartsWith**: Walk down checking if prefix path exists

Think of it like a phonebook organized by letters - you navigate letter by letter.

## Step-by-Step Walkthrough
### Insert "apple":
1. Start at root
2. Create/follow 'a' → 'p' → 'p' → 'l' → 'e'
3. Mark final node as "end of word"

### Search "app":
1. Walk path 'a' → 'p' → 'p'
2. Path exists but NOT marked as word → return False

### StartsWith "app":
1. Walk path 'a' → 'p' → 'p'
2. Path exists → return True

## Visual Example
```
After inserting: "apple", "app", "application"

        (root)
          |
          a
          |
          p
          |
          p ← "app" ends here
         / \
        l   l
        |   |
        e   i
(apple)↑   |
           c
           |
           a
           |
           t
           |
           i
           |
           o
           |
           n ← "application"
```

## Code Snippet
```python
class TrieNode:
    def __init__(self):
        self.word = False
        self.children = collections.defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
        node.word = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
```

## Complexity Analysis
- **Time Complexity**: O(m) for all operations, where m is word/prefix length
- **Space Complexity**: O(n * m) for storing n words of average length m
