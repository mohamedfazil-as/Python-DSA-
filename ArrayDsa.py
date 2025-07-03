#  Array
# import Array
#  syntax --> array('type_code',[])
from  array import  *

arr= array('i',[1,2,3,4,5,6])

a= 4
for i in range(0,len(arr)) :
    if arr[i]==a:
        print(i)
        break



