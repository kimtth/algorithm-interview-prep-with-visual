# Question 7: Two Sum

## Layman's Explanation
We have a list of numbers and a specific "target" number. We need to find two numbers in the list that add up exactly to the target.

### How the Algorithm Works (Optimized Hash Map)
Instead of checking every single pair (which takes a long time), we can use a "Memory" (Hash Map) to remember what we've seen.

1.  **The Walk:** We walk through the list of numbers one by one.
2.  **The Question:** For each number (let's call it `current`), we ask: "What number do I need to reach the target?"
    -   `needed = target - current`
3.  **The Check:** We look in our Memory. "Have I seen the `needed` number before?"
    -   **Yes:** We found the pair! The `current` number and the `needed` number (from memory) are the answer.
    -   **No:** We haven't seen it yet. So, we write down the `current` number and its location in our Memory, just in case a future number needs it.

## Visualization
I have created an interactive visualization to help you see this "Check and Remember" process.

[Open Visualization (7-two-sum.html)](./7-two-sum.html)

*(Open the HTML file in your browser to interact with the visualization)*
