import sys
import random;
def sort_using_algorithm(data, algorithm):
    # This function takes the algorithm identifier as input
    # However, it always uses the sorted function in Python
    if algorithm == 1:
        sorted_data = InsertionSort(data)
    elif algorithm == 2:
        sorted_data = ShellSort(data)
    elif algorithm == 3:
        sorted_data = SelectionSort(data)
    elif algorithm == 4:
        sorted_data = HeapSort(data)
    elif algorithm == 5:
        sorted_data = QuickSortLeftPivot(data, 0, len(data)-1)
    elif algorithm == 6:
        sorted_data = QuickSortRandomPivot(data, 0, len(data)-1)
    else:
        print("Invalid algorithm number.")
        sys.exit(1)

    return sorted_data

def InsertionSort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and temp < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp
    return arr
      
def ShellSort(arr):
    n = len(arr)
    gaps = [1]
    k = 0
    while True:
        gap = 4**(k+1) + 3*2**(k+1)
        if gap >= n:
            break
        gaps.append(gap)
        k += 1
    gaps.reverse()
    
    for gap in gaps:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
    return arr
def SelectionSort(arr):
    l = len(arr)
    for i in range(l-1):
        min = i 
        for j in range(i+1,l):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr
def tree(arr,l,i):
    largest = i
    left = 2 * i + 1 #lewy odłam drzewa
    right = 2 * i + 2 #prawy odłam drzewa 
    # l to len array
    if left < l and arr[i] < arr[left]:
        largest = left
        
    if right < l and arr[largest] < arr[right]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        tree(arr, l, largest)
        
def HeapSort(arr):
    l = len(arr)
    
    for i in range(l//2, -1, -1):
        tree(arr, l, i)
    
    for i in range(l-1,0,-1):
        arr[i], arr[0] = arr[0], arr[i]
        tree(arr,i,0)
    return arr
def QuickSortLeftPivot(arr, start, end):
    if start < end:
        pivot_index = Partition(arr, start, end)
        QuickSortLeftPivot(arr, start, pivot_index - 1)
        QuickSortLeftPivot(arr, pivot_index + 1, end)
    return arr
def Partition(arr, start, end):
    pivot = arr[start]
    left = start + 1
    right = end
    
    while True:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and arr[right] >= pivot:
            right -= 1
        if left > right:
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]
    
    arr[start], arr[right] = arr[right], arr[start]
    return right
def QuickSortRandomPivot(arr, start, end):
    if start < end:
        pivot_index = PartitionRandomPivot(arr, start, end)
        QuickSortRandomPivot(arr, start, pivot_index - 1)
        QuickSortRandomPivot(arr, pivot_index + 1, end)
    return arr

def PartitionRandomPivot(arr, start, end):
    pivot_index = random.randint(start, end)
    pivot = arr[pivot_index]
    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]
    i = start - 1
    for j in range(start, end):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    i += 1
    arr[i], arr[end] = arr[end], arr[i]
    return i


def main():
    # Command-line arguments: python script.py --algorithm <algorithm_number>
    if len(sys.argv) != 3 or sys.argv[1] != "--algorithm":
        print("Usage: python script.py --algorithm <algorithm_number>")
        sys.exit(1)

    algorithm_number = int(sys.argv[2])

    # Read input data from standard input until the end of file (EOF)
    input=sys.stdin.read().split()
    try:
        data = [int(x) for x in input[1:]]
    except EOFError:
        print("Error reading input.")

    # Perform sorting using the specified algorithm (ignored in this example)
    sorted_data = sort_using_algorithm(data, algorithm_number)

    # Print the sorted data
    print("Sorted data:", sorted_data[0:100])

if __name__ == "__main__":
    main()


