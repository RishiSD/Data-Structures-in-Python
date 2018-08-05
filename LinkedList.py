# Linked List implementation in Python

class Node(object):

	def __init__(self, value):
		self.value = value
		self.next = None

class LinkedList(object):

	def __init__(self, head=None):
		self.head = head
		
	def append(self, node):
		current = self.head
		if current:
			while current.next:
				curren = curren.next
			current.next = node
		else:
			self.head = node
			
	def print_list(self):
		current = self.head
		while current:
			print(current.value, end=' -> ')
			current = current.next
		print('None')
	
	def insert(self, node, position=1):
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
		current = self.head
		counter = 1
		while current and position != counter:
			current = current.next
			counter += 1
		if counter ==  position:
			return current.value
		else:
			return None