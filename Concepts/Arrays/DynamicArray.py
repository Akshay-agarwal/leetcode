import sys
import ctypes

class DynamicArray(object):
    '''An Array implementation of python list'''

    def __init__(self):
        '''Create a new array'''
        self._n = 0  # Initialize the length of Array to 0
        self._capacity = 1  # Initialize capacity of Array to 1
        self._A = self._make_array(self._capacity)  # Create a new array with the size as capacity of the array

    def _make_array(self, c):
        '''Create a new array of capcity c'''
        return (c * ctypes.py_object)()

    def __len__(self):
        '''Calculate the number of elements in the array'''
        return self._n

    def __getitem__(self, k):
        '''Get an element of array at Index k'''
        if not 0 < k <= self._n:  # Check if index k is less than the length of the array
            return IndexError('Provide proper index')
        return self._A[k]

    def append(self, item):
        '''Append an item at the end of the array'''
        if self._n == self._capacity:  # No more space
            self.resize(2 * self._capacity)  # Double the size of the array
        self._A[self._n] = item
        self._n += 1

    def resize(self, capacity):
        '''Resize the size of the array with the given capacity'''
        B = self._make_array(capacity)  # Create a new Array as per the capacity provided
        for i in range(self._n):  # Add elements of A to B
            B[i] = self._A[i]
        self._A = B  # Reference A to B
        self._capacity = capacity

    def remove(self, value):
        '''Remove the first element with the value'''
        for j in range(self._n):
            if self._A[j] == value:
                for k in range(j, self._n-1):  #If value found in the array then move all elements till end left by one
                    self._A[k] = self._A[k+1]
                self._A[self._n - 1] = None
                self._n -= 1
                return
            raise ValueError('Value not found in array') #If value not found return ValueError.

    def insert(self, k, value):
        '''Insert a value at index k'''
        if self._n == self._capacity:       #not enough space
            self.resize(2 * self._capacity) #double the size of Array
        for j in range(self._n, k, -1):
            self._A[j] = self._A[j-1]       #push each element till index k right by 1
        self._A[k] = value                  #set the value at index k
        self._n += 1

d = DynamicArray()
p = DynamicArray()
print(d,p)
d.append(2)