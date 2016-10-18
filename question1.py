'''
	Efficiency:  
    ----------------------------------------------
   	contained_in() runs in O(n)

    So question2() runs in O(n) 

'''

def contained_in(t, s):
	'''
	Inputs: t, s
	Function: Checks if an anagram of t is contained in s
	Procedure: makes a list containing indices in s of each letter in t
			   -1 is put inside the list in place of letters of t not present in s
			   finds the max and min of that list and checks if the
			   indices are exactly one point away from one another
	Efficiency: By computing the max and min, sorting of the list is avoided
				making the algorithm faster
				We also avoid having to find all anagrams of t by using this formula		   
	'''

	contains = []
	value = 0
	for i in range(len(t)):
			cur_elem = t[i]
			if cur_elem in s:
				value = s.index(cur_elem)
			else:
				value = -1	
			if value not in contains:			# Correction: Added removal of duplicates
				contains.append(value)	
	return ( max(contains) - min(contains) + 1 == len(contains) and
		     max(contains) != -1 ) 
				
		
			  

def question1(s, t):
	'''
	Inputs: t, s
	Function: Prints True if s contains an Anagram of t
			  False otherwise
	'''
	if t == '':
		print True
		return 
	elif s == '':
		print False
		return 	
	elif contained_in(t, s):
		print 'True'
		return
	else: 
		print 'False'					

def run():
	# Test 1
	question1("udacity", "yt")  # Should print True
	# Test 2
	question1('', 's')			# Should print False
	# Test 3
	question1('s', '')			# Should print True
	# Test 4
	question1('s', ' ')			# Should print False
	# Test 5
	question1('udacity', 'uaaai')			# Should print False

if __name__ == '__main__':
    run()