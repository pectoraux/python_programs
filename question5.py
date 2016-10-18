'''
    Efficiency:  
    ----------------------------------------------
    member function get_length() of class Linked_List runs in O(1)
    member function get_at_position() of class Linked_List runs in O(n)
    make_ll() runs in O(n)

    So question5() runs in O(n) 
'''

class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None
	def __str__(self):
		return str(self.data)	

class Linked_List(object):
	"""
		Linked list class with necessary functions
		for the problem implemented: a printer for debugging
		a .get_at_position() method to get an element at a position
		a .get_length() method to get the element that is m position 
		away faster by doing: ll.get_at_position(ll.get_length - m)
		and a .append() method to populate the linked list
	"""
	def __init__(self, head=None):
		self.head = head
		if head:
			self.length = 1
		else:
			self.length = 0

	def printer(self):
		current = self.head
		while current:
			print current
			current = current.next
		    
			
	def get_length(self):
		return self.length

	def get_at_position(self, position):
		counter = 1
		current = self.head
		if position < 0 :
			return None
		while current and counter <= position:
			if counter == position:
				return current
			current = current.next
			counter += 1
  		return None
  	
  	def append(self, new_element):
  		current = self.head	
  		if self.head:
  			while current.next:
  				current = current.next
  			current.next = new_element
  		else:
  			self.head = new_element	
  		self.length += 1		

def question5(ll, m):
	""" Takes in a linked list and a position m 
		Returns the element that is m element from the end
	"""
	ll_len = ll.get_length()
	return ll.get_at_position(ll_len-m) 

def make_ll(arr):
	"""Takes in an array and turns it into a linked list
		Useful for testing purposes
	"""
	my_ll = Linked_List()
	for i in range(len(arr)):
		my_ll.append(Node(arr[i]))
	#my_ll.printer()	  # prints the final linked list; useful for debugging
  	return my_ll
  		
def run():
	# Test 1
	print question5(make_ll(['elephant', 'shoes', 'basket']), 0) # Should return basket
	# Test 2
	print question5(make_ll(range(10)), 4)  # Should return 5
	# Test 3
	print question5(make_ll([None, 'forward', '', '-', 'right']), 1) # Should return -					

		
if __name__ == '__main__':
 	run() 