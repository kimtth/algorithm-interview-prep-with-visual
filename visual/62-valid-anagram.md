# 62. Valid Anagram

## Problem Description
Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise. An anagram uses exactly the same characters with the same frequencies, just in a different order.

## Layman's Explanation
Think of anagram checking like sorting two decks of letter tiles:

1. **Deck 1:** Letters from word "listen" → l, i, s, t, e, n
2. **Deck 2:** Letters from word "silent" → s, i, l, e, n, t

Now sort both decks alphabetically:
1. **Sorted Deck 1:** e, i, l, n, s, t
2. **Sorted Deck 2:** e, i, l, n, s, t

If they match perfectly, they're anagrams! ✓

This is like checking if two people got the same LEGO pieces - just arrange them the same way and compare!

## Algorithm Walkthrough
Given: `s = "anagram"`, `t = "nagaram"`

**Step 1: Sort both strings**
- `sorted("anagram")` = ['a', 'a', 'a', 'g', 'm', 'n', 'r']
- `sorted("nagaram")` = ['a', 'a', 'a', 'g', 'm', 'n', 'r']

**Step 2: Compare**
- `['a', 'a', 'a', 'g', 'm', 'n', 'r']` == `['a', 'a', 'a', 'g', 'm', 'n', 'r']`
- They match! ✓

**Result:** `True` - they are anagrams!

**Counter-example:** `s = "rat"`, `t = "car"`
- `sorted("rat")` = ['a', 'r', 't']
- `sorted("car")` = ['a', 'c', 'r']
- Not equal! ✗

## Code Explanation
```python
def isAnagram(self, s: str, t: str) -> bool:
    return sorted(s) == sorted(t)
```

That's it! One line. Python's `sorted()` returns a list of characters, and we compare the two lists.

**Alternative using Counter (more efficient for large strings):**
```python
from collections import Counter

def isAnagram(self, s: str, t: str) -> bool:
    return Counter(s) == Counter(t)
```

This counts character frequencies instead of sorting:
- `Counter("anagram")` = {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}
- `Counter("nagaram")` = {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}

## Complexity Analysis
**Sorting Approach:**
- **Time Complexity:** O(n log n) - Dominated by sorting
- **Space Complexity:** O(n) - Space for sorted arrays

**Counter Approach:**
- **Time Complexity:** O(n) - Single pass to count characters
- **Space Complexity:** O(1) - At most 26 letters (fixed alphabet)

## Key Insights
1. **Anagram Definition:** Same characters, same frequencies, different order
2. **Sorting Trick:** Sorting normalizes any arrangement → easy comparison
3. **Counter Alternative:** Faster O(n) using hash map for frequencies
4. **Edge Cases:** Empty strings are anagrams of each other, different lengths → cannot be anagrams
