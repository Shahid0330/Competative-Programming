#prefix sum
#finding a sum of sub array of indexes l to r
#brute fore approach
def prefix_sum_bruteforce(a,l,r):
    #brute force we just start the for loop from l and end to r this take O(N) times
    s=0
    for i in range(l,r+1):
        s=s+a[i]
    return s
a=[1,2,3,4,5,6,7,8,9,10]
l=5
r=9
output=prefix_sum_bruteforce(a,l,r)
print(output)
#we can optimize this code by doing some preprocessing.
def prefix_sum_optimize(a,l,r):
    for i in range(1,len(a)):
        a[i]=a[i]+a[i-1]
    if(l>0):
        out=a[r]-a[l-1]
        return out
    return a[r]
out=prefix_sum_optimize(a,l,r)
print(out)
