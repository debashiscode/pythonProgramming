def liniear_search(A, N, x):
    i = -1
    pos = -1
    while i<N:
        if A[i] == x:
            pos = i
            break
        i = i + 1
    return pos



# Binary Search Function
def binary_search(A, L, R, val):
    beg = L
    end = R
    POS = -1
    while beg <= end:
        mid = (beg+end)//2
        if A[mid] == val:
            POS = mid
            break
        elif A[mid] > val:
            end = mid - 1
        else:
            beg = mid + 1
    if POS == -1:
        print("Value is not present")
    return POS



if __name__ == "__main__":
    arr = [10, 8, 2, 7, 3, 4, 9, 1, 6, 5]
    x = 9
    N = len(arr)
    linear_search_result = liniear_search(arr, N, x)
    if linear_search_result == -1:
        print("Element is not present in array")
    else:
        print("Element is present at index", linear_search_result)

    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    beg = 0
    end = len(arr) - 1
    val = 9
    binary_search_result = binary_search(arr, beg, end, val)
    if binary_search_result == -1:
        print("Element is not present in array")
    else:
        print("Element is present at index", binary_search_result)