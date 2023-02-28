

# append():-        This function is used to insert the value in its argument to the right end of the deque.
# appendleft():-    This function is used to insert the value in its argument to the left end of the deque.
# pop():-           This function is used to delete an argument from the right end of the deque.
# popleft():-       This function is used to delete an argument from the left end of the deque.
# index(ele, beg, end):- This function returns the first index of the value mentioned in arguments, starting searching from beg till end index.
# insert(i, a) :-   This function inserts the value mentioned in arguments(a) at index(i) specified in arguments.
# remove():-        This function removes the first occurrence of the value mentioned in arguments.
# count():-         This function counts the number of occurrences of value mentioned in arguments.
# len(dequeue):-    Return the current size of the dequeue.
# Deque[0] :-       We can access the front element of the deque using indexing with de[0].
# Deque[-1] :-      We can access the back element of the deque using indexing with de[-1].



from collections import deque

# q = deque()       # empty queue
q = deque([10,20])

q.append(30)        # [10, 20, 30]
q.appendleft(90)    # [90, 10, 20, 30]

print(q)        # [90, 10, 20, 30]


q.pop()     # 30 
print(q)    # [90, 10, 20]

q.popleft() # 90
print(q)    # [10,20]

print(q[0], q[-1])      # front and rear  

print(len(q))   # 2

q.append(10)
print(q.count(10))  # 2  count 10 and Found 2 times 10 in queue

q.append(40)
print(q)    # [10,20,10,40]

print(q.index(10,1,3))  # 2 bcz it got 10 at index 2 according our start point


print(q.remove(10))
print(q)       # [20, 10, 40]