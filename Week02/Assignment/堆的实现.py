class BinaryHeap:
    def __init__(self, capacity):
        self.d = 2
        self.heap = [-1 for _ in range(capacity)]
        self.heapSize = 0

    def isEmpty(self):
        return self.heapSize == 0

    def isFull(self):
        return self.heapSize == len(self.heap)

    def parent(self, i):
        return int((i - 1) / self.d)

    def kthChild(self, i, k):
        return 2 * i + k

    def insert(self, x):
        if self.isFull(): return False
        self.heap[self.heapSize] = x
        self.heapSize += 1
        self.heapifyUp(self.heapSize - 1)

    def delete(self, x):
        if self.isEmpty(): return False
        maxElement = self.heap[x]
        self.heap[x] = self.heap[self.heapSize - 1]
        self.heapSize -= 1
        self.heapifyDown(x)
        return maxElement

    # Maintains the heap property while inserting an element.
    def heapifyUp(self, i):
        insertValue = self.heap[i]
        while i > 0 and insertValue > self.heap[self.parent(i)]:
            self.heap[i] = self.heap[self.parent(i)]
            i = self.parent(i)
        self.heap[i] = insertValue

    # Maintains the heap property while deleting an element.
    def heapifyDown(self, i):
        temp = self.heap[i]
        while self.kthChild(i, 1) < self.heapSize:
            child = self.maxChild(i)
            if temp >= self.kthChild(): break
            self.heap[i] = self.heap[child]
            i = child

    def maxChild(self, i):

        leftChild = self.kthChild(i, 1);
        rightChild = self.kthChild(i, 2);
        return leftChild if self.heap[leftChild] > self.heap[rightChild] else rightChild


if __name__ == '__main__':
    headp = BinaryHeap(10)
    headp.insert(10)
    headp.insert(4)
    headp.insert(9)
    headp.insert(1)
    headp.insert(7)
    headp.insert(5)
    headp.insert(3)
    headp.delete(5)
    headp.delete(2)
    print
