# from queue import Queue
# class Test:
#     def __init__(self):
#         self.q = Queue()
#         self.front = -1
#         self.rear = -1
#         self.count = 0
    
#     def enQueue(self, data):
#         if self.front == -1:
#             self.front = data
#         self.q.put(data)
#         self.rear = data
#         self.count += 1        
    
#     def deQueue(self):
#         if self.size() > 0:
#             if self.size() > 1:
#                 self.front = self.q[1]
#             else:
#                 self.front = -1
#             self.count -= 1
#             return self.q.get()
#         return -1
    
    
#     def size(self):
#         return self.count
    
#     def isEmpty(self):
#         return self.count == 0
    
#     def frontData(self):
#         return self.front
    
#     def show(self):
#         i = 0
#         while not self.q.empty():
#             print(self.q[i], end=" ")
#             i += 1
    
# queue = Test()
# while True:
#     print("1. Enqueue : ")
#     print("2. Dequeue : ")
#     print("3. Size : ")
#     print("4. IsEmpty : ")
#     print("5. Front : ")
#     print("6. Show : ")
#     print("7. break : ")
#     n = int(input("Choose the option : "))
    
#     if n == 1:
#         queue.enQueue(int(input("Data : ")))
#     elif n == 2:
#         print("Dequeue data is : ",queue.deQueue())
#     elif n == 3:
#         print("Size of queue is :",queue.size())
#     elif n == 4:
#         print("Queue is Empty : ",queue.isEmpty())
#     elif n == 5:
#         print("Front Data is : ", queue.frontData())
#     elif n == 6:
#         queue.show()
#     elif n == 7:
#         break
#     else:
#         print("Invalid Option!")