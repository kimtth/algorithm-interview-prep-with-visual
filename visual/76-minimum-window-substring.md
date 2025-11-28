# 76. Minimum Window Substring

## Problem Description
Given strings `s` and `t`, find the minimum window in `s` that contains all characters of `t`. If no such window exists, return empty string.

## Layman's Explanation
Imagine you're searching for a specific set of letters in a long text. You want to find the smallest portion of text that contains ALL the letters you need (including duplicates).

**Example:** `s = "ADOBECODEBANC"`, `t = "ABC"`

We need a window containing at least one A, one B, and one C.

```
ADOBECODEBANC
↑    ↑
Found: A...C but no B → keep expanding

ADOBECODEBANC
↑     ↑
A, D, O, B, E, C → Contains A, B, C! ✓ Window = "ADOBEC" (length 6)

Can we shrink? Move left pointer:
ADOBECODEBANC
 ↑    ↑
D, O, B, E, C → No A! Need to expand again...

Continue sliding to find smaller window:
ADOBECODEBANC
         ↑  ↑
B, A, N, C → Contains A, B, C! ✓ Window = "BANC" (length 4)
```

**Result:** `"BANC"`

## Algorithm Walkthrough

### Two-Pointer Sliding Window with Counter
Use two pointers: `left` and `right`
- Expand `right` to include characters until all of `t` is covered
- Shrink `left` to find minimum window while still valid
- Track characters needed with a counter

**Given:** `s = "ADOBECODEBANC"`, `t = "ABC"`

| Step | Window | Need Counter | Missing | Valid? |
|------|--------|--------------|---------|--------|
| 0    | ""     | {A:1,B:1,C:1}| 3       | No     |
| 1    | "A"    | {A:0,B:1,C:1}| 2       | No     |
| 2    | "AD"   | {A:0,B:1,C:1,D:-1}| 2  | No     |
| ...  | ...    | ...          | ...     | ...    |
| 6    | "ADOBEC"|{A:0,B:0,C:0,...}| 0    | Yes!   |

When valid, try shrinking from left:
- Remove 'A' → need counter becomes {A:1,...} → missing=1 → invalid
- Record window, expand right again

## Code Explanation
```python
def minWindow(self, s: str, t: str) -> str:
    need = collections.Counter(t)  # Characters we need
    missing = len(t)               # Total chars still needed
    left = start = end = 0

    # Expand right pointer
    for right, char in enumerate(s, 1):
        missing -= need[char] > 0  # Found a needed char
        need[char] -= 1            # Update count

        # Window is valid when missing == 0
        if missing == 0:
            # Shrink from left while still valid
            while left < right and need[s[left]] < 0:
                need[s[left]] += 1
                left += 1

            # Update minimum window
            if not end or right - left <= end - start:
                start, end = left, right
            
            # Move left to make window invalid (find next valid window)
            need[s[left]] += 1
            missing += 1
            left += 1

    return s[start:end]
```

**Key insight:** `need[char] < 0` means we have extra chars that can be removed.

## Complexity Analysis
- **Time Complexity:** O(|s| + |t|) - Each character visited at most twice
- **Space Complexity:** O(|t|) - Counter for target characters

## Key Insights
1. **Two-phase approach:** Expand to valid, shrink to minimum
2. **Counter tracks excess:** Negative count means we have extras
3. **Missing counter:** Quick check if window contains all needed chars
4. **Left pointer moves right only:** Ensures O(n) time
5. **Edge cases:** Empty strings, t longer than s, no valid window
