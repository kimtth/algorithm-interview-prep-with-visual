# Question 3: Reorder Data in Log Files

## Layman's Explanation
Imagine you have a pile of messy log files. Each log has an ID (like "dig1" or "let1") followed by some content.
-   **Digit-logs:** The content is all numbers (e.g., "dig1 8 1 5 1").
-   **Letter-logs:** The content is all words (e.g., "let1 art can").

The task is to organize them with specific rules:
1.  **Letter-logs come first**, followed by **Digit-logs**.
2.  **Letter-logs** must be sorted alphabetically by their **content**.
    -   If the content is exactly the same, then sort by their **ID**.
3.  **Digit-logs** should stay in the **original order** they appeared.

### How the Algorithm Works (Solution 3-1)
1.  **Separation:** We go through the pile one by one.
    -   If the content is numbers, we throw it into a "Digit Pile".
    -   If the content is words, we throw it into a "Letter Pile".
2.  **Sorting Letters:** We take the "Letter Pile" and sort it.
    -   Primary sorting key: The content (everything after the ID).
    -   Secondary sorting key: The ID (the first part).
3.  **Merging:** We simply glue the sorted "Letter Pile" and the original "Digit Pile" together.

## Visualization
I have created an interactive visualization to help you see this sorting process.

[Open Visualization (3-reorder-log-files.html)](./3-reorder-log-files.html)

*(Open the HTML file in your browser to interact with the visualization)*
