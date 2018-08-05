# Linked List implementation in Python

class Node(object):
	"""
	This class represents a single Node in LinkedList.
	
	Attributes:
		value : Value associated to Node.
		next  : Object reference to the next Node in the LinkedList.
	"""
	def __init__(self, value):
		"""
		The constructor for class Node.
		
		Parameters:
			value : Value associated to Node.
			next  : Object reference to the next Nodi in the LinkedList.		
		"""
		self.value = value
		self.next = None

class LinkedList(object):
	"""
	This class represents a LinkedList.
	
	Attributes:
		head  : Object reference to the first Node in the LinkedList. 
	"""

	def __init__(self, head=None):
		"""
		The constructor for class LinkedList.
		
		Parameters:
			head  : Object reference to the first Node in the LinkedList.
		"""
		self.head = head
		
	def append(self, node):
		"""
		The funtion to append a node in the LinkedList.
		
		Parameters:
			node  : Node to append in the LinkedList.
		"""		
		current = self.head
		if current:
			while current.next:
				curren = curren.next
			current.next = node
		else:
			self.head = node
			
	def print_list(self):
		"""
		The funtion prints the Node values in the LinkedList.
		"""	
		current = self.head
		while current:
			print(current.value, end=' -> ')
			current = current.next
		print('None')
	
	def insert(self, node, position=1):
		"""
		The funtion inserts a node in the LinkedList at the given position.
		
		Parameters:
			node     : Node to insert in the LinkedList.
			position : Position where the node is to be appended in the LinkedList.
		"""	
		current =  self.head
		if position > 1:
			for i in range(position-2):
				current = current.next
			if current:	
				node.next = current.next
				current.next = node
		elif position == 1:
			node.next = self.head
			self.head = node
		else:
			raise IndexError
		
	def remove(self, value):
		"""
		The funtion remove all the elements with Node value provided in input from the LinkedList.
		
		Parameters:
			value : Value for which Nodes are to be removed from the LinkedList.
		"""	
		current = self.head
		previous = None
		while current:
			if current.value == value:
				if previous:
					previous.next = current.next
				else:
					self.head = current.next
			previous = current
			current = current.next
	
	def delete(self, position):
		"""
		The funtion deletes the Node at a particular position the LinkedList.
		
		Parameters:
			position : Position of the Node which is to be deleted.
		"""	
		current = self.head
		previous = None
		counter = 1
		while current and position != counter:
			previous = current
			current = current.next
			counter += 1
		if current:
			if previous:
				previous.next = current.next
			else:
				self.head = current.next
	
	def get_position(self, position):
		"""
		The funtion to get Node value for given position from the LinkedList.
		
		Parameters:
			position : Position of the Node for which value is to be retreived.
		
		Returns:
			value : Value for Node at the given position.	
		"""	
		current = self.head
		counter = 1
		if position < 1:
			raise IndexError
		while current and position != counter:
			current = current.next
			counter += 1
		if counter ==  position:
			return current.value
		else:
			return None