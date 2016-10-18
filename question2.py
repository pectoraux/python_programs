'''
	Efficiency:  
    ----------------------------------------------
   	is_palindromic() runs in O(n)

    So question2() runs in O(n) 

'''
def is_palindromic(b):
	'''
		Input: a certain string b
		Output : True if b is a pallindrome, False otherwise
		Procedure: First checks for extreme cases
				   Then checks if the extreme letters match
				   If not, returns False else strips them away
				   and restart all over again using recurrence
	'''
	if b == '' or len(b) == 1:	
		return True
	elif b[0] != b[-1]:	
		return False
	else:
		return is_palindromic(b[1:-1])	

def question2(a):
	'''
		Input: a certain string a
		Output: the longest palindromic substring of a
		Procedure: First checks if a is itself a pallindrome
				   If it is a gets printed out, if not
				   Strips away its last letters and starts all over again
	'''
	if is_palindromic(a):
	   print a
	else:
	   question2(a[1:-1])	

def run():
	# Test 1 					 # Should return 'ada'
	question2('ada')              
	# Test 2                     # Should return ' '
	question2(' ')
	# Test 3 				     # Should return ''
	question2('')				 
	# Test 4
	question2('wgeeksskeegt')    # Should return 'geeksskeeg'


if __name__ == '__main__':
 	run() 