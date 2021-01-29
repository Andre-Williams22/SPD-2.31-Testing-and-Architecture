def insertion_sort(arr):
    """Performs an Insertion Sort on the array arr."""
    for i in range(1, len(arr)):
        key = arr[i] 

        j = i-1
 #            2     5
        while key < arr[j] and j >= 0: 
            # swap(key, j, arr)
           #   6         5 
            arr[j+1] = arr[j] 
            
            j -= 1
        arr[j+1] = key
    return arr

def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]


if __name__ == '__main__':
    print('### Insertion Sort ###')
    answer = insertion_sort([5, 2, 3, 1, 6])
    print(answer)