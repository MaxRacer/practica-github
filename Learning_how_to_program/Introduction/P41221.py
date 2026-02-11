nums=[]
while len(nums)<3:
    nums.extend(map(int, input().split()))
a, b, c = nums[:3]
print(a + b + c)
