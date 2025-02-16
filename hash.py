
arr = [1, 2, 1, 2, 3]
hashing = {}

for i in arr:
    if i not in hashing:
        hashing[i] = 1
    else:
        hashing[i] += 1

print(hashing)

s = "abcabaabacb"
hasher = {}
for i in s:
    if i not in hasher:
        hasher[i] = 1
    else:
        hasher[i] += 1
print(hasher)