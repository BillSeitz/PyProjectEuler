"""
Solve GHQC Xmas-2015 puzzle http://gizmodo.com/can-you-solve-the-uk-intelligence-agencys-christmas-puz-1747265899
By BillSeitz 

sizes = {row_num:(len1, len2...)}
starts = {row_num: (start1, start2...)}

Remember to always use 0 as first index!
"""

grid_size = 25 # 0...24
grid_max = grid_size - 1
sizes = {}
sizes[1] = (7,3,1,1,7)

def show_row(size_list, starts_list):
	"""
	output row as series of characters
	"""
	#out = '0' * grid_size
	out = ''
	c = 0
	for i in range(0, len(size_list)):
		if starts_list[i] > c: # next start is after current row
			out = out + ('0' * (starts_list[i] - c))
			out = out + ('1' * size_list[i])
			c = starts_list[i] + size_list[i]
		if c < 25:
			out = out + ('0' * (25 - c))
	print out		

def leftest(size_list):
	"""
	Return "solution" (list of starts) for a row that puts each run as far left as possible
	"""
	starts_list = []
	c = 0
	for run in size_list:
		starts_list.append(c)
		c = c + run + 1
	print starts_list
	return starts_list

def next(starts_list):
	"""
	Return "next solution" list of starts after current solution
	Do this recursively:
	* start at right-most run
	* if rest of runs are jammed as far right as possible against it..
	 * then bump them back to far-left and move right-most 1 more to the right
	* else:
	 * do next(all but rightmost)
	"""
	
	
if __name__ == '__main__':
	print show_row(sizes[1], leftest(sizes[1]))


	