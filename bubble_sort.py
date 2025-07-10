def bubble_sort(arr, n):
    for i in range(n-1):
        for j in range(n-i-1):
            if a[j] > a[j + 1]:
                a[j], a[j+1] = a[j+1], a[j]
a = [48, 74, 21, 36, 22, 9, 21]
n = len(a)
bubble_sort(a, n)
print(a)
