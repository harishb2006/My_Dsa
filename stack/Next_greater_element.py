# cook your dish here


nums = [2,1,2,4,3]


# [4,2,4,-1,-1]

stack = []

n = len(nums)

res = n * [-1]


for i in range(n-1 , -1 , -1):
    
    while stack and stack[-1] <= nums[i]:
        stack.pop()
        
    
    if stack :
        res[i]=stack[-1]
        
    stack.append(nums[i])     
    
print(res)  

