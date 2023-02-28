
# O(n)  For removing bcz we have to shifting all the elements


q = []
q.append(10)
q.append(20)
q.append(30)

print(q)

print(q.pop(0))     # 10
print(q.pop(0))
print(q.pop(0))
print(q.pop(0))     # IndexError: pop from empty list

