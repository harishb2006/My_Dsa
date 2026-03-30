nums=[9, 5, 4, 2]

count=0
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[j] <  nums[i]:
            count+=1 

print(count)