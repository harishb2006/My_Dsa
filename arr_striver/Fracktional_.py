# cook your dish here


value = [60, 100, 120]
weight= [10, 20, 30]
capacity = 50
# Output: 240 


items=[]


for i in range(len(value)):
    ratio=value[i]/weight[i]
    items.append((ratio,value[i],weight[i]))
    

items.sort(reverse=True)


summ=0

for ratio,value,weight in items:
    
    if capacity >= weight:
        capacity-=weight
        summ+=value 
    else:
        fractional=capacity/weight
        summ+=fractional*value
        break 
print(summ)
        