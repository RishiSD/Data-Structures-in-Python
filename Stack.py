# Stack implementation in Python
from LinkedList import LinkedList

class Stack(object):
	def __init__(self, top=None):
		self.ll = LinkedList(top)
	
	def push(self, new_element):
		self.ll.push_front(new_element)
	
	def pop(self):
		popped_element = self.ll.pop_front()
		return popped_element.value if popped_element else None