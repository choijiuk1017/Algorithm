class ListNode:
    def __init__(self, item, next : 'ListNode' = None, prev: 'ListNode' = None, selfContained = True):
        self.item = item
        self.next = next
        self.prev = prev
        if selfContained and next is None and prev is None:
            self.next = self
            self.prev = self
    def __str__(self, short = False):
        if short is True:
            return f'{self.item}'
        return f'({self.prev if self.prev is None else self.prev.item}< :{self.item}: >{self.next if self.next is None else self.next.item})'



