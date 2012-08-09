#!/usr/bin/python

class Node(object):
  def __init__(self, elem):
    self.data = elem
    self.next = self.prev = None

class LinkedList(object):
  def __init__(self, *args):
    self.head = self.tail = None
    for elem in args:
      self.enqueue(elem)

  def __len__(self):
    if not self.head:
      return 0
    count = 1
    counter = self.head
    while(counter.next):
      counter = counter.next
      count += 1
    return count

  def enqueue(self, elem):
    node = Node(elem)
    if not self.head:
      self.head = self.tail = node
      return
    node.prev = self.tail
    self.tail.next = node
    self.tail = node

  def dequeue(self):
    if not self.head:
      print self.head
      return
    ret_elem = self.head.data
    if not self.head.next:
      self.head = self.tail = None
    self.head = self.head.next
    self.head.prev = None
    print ret_elem

  def show(self):
    if not self.head:
      print 'Empty linked list'
      return
    counter = self.head
    print counter.data
    while(counter.next):
      counter = counter.next
      print counter.data

  def get(self, index):
    if not self.head:
      print 'Empty linked list'
      return
    elif index >= len(self):
      print 'Index out of range'
      return
    count = 0
    counter = self.head
    while(count < index):
      counter = counter.next
      count += 1
    print counter.data

  def remove(self, index):
    if not self.head:
      print 'Empty linked list'
      return
    ret_elem = None
    count = 0
    counter = self.head
    while(counter.next):
      if(count == index):
        ret_elem = counter.data
        counter.prev.next = counter.next
        counter.next.prev = counter.prev
        break
      counter = counter.next
      count += 1
    print ret_elem

