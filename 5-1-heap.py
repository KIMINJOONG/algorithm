class Heap:
    def __init__(self, data):
        self.heap_array = list()
        # 배열을 1부터 시작하기위해 0번째 index에 None
        self.heap_array.append(None) 
        self.heap_array.append(data)

    def move_up(self, inserted_idx):
        if inserted_idx <= 1:
            return False
        
        parent_idx = inserted_idx // 2
        if self.heap_array[inserted_idx] > self.heap_array[parent_idx]:
            return True
        else:
            return False

    def insert(self, data):
        if len(self.heap_array) == 0:
            self.heap_array.append(None) 
            self.heap_array.append(data)
            return True

        self.heap_array.append(data)

        inserted_index = len(self.heap_array) - 1

        while self.move_up(inserted_index):
            parent_idx = inserted_index // 2
            # swap 하는 구문
            self.heap_array[inserted_index], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[inserted_index]
            inserted_index = parent_idx

        return True

heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)

print(heap.heap_array)