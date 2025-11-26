# Q33: Letter Combinations of a Phone Number

## Problem Description
Given a string containing digits 2-9, return all possible letter combinations the number could represent (like phone keypad).

## Core Idea: Backtracking
**Approach:** Build combinations character by character, exploring all possible letters for each digit.

## How It Works (Layman''s Terms)

Imagine: **T9 Keyboard Combinations**
- Each digit maps to 3-4 letters (2=abc, 3=def, etc.)
- For each digit, try each possible letter
- Build strings by combining choices from each position

Example: "23"
- Digit 2 → [a, b, c]
- Digit 3 → [d, e, f]
- Combinations: ad, ae, af, bd, be, bf, cd, ce, cf

## Visualization

👉 [Interactive Visualization (HTML)](./33-letter-combinations.html)

## Core Code Logic

```python
def letterCombinations(digits: str) -> List[str]:
    if not digits:
        return []

    phone = {
        ''2'': ''abc'', ''3'': ''def'', ''4'': ''ghi'', ''5'': ''jkl'',
        ''6'': ''mno'', ''7'': ''pqrs'', ''8'': ''tuv'', ''9'': ''wxyz''
    }

    def backtrack(index, path):
        if index == len(digits):
            result.append(''''.join(path))
            return

        for letter in phone[digits[index]]:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()

    result = []
    backtrack(0, [])
    return result
```

## Complexity

- **Time:** O(4^n × n) - max 4 letters per digit, n digits
- **Space:** O(n) - recursion depth

## Key Takeaways

1. **Backtracking pattern** - try, recurse, undo
2. **Phone mapping** - digit to letters dictionary
3. **Base case** - when all digits processed, save result
