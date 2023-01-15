#Binary Search -O(logN)
a=[1,2,3,4,5,6,7,8,9,10] # The array is sorted
Target=10
low =0 
high=len(a)-1
while(low<=high): # if condition fails then we gone through whole array
    mid =low+(high-low)//2
    if(a[mid]==Target):
        print("Element Found")
        break
    elif(a[mid]<Target):
        low=mid+1
    elif(a[mid]>Target):
        high=mid-1