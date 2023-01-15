#Linear Search
#Given an array of elements where we are searching our target element
#Linear search- we go from 0 to n-1 index's it takes O(N) time in worst case 
#array is no need to be sorted because we check every element in the array
arr =[10,1,20,2,30,3,0,5,4]
target=4
flag=False
for i in range(len(arr)): #going throguh each element 
    if(target==arr[i]): #checking the target is present or not
        flag=True # Found
        break #break the loop 
if(flag):
    print("Element Found")
else:
    print("Element Not Found")