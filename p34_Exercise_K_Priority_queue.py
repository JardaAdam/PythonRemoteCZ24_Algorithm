"""Prioritní fronta
Zadání:
Implementujte frontu, která dokáže zpracovávat prioritní prvky.
Prioritní prvky by měly být vždy zpracovány před ne-prioritními prvky,
přičemž pořadí v rámci prioritní nebo ne-prioritní fronty by mělo být FIFO.

prioritní1 neprioritní1 neprioritní2 prioritní2
-> prioritní1 prioritní2 neprioritní1 neprioritní2
"""
from collections import deque


class PriorityQueue:
    def __init__(self):
        self.normal_queue = deque()
        self.priority_queue = deque()

    def enqueue(self, item, priority=False):
        if priority:
            self.priority_queue.append(item)
        else:
            self.normal_queue.append(item)

    def dequeue(self):
        if self.priority_queue:
            return self.priority_queue.popleft()
        if self.normal_queue:
            return self.normal_queue.popleft()
        raise IndexError("Queue is empty.")


if __name__ == '__main__':
    queue = PriorityQueue()
    queue.enqueue("normal task 1")
    queue.enqueue("normal task 2")
    queue.enqueue("priority task 1", True)
    queue.enqueue("priority task 2", True)
    queue.enqueue("normal task 3")
    queue.enqueue("normal task 4")

    print(queue.dequeue())  # "priority task 1"
    print(queue.dequeue())  # "priority task 2"
    print(queue.dequeue())  # "normal task 1"
    print(queue.dequeue())  # "normal task 2"
    print(queue.dequeue())  # "normal task 3"
    print(queue.dequeue())  # "normal task 4"
    print(queue.dequeue())  # IndexError: Queue is empty.
