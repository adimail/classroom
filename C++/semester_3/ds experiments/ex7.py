class SortingAlgorithms:

    def BubbleSort(self, arr):
        length = len(arr)

        for i in range(length - 1):
            swapped = False
            for j in range(length - 1 - i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                break

        return arr

    def InsertionSort(self, arr):
        length = len(arr)

        for i in range(1, length):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

        return arr
    
    def SelectionSort(self, arr):
        length = len(arr)

        for i in range(length - 1):
            for j in range(i + 1, length):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
        return arr
    
    def QuickSort(self, arr):
        if len(arr) <= 1:
            return arr

        pivot = arr[len(arr) // 2]  # Choose a pivot element
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        return self.QuickSort(left) + middle + self.QuickSort(right)
    
    def mergeSort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2  # Find the middle of the array
            left_half = arr[:mid]  # Split the array into two halves
            right_half = arr[mid:]

            self.mergeSort(left_half)  # Recursively sort the left half
            self.mergeSort(right_half)  # Recursively sort the right half

            # Merge the two sorted halves
            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1
        return arr
    
    def HeapSort(self, arr):
        return arr


def main():
    sort = SortingAlgorithms()

    arr = [8,5,5,2,8,4]

    # print(sort.BubbleSort(arr))       #passed
    # print(sort.InsertionSort(arr))    #passed
    # print(sort.SelectionSort(arr))    #passed
    # print(sort.QuickSort(arr))        #passed
    print(sort.mergeSort(arr))

if __name__ == '__main__':
    main()