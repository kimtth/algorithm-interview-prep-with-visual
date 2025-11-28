# 77. Longest Repeating Character Replacement

## Problem Description
Given a string `s` and an integer `k`, you can replace at most `k` characters. Find the length of the longest substring containing the same letter after replacements.

## Layman's Explanation
You have a string and can change up to `k` letters to any other letter. What's the longest substring you can make where all letters are the same?

**Example:** `s = "AABABBA"`, `k = 1`

```
AABABBA  with k=1 replacement:
↑↑↑↑     "AABA" - change B to A → "AAAA" (length 4) ✓
   ↑↑↑↑  "ABBA" - need 2 changes → not possible with k=1
```

**Strategy:** For any window, count the most frequent character. Other characters need to be replaced.

```
Window length - max frequency = characters to replace

If (window length - max freq) ≤ k → window is valid!
```

**Result:** 4 (substring "AABA" → "AAAA")

## Algorithm Walkthrough
Given: `s = "AABABBA"`, `k = 1`

Use sliding window:
- Expand right to grow window
- When replacements needed > k, shrink from left

| Window | Counts | Max Freq | Need Replace | Valid? |
|--------|--------|----------|--------------|--------|
| A      | {A:1}  | 1        | 0            | Yes    |
| AA     | {A:2}  | 2        | 0            | Yes    |
| AAB    | {A:2,B:1} | 2     | 1            | Yes (1≤1) |
| AABA   | {A:3,B:1} | 3     | 1            | Yes (1≤1) |
| AABAB  | {A:3,B:2} | 3     | 2            | No (2>1) |

When invalid, shrink window:
| ABAB   | {A:2,B:2} | 2     | 2            | No     |
→ Remove A from left:
| BAB    | {A:1,B:2} | 2     | 1            | Yes    |

Continue expanding...

**Maximum valid window length found: 4**

## Code Explanation
```python
def characterReplacement(self, s: str, k: int) -> int:
    left = right = 0
    counts = collections.Counter()
    
    for right in range(1, len(s) + 1):
        counts[s[right - 1]] += 1
        
        # Find most frequent character in window
        max_char_n = counts.most_common(1)[0][1]
        
        # If replacements needed > k, shrink window
        if right - left - max_char_n > k:
            counts[s[left]] -= 1
            left += 1
    
    return right - left
```

**Key formula:** 
```
replacements_needed = window_length - max_frequency
                    = (right - left) - max_char_count
```

**Clever trick:** We don't shrink the window smaller than the current best. If a larger valid window exists, we'll find it. Otherwise, we keep the current maximum.

## Complexity Analysis
- **Time Complexity:** O(26 × n) = O(n) - For each position, finding max in at most 26 characters
- **Space Complexity:** O(26) = O(1) - Counter for at most 26 letters

## Key Insights
1. **Window validity:** `window_size - max_freq ≤ k`
2. **Greedy max tracking:** Keep the most frequent char, replace others
3. **Window never shrinks below best:** Optimization to maintain maximum size
4. **Only move left when invalid:** When replacements exceed k, left pointer moves
5. **Final answer:** `right - left` at the end (window size is the answer)
