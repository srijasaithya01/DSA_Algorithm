def Quick_sort(arr, left, right): #defining the function
    i = left      
    j = right
    mid = int((left+right)/2)
    piv = arr[mid]  
    #Nesting loop
    while i<=j:    #outer loop, while loop
        while arr[i]<piv:   #inner loop 1
            i+=1      #increment
        while arr[j]>piv:    #inner loop 2
            j-=1      #decrement
        if i<=j:
            arr[i], arr[j] =arr[j],arr[i]
            i+=1
            j-=1
    if i<right: 
        Quick_sort(arr,i,right)
    if j>left:
        Quick_sort(arr,left,j)
a = [45,32,57,12,54,77] 
n = len(a)   #number of elements
Quick_sort(a,0,n-1)   #calling function
print(a)  #printing
