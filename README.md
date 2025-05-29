# Crush-money.py
This Python script calculates the minimum number of coins needed to represent a given amount of money using Iranian coin denominations: 10, 2, and 1 Toman.

How It Works:

Input Handling: The program prompts the user to enter an amount in Toman. It then attempts to convert this input into an integer. If the input is invalid (e.g., non-numeric or negative), the program exits without further action.

Coin Calculation: The calculate_coins function takes the amount and computes:

The number of 10-Toman coins (ten_toman).

The remaining amount after subtracting the 10-Toman coins is then used to calculate the number of 2-Toman coins (two_toman).

Finally, the remaining amount is the number of 1-Toman coins (one_toman).

Output Formatting: The results are formatted into a list, and each coin denomination is displayed only if it's greater than zero. The denominations are separated by commas.

Example:

Input: 28

Output: 2 10, 1 2, 6 1
Python Tutorials
+7
Stack Overflow
+7
codifytutor.com
+7

This indicates that 28 Toman can be represented as two 10-Toman coins, one 2-Toman coin, and six 1-Toman coins.
