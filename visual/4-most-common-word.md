# Question 4: Most Common Word

## Layman's Explanation
The goal is to find the most frequently used word in a paragraph, but with a few catches:
1.  **Ignore Punctuation:** "Ball," and "ball" should be treated as the same word "ball".
2.  **Case Insensitive:** "Bob" and "bob" are the same.
3.  **Banned Words:** There is a list of "banned" words (like "hit") that we should completely ignore, even if they appear many times.

### How the Algorithm Works (Solution 4-1)
1.  **Cleaning:**
    -   We take the paragraph and replace any character that is *not* a word character (like `!`, `?`, `,`, `.`) with a space.
    -   We convert everything to lowercase.
2.  **Splitting:** We chop the cleaned text into individual words.
3.  **Filtering:** We look at each word. If it is in our "banned" list, we throw it away.
4.  **Counting:** We count how many times each remaining word appears.
5.  **Result:** We pick the word with the highest count.

## Visualization
I have created an interactive visualization to help you see this process.

[Open Visualization (4-most-common-word.html)](./4-most-common-word.html)

*(Open the HTML file in your browser to interact with the visualization)*
