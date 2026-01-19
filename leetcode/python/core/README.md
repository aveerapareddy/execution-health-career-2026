# Core Python for LeetCode

This folder contains **minimal Python constructs** required for solving LeetCode problems.
No advanced Python. Only what is repeatedly used in interviews.

Focus:
- Lists
- Strings
- Dictionaries
- Sets
- Loops
- Functions

Rule:
If it is not used in LeetCode, it does not belong here.


# Big-O Cheat Sheet (Python for LeetCode)

This is a fast reference for **time + space complexity** of common Python operations used in LeetCode.

> Rule of thumb:
> - Prefer **O(1)** lookups: `dict`, `set`
> - Be careful with operations that shift elements (often **O(n)**): `list.pop(0)`, `insert(0, x)`

---

## 1) Big-O Basics

### Common growth rates (best → worst)
- **O(1)** constant
- **O(log n)** logarithmic
- **O(n)** linear
- **O(n log n)** sort-like
- **O(n²)** double loops
- **O(2ⁿ)** subsets / recursion without pruning
- **O(n!)** permutations

### Typical LeetCode targets
- Easy: **O(n)** or **O(n log n)**
- Medium: **O(n)** or **O(n log n)** (sometimes **O(n²)** accepted if n small)
- Hard: often needs **O(n)** / **O(n log n)** with a clever idea

---

## 2) Python `list` (dynamic array)

### Access / update
- `a[i]` get: **O(1)**
- `a[i] = x`: **O(1)**

### Append / pop
- `a.append(x)`: **amortized O(1)**
- `a.pop()`: **O(1)**

### Insert / delete (shifts elements)
- `a.insert(i, x)`: **O(n)**
- `a.pop(i)`: **O(n)**
- `del a[i]`: **O(n)**

### Membership
- `x in a`: **O(n)**

### Slicing (creates copy)
- `a[l:r]`: **O(k)** time, **O(k)** space where `k = r-l`

### Reverse / sort
- `a.reverse()`: **O(n)** time, **O(1)** extra space
- `sorted(a)`: **O(n log n)** time, **O(n)** space (creates new list)
- `a.sort()`: **O(n log n)** time, **O(1)** extra space (in-place, but uses internal temp memory)

---

## 3) Python `str` (immutable)

### Access
- `s[i]`: **O(1)**

### Slicing (creates new string)
- `s[l:r]`: **O(k)** time, **O(k)** space

### Concatenation
- `s1 + s2`: **O(len(s1)+len(s2))** time (creates new string)
- Repeated `+=` in a loop: can become **O(n²)** overall (avoid)

Preferred for building strings:
- Collect chars in list + `"".join(list)` → **O(n)** total

### Membership
- `c in s`: **O(n)**

---

## 4) Python `dict` (hash map)

### Average-case (what LeetCode assumes)
- `d[key]` get/set: **O(1)** average
- `key in d`: **O(1)** average
- `d.get(key, default)`: **O(1)** average

### Worst-case
- Can degrade to **O(n)** (pathological hashing), but ignore for interviews.

### Iteration
- `for k in d`: **O(n)** over keys
- `for k, v in d.items()`: **O(n)**

### Space
- Storing `n` keys/values: **O(n)**

---

## 5) Python `set` (hash set)

### Average-case
- `x in s`: **O(1)** average
- `s.add(x)`: **O(1)** average
- `s.remove(x)` / `s.discard(x)`: **O(1)** average

### Iteration
- `for x in s`: **O(n)**

### Space
- Storing `n` elements: **O(n)**

---

## 6) `collections.deque` (queue / BFS)

- `dq.append(x)`: **O(1)**
- `dq.appendleft(x)`: **O(1)**
- `dq.pop()`: **O(1)**
- `dq.popleft()`: **O(1)**

Use deque for BFS queue  
Avoid `list.pop(0)` (it’s **O(n)**)

---

## 7) Heap (priority queue) — `heapq`

- `heappush`: **O(log n)**
- `heappop`: **O(log n)**
- `heapify(list)`: **O(n)**

---

## 8) Sorting

- `sorted(nums)` / `nums.sort()`: **O(n log n)**

If you sort then scan:
- sort **O(n log n)** + scan **O(n)** → **O(n log n)** total

---

## 9) Typical LeetCode Pattern Complexities

### HashMap lookup (Two Sum)
- Time: **O(n)**
- Space: **O(n)**

### Two pointers (sorted array)
- Time: **O(n)**
- Space: **O(1)**

### Sliding window
- Time: **O(n)**
- Space: usually **O(k)** or **O(n)** depending on data structure

### Stack
- Time: **O(n)**
- Space: **O(n)**

### BFS / DFS on graph
- Time: **O(V + E)**
- Space: **O(V)**

### Recursion on tree
- Time: often **O(n)**
- Space: **O(h)** call stack (`h` = height)

---

## 10) Interview-ready phrasing (use this)

- "Single pass through array → **O(n)** time."
- "HashMap for constant-time lookup → **O(1)** average per op."
- "We store seen elements → **O(n)** extra space."
- "Sorting dominates → **O(n log n)** time."

