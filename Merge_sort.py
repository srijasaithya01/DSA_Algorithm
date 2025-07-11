def Merge_sort(arr):    #defining the function
    if len(arr) > 1:    #checking the if the list has more than one element
        mid = len(arr)//2   #splitting into two halves
        left = arr[:mid]
        right = arr[mid:]
        Merge_sort(left)     #recursive or sorting
        Merge_sort(right)
        i = j = k = 0       #i->left list,j->for right list, k-> main arr
        while i<len(left) and j <len(right):    #compares elements from both parts and merges in order
            if left[i] < right[j]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
            k+=1   #moves to the next position in array
        while i < len(left):    #copy remaining left elements into main array
            arr[k] = left[i]
            i+=1
            k+=1
        while j<len(right):     #copy remaining right elements into main array
            arr[k] = right[j]
            j+=1
            k+=1
a = [6,3,5,2,4,8,10,1]
Merge_sort(a) #calling the function
print(a)
