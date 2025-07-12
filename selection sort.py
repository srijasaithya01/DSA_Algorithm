def selection_sort(a):        #define the function
    n = len(a)
    for i in range(n-1):    #outer loop i from 0 to n-1
        min = i
        for j in range(i+1,n):    #inner loop  j from i+1(0+1) to n
            if a[j] < a[min]:
                min = j
        a[i],a[min] = a[min],a[i]
a = [25, 56, 76, 33, 12]
selection_sort(a)
print(a)
