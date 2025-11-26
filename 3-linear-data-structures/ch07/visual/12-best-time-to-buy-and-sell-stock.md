# Question 12: Best Time to Buy and Sell Stock

## Layman's Explanation
You have a list of stock prices for each day. You want to buy on one day and sell on a later day to make the most money.
**Goal:** Find the maximum profit.

### How the Algorithm Works (One Pass)
Imagine you are walking through time, day by day.
1.  **Track Minimum Price:** You always remember the *lowest price you have seen so far*. Let's call this `min_price`.
2.  **Calculate Potential Profit:** On any given day, you ask: "If I had bought at the `min_price` and sold today, how much would I make?"
    -   `profit = current_price - min_price`
3.  **Track Maximum Profit:** You compare this potential profit with the best profit you've found so far. If today's profit is better, you update your record.

## Visualization
I have created an interactive visualization to help you see how we track the minimum price and calculate profit.

[Open Visualization (12-best-time-to-buy-and-sell-stock.html)](./12-best-time-to-buy-and-sell-stock.html)

*(Open the HTML file in your browser to interact with the visualization)*
