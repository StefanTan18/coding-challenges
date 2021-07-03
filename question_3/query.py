def query_search(q, n, arr):
    # starts searching in the upper right hand corner of the n-square matrix (0, n - 1)
    i = 0
    j = n - 1

    while i < n and j >= 0:
        # query is located 
        if q == arr[i][j]:
            return (i, j)
        # query is found to be less than the current search target so the column to the left is searched
        elif q < arr[i][j]:
            j -= 1
        # query is found to be greater than the current search target so the row to the bottom is searched
        else:
            i += 1

    # query is not located in the array
    return -1

def main():
    arr1 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
    print("5 is located in arr1 at {}".format(query_search(5, 3, arr1)))

    arr1 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
    print("7 is located in arr1 at {}".format(query_search(7, 3, arr1)))

    arr1 = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]]
    print("17 is located in arr1 at {}".format(query_search(17, 4, arr1)))

if __name__ == "__main__":
    main()