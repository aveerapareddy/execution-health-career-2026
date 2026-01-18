s = "aabbc"
freq = {}
print(freq)

for c in s:
    freq[c] = freq.get(c , 0)+1
    
print(freq)

for key, value in freq.items():
    print(key, value)
    
exists = "a" in freq

print(exists)