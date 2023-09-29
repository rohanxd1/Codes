grid=['mpxz', 'abcd', 'wlmf']
sortgrid=[]
check=[]
elem=''
for i in grid:
    elem=''.join(sorted(i))
    sortgrid.append(elem)
    check.append(elem)
    elem.replace(elem,'')
check.sort()
print(sortgrid[:])
print(check[:])
if sortgrid[:]==check[:]:
    print("YEs")
else:
    print("NO")