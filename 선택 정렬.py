def selection_sort(n):
    arr = list(map(int, input("입력하세요: ").split()))
    stack = []
    for i in range(n):
        for j in range(i+1,n-1):
            if arr[i] > arr[j]:
                stack.append(arr[i])
                arr[i] = arr[j]
                arr[j] = stack[-1]
        print(arr)
    return arr
print(selection_sort(6))
