#  Bubble  sort

arr = [1,10,20,5,3]


for  i in range(0,len(arr)-1): #How many  rounds
    for j in range(0,len(arr)-1): # use to  comapre  each  value  in each  round
        if arr[j]<arr[j+1]:
            continue
        elif arr[j]>arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]



print(arr)

