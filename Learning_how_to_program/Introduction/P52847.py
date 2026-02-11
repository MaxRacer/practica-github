nums=[]
while len(nums)<3:
    nums.extend(map(int, input().split()))
a, b, c= nums[:3]
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)
