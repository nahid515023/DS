from collections import deque

q=deque([1,2,3])
q.append(5)
q.appendleft(20)

print(list(q))
print(q.popleft())
print(q.popleft())
print(q.popleft())