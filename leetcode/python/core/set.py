seen = set()

seen.add(1)
seen.add(2)
print(seen)

seen.remove(1)
seen.discard(3)

print(seen)

exists = 1 in seen

print(exists)