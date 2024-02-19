from abc import ABCMeta, abstractmethod

class ClassNameMeta(ABCMeta):
    def __init__(self, name, bases, attrs):
        super().__init__(name, bases, attrs)
        self.class_name = name
        
class SortBase(metaclass = ClassNameMeta):
    @classmethod
    @abstractmethod
    def sort(self, arr):
        pass
    
    @classmethod
    def test(self):
        arr = [12,589,12,781243,7854,43,234,11]
        print(self.class_name)
        self.sort(arr)
        print(arr)
        
class InsertSort(SortBase):
    @classmethod
    def sort(self, arr):
        for i in range(1, len(arr)):
            flag = arr[i]
            
            j = i
            while j > 0 and arr[j - 1] > flag:
                arr[j] = arr[j - 1]
                j -= 1
                
            arr[j] = flag
            
InsertSort.test()

class MergeSort(SortBase):
    @classmethod
    def sort(self, arr):
        self.__sort(arr, 0, len(arr) - 1)
        
        
    @classmethod
    def __sort(self, arr, left, right):
        if left < right:
            mid = (left + right) // 2
            
            self.__sort(arr, left, mid)
            self.__sort(arr, mid + 1, right)
            self.__merge(arr, left, mid, right)
            
    @classmethod
    def __merge(self, arr, left, mid, right):
        left_index = left
        right_index = mid + 1
        data = []
        
        while left_index <= mid and right_index <= right:
            if arr[left_index] <= arr[right_index]:
                data.append(arr[left_index])
                left_index += 1
            else:
                data.append(arr[right_index])
                right_index += 1
        
        while left_index <= mid:
            data.append(arr[left_index])
            left_index += 1
            
        while right_index <= right:
            data.append(arr[right_index])
            right_index += 1
            
        for i in range(left, right + 1):
            arr[i] = data.pop(0)
            
            
MergeSort.test()

class QuickSort(SortBase):
    @classmethod
    def sort(self, arr):
        self.__sort(arr, 0, len(arr) - 1)
    
    @classmethod
    def __sort(self, arr, left, right):
        left_index = left
        right_index = right
        flag = arr[left]
        
        while left_index < right_index:
            while left_index < right_index and arr[right_index] >= flag:
                right_index -= 1
            if left_index < right_index and arr[right_index] < flag:
                arr[left_index], arr[right_index] = arr[right_index], arr[left_index]
                
            while left_index < right_index and arr[left_index] <= flag:
                left_index += 1
            if left_index < right_index and arr[left_index] > flag:
                arr[left_index], arr[right_index] = arr[right_index], arr[left_index]
        
        if left < left_index:
            self.__sort(arr, left, left_index - 1)
        if right_index < right:
            self.__sort(arr, right_index + 1, right)
            
QuickSort.test()

class BubblingSort(SortBase):
    @classmethod
    def sort(self, arr):
        for i in range(len(arr) - 1):
            for j in range(len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

BubblingSort.test()
