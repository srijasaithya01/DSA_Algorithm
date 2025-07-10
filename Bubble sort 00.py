#Bubble Sort
def bubble_sort(arr, n): #defining
    for i in range(n-1):    #Outer loop   i=> passes
        for j in range(n-i-1):   #Inner loop  j=> position
             if a[j] > a[j+1]:
                 a[j], a[j+1] = a[j+1], a[j]
a = [2, 56, 45, 13, 9, 1] #array
n = len(a) #length => no. of elements
bubble_sort(a,n) #calling the function
print(a) #printing

