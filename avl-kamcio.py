#Posortuj rosnąco ciąg kluczy, które wstawisz do drzewa BST (metoda sortowania dowolna)
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

#Wybierz środkowy element ciągu (= mediana ) jako element bieżący E

def Mediana(arr):
    return arr[len(arr)//2]