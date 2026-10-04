# This is LeetCode 678 – Valid Parenthesis String.

# The easiest and most efficient approach is the Greedy Range method.

# Python Solution
class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0
        high = 0

        for ch in s:
            if ch == '(':
                low += 1
                high += 1

            elif ch == ')':
                low -= 1
                high -= 1

            else:  # '*'
                low -= 1      # '*' acts as ')'
                high += 1     # '*' acts as '('

            # Too many ')' even in the best case
            if high < 0:
                return False

            # low cannot be negative
            low = max(low, 0)

        return low == 0
# How it works

# We maintain two values:

# low = minimum possible number of unmatched (
# high = maximum possible number of unmatched (

# For each character:

# Character	low	high
# (	+1	+1
# )	-1	-1
# *	-1	+1

# For *, we consider all three possibilities:

# * → ')'
# * → '('
# * → ''

# So:

# low -= 1
# high += 1

# Then:

# low = max(low, 0)

# because we cannot have fewer than 0 unmatched opening brackets.

# Example: "(*))"

# Start:

# low = 0, high = 0

# (:

# low = 1, high = 1

# *:

# low = 0, high = 2

# ):

# low = 0, high = 1

# ):

# low = 0, high = 0

# At the end:

# low == 0

# Therefore:

# true
# Complexity
# Time:  O(n)
# Space: O(1)

# The important interview idea is: we don't need to decide what each * is immediately; we keep a range of possible unmatched opening brackets.