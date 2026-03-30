
arr = [5,2,4,6,1]

n=len(arr)

for i in range(n):
    swapped=False
    for j in range(n-i-1):
        
        if arr[j] > arr[j+1]:
            arr[j+1],arr[j]=arr[j],arr[j+1] 
            swapped=True
        
    if not swapped:
        break 

print(arr)
        