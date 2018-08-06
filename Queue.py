# Queue implementation in Python
from LinkedList import LinkedList

class Queue(object):
	
	def __init__(self, head=None):
		self.ll = LinkedList(head)
		
	def enqueue(self, new_element):
		self.ll.push_back(new_element)
		
	def dequeue(self):
		return self.ll.pop_front()
		
	def peek(self):
		return self.ll.get_position(1)