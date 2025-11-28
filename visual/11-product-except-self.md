# Question 11: Product of Array Except Self

## Layman's Explanation
We have a list of numbers. For each number, we want to calculate the product of **all other numbers** in the list, *except* the one we are currently looking at.
**Constraint:** We cannot use division. (If we could, we'd just multiply everything and divide by the current number).

### How the Algorithm Works (Left and Right Sweeps)
Imagine standing at a specific number in the line. The product of "everything else" is simply:
`(Product of everyone to your left) * (Product of everyone to your right)`

1.  **Left Sweep:** We walk from left to right. We keep a running product of everything we've seen so far. We write this down for each position.
    -   At index `i`, the written value is the product of `nums[0]` to `nums[i-1]`.
2.  **Right Sweep:** We walk from right to left. We keep a running product of everything we've seen from the right side.
    -   At index `i`, we take the value we already wrote (Left Product) and multiply it by our current running product (Right Product).
3.  **Result:** The final value at each position is `Left Product * Right Product`.

## Visualization
I have created an interactive visualization to help you see these two sweeps.

[Open Visualization (11-product-except-self.html)](./11-product-except-self.html)

*(Open the HTML file in your browser to interact with the visualization)*
