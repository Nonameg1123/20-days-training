from collections import defaultdict,Counter
s=defaultdict(int)
ip="abcd"
d="polikujmnhytgbvfredcxswqaz"
n=Counter(ip)
sol=""
print(n)
for i in d:
    if i in ip:
        sol+=i*n[i]
print(sol)


