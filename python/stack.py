#!/usr/bin/python

from linked_list import LinkedList, Node

class Stack(object):
  def __init__(self, *args):
    self.tail = None
    for elem in args:
      self.push(elem)

  def push(self, elem):
    node = Node(elem)
    if not self.tail:
      self.tail = node
    self.tail.next = node
    node.prev = self.tail
    self.tail = node

  def pop(self):
    if not self.tail:
      print 'Stack is empty'
      return
    ret_elem = self.tail.data
    self.tail = self.tail.prev
    self.tail.next = None
    print ret_elem

