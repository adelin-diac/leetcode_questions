from collections import deque

"""
QUEUE = FIFO

methods:
- enqueue: add to queue
- dequeue: remove from queue
- peek: see item on top of queue
- is_empty
- length

STACK = LIFO
methods:
- append -> add on top of stack
- pop -> get top of stack

"""


class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        # tmp.extend(self.queue)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0
    

stack = MyStack()

stack.push(1)
stack.push(2)
print(stack.top())
print(stack.pop())
print(stack.empty())
print(stack.queue)