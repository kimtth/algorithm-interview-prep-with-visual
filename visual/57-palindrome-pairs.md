# Problem 57: Palindrome Pairs

## Visualization
[View Interactive Visualization](./57-palindrome-pairs.html)

## Problem Statement
Given a list of unique words, return all pairs of distinct indices (i, j) such that the concatenation of words[i] + words[j] is a palindrome.

## Layman's Explanation
A palindrome reads the same forwards and backwards (like "racecar"). We need to find word pairs that, when joined together, form palindromes. The brute force way checks every pair, but a smarter approach uses a **Trie** storing words in reverse - if we can match a word's prefix with a reversed word in the trie, and the remaining suffix is itself a palindrome, we found a valid pair!

## Step-by-Step Walkthrough (Brute Force)
1. **For Each Pair**: Try all (i, j) where i ≠ j
2. **Concatenate**: word[i] + word[j]
3. **Check Palindrome**: Is result == result reversed?
4. **Collect Valid**: Add [i, j] if palindrome

## Visual Example
```
words = ["bat", "tab", "cat"]

Check pairs:
"bat" + "tab" = "battab" ← Palindrome! [0, 1]
"bat" + "cat" = "batcat" ← Not palindrome
"tab" + "bat" = "tabbat" ← Palindrome! [1, 0]
"tab" + "cat" = "tabcat" ← Not palindrome
"cat" + "bat" = "catbat" ← Not palindrome
"cat" + "tab" = "cattab" ← Not palindrome

Result: [[0, 1], [1, 0]]
```

## Code Snippet (Brute Force)
```python
def palindromePairs(self, words: List[str]) -> List[List[int]]:
    def is_palindrome(word):
        return word == word[::-1]

    output = []
    for i, word1 in enumerate(words):
        for j, word2 in enumerate(words):
            if i == j:
                continue
            if is_palindrome(word1 + word2):
                output.append([i, j])
    return output
```

## Optimized Approach (Trie)
Store reversed words in a Trie. For each word, traverse and look for:
1. Exact reverse match (different length words)
2. Word is shorter but remaining part in trie is palindrome
3. Word is longer but remaining part after match is palindrome

## Complexity Analysis
- **Brute Force**: O(n² × k) where k is average word length
- **Trie**: O(n × k²) for building and searching
