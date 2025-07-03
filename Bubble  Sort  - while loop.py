#  Bubble  sort - while loop

arr = [1,10,20,5,3]
while (True):
    a = True
    for j in range(0, len(arr) - 1):  # use to  comapre  each  value  in each  round
        if arr[j] < arr[j + 1]:
            continue
        elif arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
        a=  False
    if a==False:
        continue
    elif a==True:
        break

print(arr)