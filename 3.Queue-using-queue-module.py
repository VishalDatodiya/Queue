# put(item) - This function is used to insert element to the queue.
# get() - This function is used to extract the element from the queue.
# empty() - This function is used to check whether a queue is empty or not. It returns true if queue is empty.
# qsize() - This function returns the length of the queue.
# full() - If the queue is full returns true; otherwise false.



from queue import Queue

q = Queue(maxsize=3)

print(q)

q.put(10)
q.put(20)
q.put(30)
# q.put(199)    # if we try to put 4th element then it will stuck

print(q.full())     # True
print(q.qsize())    # 3


print(q.get())      # 10

print(q.full())     # False
print(q.qsize())    # 2


print(q.get())      # 20
print(q.get())      # 30

print(q.full())     # False
print(q.qsize())    # 0
print(q.empty())    # True