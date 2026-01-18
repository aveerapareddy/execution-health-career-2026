"""
Core Python Cheat Code for LeetCode
----------------------------------
This file contains ALL Python syntax you will realistically
see while solving LeetCode problems (Easy → Medium).

If something is not here, it is NOT required.
"""

# ==========================================================
# 1. LISTS (arrays)
# ==========================================================

nums = [1, 2, 3]
nums.append(4)
nums.pop()
first = nums[0]
last = nums[-1]

for n in nums:
    pass

for i in range(len(nums)):
    pass

for i, val in enumerate(nums):
    pass


nums.sort()
nums.reverse()
nums_copy = nums[::-1]

# ==========================================================
# 2. STRINGS
# ==========================================================

s = "leetcode"
first_char = s[0]
last_char = s[-1]
length = len(s)

chars = list(s)
joined = "".join(chars)

s_lower = s.lower()
s_upper = s.upper()

words = "a b c".split(" ")

# palindrome check
is_palindrome = s == s[::-1]

# ==========================================================
# 3. DICTIONARY (HashMap) — MOST IMPORTANT
# ==========================================================

freq = {}

for c in s:
    freq[c] = freq.get(c, 0) + 1

for key in freq:
    pass

for key, value in freq.items():
    pass

# dictionary existence check
exists = "a" in freq

# ==========================================================
# 4. SET
# ==========================================================
seen = set()
seen.add(1)
exists = 1 in seen
seen.remove(1)


# ==========================================================
# 5. FUNCTIONS (LeetCode style)
# ==========================================================
def add(a, b):
    return a + b


class Solution:
    def example(self, nums):
        return nums


# ==========================================================
# 6. NONE (null checks)
# ==========================================================
x = None
if x is None:
    pass

if not x:
    pass


# ==========================================================
# 7. LIST COMPREHENSION (optional but common)
# ==========================================================
positives = [x for x in nums if x > 0]


# ==========================================================
# 8. COLLECTIONS (may appear in solutions)
# ==========================================================
from collections import Counter, defaultdict, deque

# Counter (frequency)
counter = Counter("aabbb")

# defaultdict
dd = defaultdict(int)
dd["a"] += 1

# deque (queue)
queue = deque()
queue.append(1)
queue.append(2)
queue.popleft()


# ==========================================================
# 9. STACK (using list)
# ==========================================================
stack = []
stack.append(1)
stack.append(2)
top = stack.pop()


# ==========================================================
# 10. COMMON BUILT-INS
# ==========================================================
max_val = max(nums)
min_val = min(nums)
total = sum(nums)
sorted_nums = sorted(nums)


# ==========================================================
# 11. SIMPLE RECURSION (later use)
# ==========================================================
def dfs(node):
    if node is None:
        return
    dfs(node)
    dfs(node)
