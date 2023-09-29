calorie=[1,3,2]
calorie.sort(reverse=True)
walk=0
for i in range(len(calorie)):
    walk+=(2**i)*calorie[i]
print(walk)