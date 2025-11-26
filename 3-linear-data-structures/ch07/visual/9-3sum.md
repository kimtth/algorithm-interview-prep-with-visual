# Question 9: 3Sum

## Layman's Explanation
We need to find three numbers in a list that add up to exactly zero. We want to find all such unique triplets.

### How the Algorithm Works (Sort + Two Pointers)
Finding three numbers is hard. But finding *two* numbers that add up to a target is easier (we did that in Question 7).
So, we turn this 3-number problem into a series of 2-number problems.

1.  **Sort:** First, we sort the numbers. This helps us avoid duplicates and allows us to use the "Two Pointer" technique.
2.  **Fix One Number:** We go through the list and pick one number (let's call it `A`) to be the first of our triplet.
3.  **Find the Other Two:** Now we need to find two other numbers (`B` and `C`) such that `A + B + C = 0`.
    -   This is the same as finding `B + C = -A`.
    -   We use two pointers: one starting right after `A` (`left`) and one at the end of the list (`right`).
    -   If `B + C` is too small, we move the `left` pointer to a larger number.
    -   If `B + C` is too big, we move the `right` pointer to a smaller number.
    -   If `B + C` is just right, we found a triplet!
4.  **Skip Duplicates:** Since we want unique triplets, if we see the same number again, we skip it.

## Visualization
I have created an interactive visualization to help you see how we fix one number and search for the other two.

[Open Visualization (9-3sum.html)](./9-3sum.html)

*(Open the HTML file in your browser to interact with the visualization)*
