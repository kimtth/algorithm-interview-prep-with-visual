# Q30: Longest Substring Without Repeating Characters

## Problem Description
Given a string, find the length of the **longest substring** without repeating characters.

## Core Idea: Sliding Window + Hash Map
**Approach:** Use two pointers (window) and a hash map to track character positions. When a duplicate is found, shrink the window.

## How It Works (Layman''s Terms)

Imagine: **Expanding a Rubber Band**
- Stretch the band (window) as far as possible without duplicates
- When you hit a repeat, snap the left side forward
- Track the maximum stretch achieved

Example: "abcabcbb"
1. Window "a" → max=1, map={a:0}
2. Window "ab" → max=2, map={a:0, b:1}
3. Window "abc" → max=3, map={a:0, b:1, c:2}
4. Hit ''a'' again → move left to index 1, window "bca" → max=3
5. Hit ''b'' again → move left to index 2, window "cab" → max=3
6. Continue... final max=3

## Visualization

👉 [Interactive Visualization (HTML)](./30-longest-substring-without-repeating.html)

## Core Code Logic

```python
def lengthOfLongestSubstring(s: str) -> int:
    used = {}
    max_len = start = 0

    for i, char in enumerate(s):
        # If char seen and within current window
        if char in used and start <= used[char]:
            start = used[char] + 1
        else:
            max_len = max(max_len, i - start + 1)
        used[char] = i

    return max_len
```

## Complexity

- **Time:** O(n) - single pass through string
- **Space:** O(min(n, m)) where m is alphabet size

## Key Takeaways

1. **Sliding window** - efficient for substring problems
2. **Hash map stores indices** - enables O(1) jump to valid position
3. **Check window bounds** - old occurrences outside window are ignored
