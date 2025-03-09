from listNode import ListNode

class SinglyLinkedListDummy:
    def __init__(self, iterable = []):
        self.head = ListNode('dummy', selfContained = False)
        self.numItems = 0
        self.extend(iterable)
    def __str__(self):
        return f"{self.__class__.__name__} [{self.numItems}, h{self.head}:" + '->'.join([ f" {node.item}" for node in self ]) + "]"
    def at(self, pos: int):
        if pos < 0:
            pos += self.numItems
            if pos < 0:
                pos = 0
        elif pos >= self.numItems:
            pos = self.numItems
        prev = self.head
        node = self.head.next
        for i in range(pos):
            prev = node
            node = node.next
        return (prev, node)                
    def __insert(self, pos: int, newNode: ListNode):
        if newNode is None:
            return
        prev, node = self.at(pos)
        prev.next = newNode
        newNode.next = node
        self.numItems += 1
    def insert(self, pos: int, value):
        self.__insert( pos, ListNode(value, selfContained=False) )
    def push_back(self, newNode: ListNode):
        self.__insert(self.numItems, newNode)        
    def push_front(self, newNode: ListNode):
        self.__insert(0, newNode)
    def append(self, newNode: ListNode):
        self.__insert(self.numItems, newNode)
    def find(self, value):
        prev = self.head
        for node in self:
            if node.item == value:
                return (prev, node)
            prev = node
        return (None, None)
    def pop(self, pos: int = -1):
        prev, node = self.at(pos)
        if node == None:
            return None
        prev.next = node.next    
        node.next = None
        self.numItems -= 1
        return node.item            
    def remove(self, value):
        prev, node = self.find(value)
        if prev == None:
            return
        prev.next = node.next    
        node.next = None
        self.numItems -= 1
    def index(self, value):
        pos = 0
        for node in self:
            if node.item == value:
                return pos
            pos += 1
        raise StopIteration
    def isEmpty(self) -> bool:
        return self.numItems == 0
    def size(self) -> int:
        return self.numItems
    def clear(self):
        while self.isEmpty() == False:
            self.pop()
    def count(self, value) -> int:
        cnt = 0
        for node in self:
            if node.item == value:
                cnt += 1
        return cnt
    def extend(self, other):
        for node in other:
            if isinstance(node, ListNode):
                self.append( ListNode(node.item, selfContained=False))
            else:
                self.append( ListNode(node, selfContained=False))
    def copy(self):
        newSll = self.__class__()
        for node in self:
            newSll.append( ListNode(node.item, selfContained=False))
        return newSll
    def reverse(self):
        for i in range( self.numItems // 2 ):
            f = self.at(i)[1]
            t = self.at(-1-i)[1]
            f.item, t.item = t.item, f.item
    def sort(self):
        lst = []
        for node in self:
            lst.append(node.item)
        self.clear()
        lst.sort()
        self.extend(lst)
    def __iter__(self):
        return Iterator(self)
    def __getitem__(self, i):
        if isinstance(i, slice):
            start, stop, step = i.indices(self.numItems)
            return self.__class__([ self.at(index)[1] for index in range(start, stop, step) ] )
        return self.at(i)[1]

class SinglyLinkedList:
    def __init__(self, iterable):
        self.tail = None
        self.numItems = 0
        self.extend(iterable)
    def __str__(self):
        return f"{self.__class__.__name__} [{self.numItems}, t{self.tail}:" + '->'.join([ f" {node.item}" for node in self ]) + "]"
    def at(self, pos: int):
        if pos < 0:
            pos += self.numItems
            if pos < 0:
                pos = 0
        elif pos >= self.numItems:
            pos = self.numItems
        if self.tail is None:
            return (None, None)
        prev = node = self.tail.next
        for _ in range(pos):
            prev = node
            node = node.next
        return (prev, node)                
    def __insert(self, pos: int, newNode: ListNode):
        if newNode is None:
            return
        prev, node = self.at(pos)
        if prev == node:
            if self.tail is None:
                self.tail = newNode
            else:
                newNode.next = self.tail.next
                self.tail.next = newNode  
        else:
            if prev == self.tail:
                newNode.next = prev.next
                self.tail = newNode
            else:
                newNode.next = node
            prev.next = newNode
        self.numItems += 1
    def insert(self, pos: int, value):
        self.__insert( pos, ListNode(value) )
    def push_back(self, newNode: ListNode):
        if self.tail is None:
            newNode.next = newNode
        else:
            newNode.next = self.tail.next
            self.tail.next = newNode
        self.tail = newNode
        self.numItems += 1
    def push_front(self, newNode: ListNode):
        if self.tail is None:
            newNode.next = newNode
            self.tail = newNode
        else:
            newNode.next = self.tail.next
            self.tail.next = newNode
        self.numItems += 1
    def append(self, newNode: ListNode):
        self.push_back(newNode)
    def find(self, value):
        if self.tail is None:
            return (None, None)
        prev = self.tail.next
        for node in self:
            if node.item == value:
                return (prev, node)
            prev = node
        return (None, None)
    def pop(self, pos: int = -1):
        if self.tail is None:
            return
        prev, node = self.at(pos)
        if prev == node:
            if self.tail == node:
                self.tail = None
            else:
                self.tail.next = prev.next
        else:
            if self.tail == node:
                self.tail = prev
            prev.next = node.next
        self.numItems -= 1
        return node.item
    def remove(self, value):
        if self.tail is None:
            return
        prev, node = self.find(value)
        if prev == None:
            return
        if prev == node:
            if self.tail == node:
                self.tail = None
            else:
                self.tail.next = prev.next
            self.numItems -= 1
            return
        if self.tail == node:
            self.tail = prev
        prev.next = node.next
        self.numItems -= 1
    def index(self, value):
        pos = 0
        for node in self:
            if node.item == value:
                return pos
            pos += 1
        raise None
    def isEmpty(self) -> bool:
        return self.numItems == 0
    def size(self) -> int:
        return self.numItems
    def clear(self):
        while self.isEmpty() == False:
            self.pop()
    def count(self, value) -> int:
        cnt = 0
        for node in self:
            if node.item == value:
                cnt += 1
        return cnt
    def extend(self, other):
        for node in other:
            if isinstance(node, ListNode):
                self.append( ListNode(node.item))
            else:
                self.append( ListNode(node))
    def copy(self):
        newSll = self.__class__()
        for node in self:
            newSll.append( ListNode(node.item))
        return newSll
    def equalLast(self, node):
        return node == self.tail
    def reverse(self):
        for i in range( self.numItems // 2 ):
            f = self.at(i)[1]
            t = self.at(-1-i)[1]
            f.item, t.item = t.item, f.item
    def sort(self):
        lst = [ node.item for node in self ]
        self.clear()
        lst.sort()
        self.extend(lst)
    def __iter__(self):
        return CircularIterator(self)
    def __getitem__(self, i):
        if isinstance(i, slice):
            start, stop, step = i.indices(self.numItems)
            return self.__class__([ self.at(index)[1] for index in range(start, stop, step) ] )
        return self.at(i)[1]
    
class DoublyLinkedList:
    def __init__(self, iterable = []):
        self.tail = None
        self.numItems = 0
        self.extend(iterable)
    def __str__(self):
        return f"{self.__class__.__name__}[{self.numItems}, t{self.tail} :" + '->'.join([ f"{node.item}" for node in self ]) + "]"
    def _fix_pos(self, pos : int):
        if pos < 0:
            pos += self.numItems
            if pos < 0:
                pos = 0
        elif pos >= self.numItems:
            pos = self.numItems
        return pos
    def push_back(self, val):
        if self.tail is None:
            newNode = ListNode(val) # it returns a self referencing node
        else:
            newNode = ListNode(val, self.tail.next, self.tail)
            newNode.next.prev = newNode
            newNode.prev.next = newNode
        self.tail = newNode
        self.numItems += 1
    def push_front(self, val):
        if self.tail is None:
            return self.push_back(val)
        newNode = ListNode(val, self.tail.next, self.tail)
        self.tail.next = newNode
        newNode.next.prev = newNode
        self.numItems += 1
    def at(self, pos: int):
        pos = self._fix_pos(pos)
        if pos == self.numItems:
            return None
        if pos == 0:
            return self.tail.next
        if pos == self.numItems -1:
            return self.tail
        current = self.tail.next
        for _ in range(pos):
            current = current.next
        return current              
    def __insert(self, pos: int, newNode: ListNode):
        if newNode is None:
            return
        current = self.at(pos)
        if current == None: 
            self.push_back(newNode.item)
            return
        newNode.prev = current.prev
        newNode.prev.next = newNode
        current.prev = newNode
        newNode.next = current
        self.numItems += 1
    def insert(self, pos: int, value):
        self.__insert( pos, ListNode(value) )
    def append(self, val):
        self.push_back(val)
    def find(self, value):
        for node in self:
            if node.item == value:
                return node
        return None
    def pop(self, pos: int = -1):
        if self.tail is None:
            return None
        current = self.at(pos)
        if current is None:
            return None
        current.prev.next = current.next
        current.next.prev = current.prev
        if current == self.tail:
            self.tail = None if current == current.prev else current.prev
        self.numItems -= 1
        return current.item
    def pop_back(self):
        if self.tail is None:
            return None
        self.tail.prev.next = self.tail.next
        self.tail.next.prev = self.tail.prev
        item = self.tail.item
        if self.tail.prev == self.tail:
            self.tail = None 
        else:
            self.tail = self.tail.prev
        self.numItems -= 1
        return item
    def pop_front(self):
        if self.tail is None:
            return None
        head = self.tail.next
        self.tail.next = head.next
        head.next.prev = self.tail
        item = head.item
        if head == self.tail:
            self.tail = None
        self.numItems -= 1
        return item
    def remove(self, value):
        current = self.find(value)
        if current == None:
            return
        current.prev.next = current.next
        current.next.prev = current.prev
        if current == self.tail:
            self.tail = current.prev
        self.numItems -= 1
    def index(self, value):
        pos = 0
        for node in self:
            if node.item == value:
                return pos
            pos += 1
        return None
    def isEmpty(self) -> bool:
        return self.numItems == 0
    def size(self) -> int:
        return self.numItems
    def clear(self):
        while self.isEmpty() == False:
            self.pop()
    def count(self, value) -> int:
        cnt = 0
        for node in self:
            if node.item == value:
                cnt += 1
        return cnt
    def extend(self, other):
        for node in other:
            if isinstance(node, ListNode):
                self.append( node.item )
            else:
                self.append(node)
    def copy(self):
        return self[:]
    def reverse(self):
        if self.tail is None:
            return
        left = self.tail.next
        right = self.tail
        while left != right:
            left.item, right.item = right.item, left.item
            if left.next == right or right.prev == left:
                break
            left = left.next
            right = right.prev
    def sort(self):
        lst = [ node.item for node in self ]
        self.clear()
        lst.sort()
        self.extend(lst)
    def equalLast(self, node):
        return node == self.tail
    def __iter__(self):
        return CircularIterator(self)
    def __getitem__(self, i):
        if isinstance(i, slice):
            start, stop, step = i.indices(self.numItems)
            return self.__class__([ self.at(index) for index in range(start, stop, step) ] )
        return self.at(i)
    
class Iterator:
    def __init__(self, iterable):
        self.list = iterable
        self.it = iterable.at(0)[1]
    def __next__(self):
        if self.it is None:
            raise StopIteration
        node = self.it
        self.it = self.it.next
        return node

class CircularIterator(Iterator):
    def __init__(self, iterable):
        self.list = iterable
        if isinstance(iterable, SinglyLinkedList):
            self.it = iterable.at(0)[1]
        elif isinstance(iterable, DoublyLinkedList):
            self.it = iterable.at(0)
        else:
            self.it = iterable[0]
    def __next__(self):
        if self.it is None:
            raise StopIteration        
        node = self.it
        self.it = None if self.list.equalLast(node) else self.it.next
        return node

if __name__ == '__main__':

    sll = SinglyLinkedListDummy(['a', 'b', 'c'])
    print('sll with dummy (head version)', sll)
    for node in sll:
        print('iteration', node)

    sll = SinglyLinkedList(['a', 'b', 'c'])
    print('sll with no dummy (tail version)', sll)
    for node in sll:
        print('iteration', node)

    ll = DoublyLinkedList(['k', 'l','m'])
    print('dll with no dummy (tail version)', ll)
    for node in ll:
        print('iteration', node)
    
    ll.push_back('a')
    print('push back a', ll)
    ll.push_front('b')
    print('push front b', ll)
    ll.insert(-1, 'c')
    print('adding c at the end', ll)
    ll.append('d')
    print('append d', ll)
    ll.push_front('e')
    print('push_front e', ll)
    ll.push_back('e')
    print('push_back e', ll)
    ll.pop_back()
    print('pop back', ll)
    ll.pop_front()
    print('pop front', ll)


    print('count of b', ll.count('b'))
    print('index of e', ll.index('e'))
    print('index of a', ll.index('a'))
    print('index of k', ll.index('k'))

    ll2 = ll.copy()
    print('copy ll to sll2', ll, ll2)
    ll.extend(ll2)
    print('extend ll by adding sll2', ll, ll2)
    ll.clear()
    print('clearing ll', ll, ll2)
    ll2.reverse()
    print('reverse ll2', ll2)
    ll2.sort()
    print('sorting ll2', ll2)

    node = ll2.find('a')
    print('finding a in ll2', node)
