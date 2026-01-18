nums = [1, 2, 3]

print(nums)

nums.append(4)

print(nums)

nums.pop()

print(nums)

first = nums[0]

print(first)

last = nums[-1]

print(last)

for n in nums:
    print(n)
    
for i in range(len(nums)):
    print(i)
    
for i, val in enumerate(nums):
    print ( i , val)
    
nums.sort()
print(nums)
nums.reverse()
print(nums)
nums_copy = nums[::-1]
print(nums_copy)