s = "leetcode"
print(s)

first_char = s[0]
last_char = s[-1]
length = len(s)
print(first_char)
print(last_char)
print(length)

chars = list(s)
print(chars)

joined = "".join(chars)

print(joined)

s_lower = s.lower()
s_upper = s.upper()

print(s_lower)
print(s_upper)

words = "ab bc cd".split(" ")
print(words)

is_palindrome = s == s[::-1]
print (is_palindrome)