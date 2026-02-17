nums=[]
while len(nums)<2:
    nums.extend(map(int, input().split()))
a, b= nums[:3]
if a>b:
    print(a)
elif a==b:
    print(a)
else:
    print(b)