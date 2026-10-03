# This is the classic Longest Valid Parentheses problem. A simple and interview-friendly solution uses a stack.

# Python — Stack Approach
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_len = 0

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()

                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])

        return max_len
# How it works

# We store indices in the stack.

# For:

# s = ")()())"

# Initially:

# stack = [-1]

# The -1 acts as a boundary before the string.

# When we see:

# ( → push its index.
# ) → pop the matching (.
# If the stack becomes empty → the current ) becomes the new boundary.
# Otherwise → calculate the current valid length:
# i - stack[-1]

# For ")()())":

# Index:  0 1 2 3 4 5
# String: ) ( ) ( ) )

# Longest valid substring = "()()" 
# Length = 4
# Complexity
# Metric	Complexity
# Time	O(n)
# Space	O(n)

# This works comfortably for n <= 3 * 10⁴.

# Interview explanation

# You can say:

# "I use a stack to store indices of unmatched opening parentheses. I initialize it with -1 as a boundary. Whenever I encounter a closing parenthesis, I pop the stack. If the stack becomes empty, I push the current index as the new boundary. Otherwise, the current valid substring length is the current index minus the index at the top of the stack. I keep track of the maximum length."

# Key idea: The stack stores the index of the last unmatched ) or unmatched ( boundary, allowing us to calculate valid substring lengths in O(1).