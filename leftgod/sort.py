import random


class SortFunction(object):
    def __init__(self):
        pass

    # 1. select sort
    # 时间复杂度O(n2)，空间复杂度O(1)

    def select_sort(self, arr):
        if not arr or len(arr) < 2:
            return arr
        min_index = 0
        for i in range(len(arr) - 1):
            print(arr)
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_index]:
                    min_index = j
            print(i, min_index)
            self.swap(arr, i, min_index)
        return arr

    # 2. bubble sort
    # 时间复杂度O(n2)，空间复杂度O(1)
    def bubble_sort(self, arr):
        if not arr or len(arr) < 2:
            return arr
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] > arr[j]:
                    self.swap(arr, i, j)
        return arr

    # 3. insert sort
    # 时间复杂度O(n2)，空间复杂度O(1)
    def insert_sort(self, arr):
        if not arr or len(arr) < 2:
            return arr
        for i in range(1, len(arr)):
            cur_idx = i - 1
            # print(cur_idx)
            while cur_idx >= 0 and arr[cur_idx] > arr[i]:
                self.swap(arr, i, cur_idx)
                i = cur_idx
                cur_idx -= 1
        return arr

    def qs(self, arr, left, right):
        if not arr or left > right:
            return
        if left == right:
            return arr
        i = left
        j = right
        p = arr[i]
        while i < j:
            while i < j and arr[j] >= p:
                j -= 1
            while i < j and arr[i] <= p:
                i += 1
            if i != j:
                self.swap(arr, i, j)
            else:
                self.swap(arr, left, i)
        self.qs(arr, left, i)
        self.qs(arr, i + 1, right)
        return arr

    # 5. 堆排序时间复杂度O(NlogN),空间复杂度O(1)
    def heap_sort(self, arr):
        pass
    # 6. 时间复杂度，空间复杂度
    def merge_sort(self, myList):
        if len(myList) > 1:
            mid = len(myList) // 2
            left = myList[:mid]
            right = myList[mid:]

            # Recursive call on each half
            self.merge_sort(left)
            self.merge_sort(right)

            # Two iterators for traversing the two halves
            i = 0
            j = 0

            # Iterator for the main list
            k = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    # The value from the left half has been used
                    myList[k] = left[i]
                    # Move the iterator forward
                    i += 1
                else:
                    myList[k] = right[j]
                    j += 1
                # Move to the next slot
                k += 1

            # For all the remaining values
            while i < len(left):
                myList[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                myList[k] = right[j]
                j += 1
                k += 1
        return myList

    def swap(self, arr, i, j):
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp


def comparator(arr):
    return sorted(arr)


def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list


if __name__ == "__main__":
    li = [89, 13, 32, 12, 1, 3, 9, 0]
    # print(select_sort(li))
    # print(bubble_sort(li))
    sort_func = SortFunction()
    # print(sort_func.insert_sort(li))
    times = 10

    for i in range(times):
        start = random.randrange(1, 100, 1)
        stop = random.randrange(1, 100, 1)
        length = random.randrange(1, 100, 1)
        arr = random_int_list(start, stop, length)
        # print(arr)
        # print(comparator(arr))
        if comparator(arr) != sort_func.qs(arr, 0, len(arr)-1):
            print("there is an error!")
        else:
            print("succeed!")
