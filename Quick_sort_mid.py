def Quick_sort(arr, left, right):
    i = left
    j = right
    mid = int((left+right)/2)
    piv = arr[mid]
    while i<=j:
        while arr[i]<piv:
            i+=1
        while arr[j]>piv:
            j-=1
        if i<=j:
            arr[i], arr[j] =arr[j],arr[i]
            i+=1
            j-=1
    if i<right:
        Quick_sort(arr,i,right)
    if j>left:
        Quick_sort(arr,left,j)
a = [45,32,57,12,54,77]
n = len(a)
Quick_sort(a,0,n-1)
print(a)
