"""Coin change (count ways) using top-down dynamic programming.

This module provides a memoized recursive solution that counts how many
combinations of coin denominations can form a target amount.
"""


def count_ways(coins, i, amount, memo):
    """Return the number of ways to make `amount` using the first `i` coins.

    This uses top-down dynamic programming (memoized recursion).

    Args:
        coins: List of coin denominations.
        i: Number of denominations from the start of `coins` that are allowed.
        amount: Target amount to form.
        memo: Dictionary cache keyed by (i, amount).

    Returns:
        The count of distinct combinations that sum to `amount`.
    """
    if amount == 0:
        return 1
    if i == 0 or amount < 0:
        return 0
    if (i, amount) in memo:
        return memo[(i, amount)]

    # Skip this denomination or use it (stay on same i)
    result = count_ways(coins, i-1, amount, memo) + \
        count_ways(coins, i, amount-coins[i-1], memo)
    memo[(i, amount)] = result
    return result


if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 5
    result = count_ways(coins, len(coins), amount, {})
    # Expected: 4
    print(f"Number of ways to make {amount} using {coins}: {result}")
