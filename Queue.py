# Queue implementation in Python
from LinkedList import LinkedList

class Queue(object):
	"""
	This class represents a Queue implementation with a LinkedList.
	
	Attributes:
		ll : LinkedList used for implementing the Queue.
	"""
	
	def __init__(self, head=None):
		"""
		The constructor for class Queue.
		
		Parameters:
			head : Represents the first element to enqueue.
		"""
		self.ll = LinkedList(head)
		
	def enqueue(self, new_element):
		"""
		The function to enqueue a new element.
		
		Parameters:
			new_element : New element to enqueue.
		"""
		self.ll.push_back(new_element)
		
	def dequeue(self):
		"""
		The function to dequeue a new element.
		
		Returns:
			element : Dequeued element from the head of the queue.
		"""
		return self.ll.pop_front()
		
	def peek(self):
		"""
		The function to get value of element at the beginning of the queue.
		
		Parameters:
			value : Value of element at the beginning of the queue.
		"""
		return self.ll.get_position(1)