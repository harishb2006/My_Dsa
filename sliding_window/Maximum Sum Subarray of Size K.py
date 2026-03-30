

arr= [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4


slide_window=0

for i in range(k):
    slide_window+=arr[i]
    
max_sum=slide_window
for i in range(k,len(arr)):
    slide_window+= arr[i]
    slide_window-=arr[i-k]

    max_sum=max(max_sum,slide_window)
    
print(max_sum)
    
    