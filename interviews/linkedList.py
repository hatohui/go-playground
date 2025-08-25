from typing import List

class Node:
  def __init__(self, value: int, next: "Node" = None):
      self.value = value
      self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def get(self, index: int) -> int:
      if not self._isValidIndex(index): return -1
      return self._getNode(index).value

    def insertHead(self, val: int) -> None:
      new_node = Node(val)
      
      if (self.head is None):
        self.head = new_node
        self.tail = self.head
      else:
        new_node.next = self.head
        self.head = new_node

      self.length += 1

    def insertTail(self, val: int) -> None:   
      new_node = Node(val)
         
      if (self.head is None):
        self.head = new_node
        self.tail = self.head
      else:
        self.tail.next = new_node
        self.tail = self.tail.next
      
      self.length += 1

    def remove(self, index: int) -> bool:
      if not self._isValidIndex(index): return False
      
      if (index == 0):
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
        self.length -= 1
        return True
        
      prev = self._getNode(index - 1)   
      current = prev.next
      
      if (current.next == None): 
        self.tail = prev
        self.tail.next = None
      else: 
        prev.next = current.next
          
      self.length -= 1
      return True

    def getValues(self) -> List[int]:
      values = []
      c = self.head

      while c is not None:      
        values.append(c.value)
        c = c.next
      
      return values  
      
    def _isValidIndex(self, index) -> bool:
      return 0 <= index < self.length
    
    def _getNode(self, index) -> Node:
      if not self._isValidIndex(index): return None
      else:
        node = self.head
        for _ in range(index):
          node = node.next
        return node