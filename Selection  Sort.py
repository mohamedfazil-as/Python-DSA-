# Selection Sort

arr = [15,10,20,5,3,1]

#  used for  position
for pos in  range(len(arr)-1):
    min = pos # put  the  minmum  value  insude the  loop
    # for this loop  declare  the value  after  the pos till  the last  value
    for  i in  range(pos+1,len(arr)):
        if arr[i]<arr[min]:
            min =  i

    arr[min],arr[pos] = arr[pos],arr[min]

print(arr)