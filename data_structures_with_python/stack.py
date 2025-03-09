from listNode import ListNode
from linkedList import DoublyLinkedList
    
class Stack:
    def __init__(self, iterable = []):
        self.list = DoublyLinkedList(iterable)
    def __str__(self):
        return f"{self.__class__.__name__} [{self.list.numItems}, t({self.list.tail}) :" + '->'.join([ f"{node.item}" for node in self.list ]) + "]"
    def push(self, val):
        self.list.push_back(val)
    def pop(self):
        return self.list.pop_back()
    def top(self):
        return self.list.at(-1)
    def isEmpty(self):
        return self.list.isEmpty()
    def popAll(self):
        self.list.clear()
    def size(self) -> int:
        return self.list.size()
    def clear(self):
        return self.list.popAll()
    def extend(self, other):
        for node in other:
            if isinstance(node, ListNode):
                self.list.push_back( node.item )
            else:
                self.list.push_back(node)
    def copy(self):
        return self[:]
    def __iter__(self):
        return Iterator(self.list)
    def __getitem__(self, i):
        if isinstance(i, slice):
            start, stop, step = i.indices(self.list.size())
            return self.__class__([ self.list.at(index) for index in range(start, stop, step) ] )        
        return self.list.at(i)
    
class Iterator:
    def __init__(self, iterable):
        self.list = iterable
        self.it = iterable.at(0)
    def __next__(self):
        if self.it is None:
            raise StopIteration        
        node = self.it
        self.it = None if self.list.equalLast(node) else self.it.next
        return node

if __name__ == '__main__':
    stack = Stack(['k', 'l','m'])

    stack.push('a')
    print('push a', stack)
    stack.push('b')
    print('push b', stack)
    stack.push('e')
    print('push e', stack)
    stack.push('e')
    print('push e', stack)
    stack.pop()
    print('pop', stack)
    stack.pop()
    print('pop', stack)
    print('top', stack.top())
    print('list', stack)

    stack.popAll()
    print('pop all', stack)
