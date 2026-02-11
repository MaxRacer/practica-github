nums=[]
while len(nums)<2:
    nums.extend(map(int, input().split()))
a, b = nums[:2]
print(a + b)
