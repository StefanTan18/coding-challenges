def repeated(arr, low, high):
    # only one element in the array
    if low == high:
        return arr[high]
    
    # Find the middle
    mid = (low + high) // 2
    # print("mid: {}".format(mid))

    # Checks if the middle element is repeated
    if (arr[mid] != mid + 1):
        if (mid > 0 and arr[mid] == arr[mid - 1]):
            return mid
        # repeated element must be in the left half of the array
        return repeated(arr, low, mid - 1)
    # repeated element must be in the right half of the array
    return repeated(arr, mid + 1, high)

def main():
    arr1 = [1, 2, 2, 3, 4, 5]
    print("Repeated element of arr1 is: {}".format(repeated(arr1, 0, len(arr1) - 1)))

    arr2 = [1, 2, 3, 4, 5, 5, 7]
    print("Repeated element of arr2 is: {}".format(repeated(arr2, 0, len(arr2) - 1)))

    arr3 = [1, 1, 2, 3, 4, 5, 6]
    print("Repeated element of arr3 is: {}".format(repeated(arr3, 0, len(arr3) - 1)))

if __name__ == "__main__":
    main()