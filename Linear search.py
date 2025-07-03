#  Linear  Search

array = [1,2,3,4,5,6,7]

x= 8

for i  in  range(0,len(array)):
    if array[i]==x:
        print(i)
        break 
else:
    print("X is  not  present in  array ")