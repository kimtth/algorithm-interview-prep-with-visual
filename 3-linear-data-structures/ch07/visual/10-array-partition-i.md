# Question 10: Array Partition I

## Layman's Explanation
We have a list of numbers (e.g., `[1, 4, 3, 2]`). We need to group them into pairs (like `(1, 4)` and `(2, 3)`).
For each pair, we take the **minimum** number. Then we add up all these minimums.
Our goal is to make this total sum as **large as possible**.

### How the Algorithm Works (Sort and Pair)
Think about it: If you pair a small number (1) with a huge number (1000), the `min(1, 1000)` is just 1. The 1000 is "wasted".
To save the large numbers, we should pair them with other large numbers.
-   If we have `1, 2, 3, 4`.
-   Bad pairing: `(1, 4)` and `(2, 3)`. Mins are 1 and 2. Sum = 3.
-   Good pairing: `(1, 2)` and `(3, 4)`. Mins are 1 and 3. Sum = 4.

**Strategy:**
1.  **Sort** the list from smallest to largest.
2.  **Pair** neighbors together: `(1st, 2nd)`, `(3rd, 4th)`, etc.
3.  **Sum:** Since the list is sorted, the first number in each pair is always the minimum. So we just add up every other number (index 0, 2, 4...).

## Visualization
I have created an interactive visualization to help you see why sorting helps maximize the sum.

[Open Visualization (10-array-partition-i.html)](./10-array-partition-i.html)

*(Open the HTML file in your browser to interact with the visualization)*
