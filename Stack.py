# Stack implementation in Python
from LinkedList import LinkedList

class Stack(object):
	"""
	This class represents a Stack implementation with a LinkedList.
	
	Attributes:
		ll : LinkedList used for implementing the Stack.
	"""
	
	def __init__(self, top=None):
		"""
		The constructor for class Stack.
		
		Parameters:
			top : represents the top of the stack.
		"""
		self.ll = LinkedList(top)
	
	def push(self, new_element):
		"""
		The function to push an element into the Stack.
		
		Parameters:
			new_element : element to be pushed to the top of Stack.
		"""
		self.ll.push_front(new_element)
	
	def pop(self):
		"""
		The function to pop an element from the top of the Stack.
		
		Returns:
			new_element : Popped element from the top of the Stack.
		"""	
		popped_element = self.ll.pop_front()
		return popped_element.value if popped_element else None
	
	def peek(self):
		"""
		This function returns the value of the element at the top of the Stack.
		
		Returns:
			value : Value of element at the top of the Stack.
		"""
		return self.ll.head.value if self.ll.head else None