import queue

# data_queue = queue.Queue()
# data_queue.put("funcoding")
# data_queue.put(1)
# print(data_queue.qsize()) # return 2
# print(data_queue.get()) # return 'funcoding'
# print(data_queue.qsize()) # return 1
# print(data_queue.get()) # return 1

# data_queue = queue.LifoQueue()
# data_queue.put('funcoding')
# data_queue.put(1)
# print(data_queue.qsize()) # return 2
# print(data_queue.get()) # return 1
# print(data_queue.get()) # return 'funcoding'

# data_queue = queue.PriorityQueue()
# data_queue.put((10, "korea"))
# data_queue.put((5, 1))
# data_queue.put((15, "china"))
# print(data_queue.qsize()) # return 3 
# print(data_queue.get()) # return (5, 1)
# print(data_queue.get())
# print(data_queue.get())

# queue_list = list()

# def enqueue(data):
#     queue_list.append(data)

# def dequeue():
#     data = queue_list[0]
#     del queue_list[0]
#     return data

# for index in range(10):
#     enqueue(index)

# print(len(queue_list))
# print(dequeue())
# print(dequeue())
# print(dequeue())


queue_list = list()

def enqueue(data):
    queue_list.append(data)

def dequeue():
    data = queue_list[0]
    del queue_list[0]
    return data

for index in range(10):
    enqueue(index)

print(queue_list)

print(dequeue()) 
print(dequeue())