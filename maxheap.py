class MaxHeap:
    def __init__(self):
        '''
        Initilizes an empty list.
        '''
        self.heap = []

    def _parent(self, index):
        '''
        Formula to find parrent index in list.
        '''
        return (index - 1) // 2

    def _left_child(self, index):
        '''
        Formula to find left child index in list
        '''
        return 2 * index + 1

    def _right_child(self, index):
        '''
        Formula to find right child index in list
        '''
        return 2 * index + 2

    def add(self, entry):
        '''
        Takes in entry and appends it to the back of the list and calls the upheap with appended index.
        '''
        self.heap.append(entry)
        self._upheap(len(self.heap) - 1)

    def _upheap(self, index):
        '''
        Takes in an index and if their is an item in list it will check to see if its bigger than the parent and upheap if needed.
        Parent takes place of upheaped item.
        '''
        while index > 0:
            parent_index = self._parent(index)
            if self.heap[index] > self.heap[parent_index]:
                temp = self.heap[index]
                self.heap[index] = self.heap[parent_index]
                self.heap[parent_index] = temp
                index = parent_index
            else:
                break

    def _downheap(self, index):
        '''
        Takes in index and compares with the left child and compares with right child.
        If the largest is still in the current index it'll stop and the current element will swap with the largest child.
        Then it moves down to the largest child's index and repeats.
        '''
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)
            largest = index
            if left_index < len(self.heap) and self.heap[left_index] > self.heap[largest]:
                largest = left_index
            if right_index < len(self.heap) and self.heap[right_index] > self.heap[largest]:
                largest = right_index
            if largest == index:
                break
            temp = self.heap[index]
            self.heap[index] = self.heap[largest]
            self.heap[largest] = temp
            index = largest

    def pop(self):
        '''
        Raises an error if heap is empty and if not then takes out the first item in the list.
        It replaces the root with the last item in the list then calls the downheap if its not the only item to ensure the max is at the top.
        '''
        if len(self.heap) == 0:
            raise IndexError('Cannot remove from empty heap')
        temp = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap[-1] = temp
        entry = self.heap.pop()
        if len(self.heap) > 0:
            self._downheap(0)
        return entry

    def peek(self):
        '''
        Returns the root and errors if empty.
        '''
        if len(self.heap) == 0:
            raise IndexError('Nothing in list')
        return self.heap[0]

    def count(self):
        '''
        Return the count of items in list.
        '''
        return len(self.heap)