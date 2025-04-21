nums=input().split()#10 13 20 23 20 17
max1=float('-inf')
min1=float('inf')
for digits in nums:
    num =int(digits)
    if num>1:
        for j in range(2,(num//2)+1):
            if num%j==0:
                break
        else:
            if num>max1:
                max1=num
            if num<min1:
                 min1=num
print(max1+min1)
