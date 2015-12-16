"""
Solve GHQC Xmas-2015 puzzle http://gizmodo.com/can-you-solve-the-uk-intelligence-agencys-christmas-puz-1747265899
By BillSeitz 

sizes = {row_num:(len1, len2...)}
starts = {row_num: (start1, start2...)}

Remember to always use 0 as first index!

Basic process:
* start with every row having its runs pushed to the far left
* treat top row like ones-digit, 2nd row like tens-digit, etc.
* so start by testing all the row_next variations of the first row, then
 * bump the 2nd row row_next once and push the 1st row back to leftest, testing all the first-row variations, then
 * rest of 2nd/1st row variations combos, then
 * bump the 3rd row row_next once, etc.
"""

grid_size = 25 # 0...24
grid_max = grid_size - 1
sizes = {}
sizes[0] = (7,3,1,1,7)
sizes[1] = (1,1,2,2,1,1)
sizes[2] = (1,3,1,3,1,1,3,1)
sizes[3] = (1,3,1,1,6,1,3,1)
sizes[4] = (1,3,1,5,2,1,3,1)
sizes[5] = (1,1,2,1,1)
sizes[6] = (7,1,1,1,1,1,7)
sizes[7] = (3,3)
sizes[8] = (2,3,1,1,3,1,1,2)
sizes[9] = (1,1,3,2,1,1)
sizes[10] = (4,1,4,2,1,2)
sizes[11] = (1,1,1,1,1,4,1,3)
sizes[12] = (2,1,1,1,2,5)
sizes[13] = (3,2,2,6,3,1)
sizes[14] = (1,9,1,1,2,1)
sizes[15] = (2,1,2,2,3,1)
sizes[16] = (3,1,1,1,1,5,1)
sizes[17] = (1,2,2,5)
sizes[18] = (7,1,2,1,1,3)
sizes[19] = (1,1,2,1,2,2,1)
sizes[20] = (1,3,1,4,5,1)
sizes[21] = (1,3,1,3,10,2)
sizes[22] = (1,3,1,1,6,6)
sizes[23] = (1,1,2,1,1,2)
sizes[24] = (7,2,1,2,5)
cols = {}
cols[0] = (7,2,1,1,7)
cols[1] = (1,1,2,2,1,1)
cols[2] = (1,3,1,3,1,3,1,3,1)
cols[3] = (1,3,1,1,5,1,3,1)
cols[4] = (1,3,1,1,4,1,3,1)
cols[5] = (1,1,1,2,1,1,)
cols[6] = (7,1,1,1,1,1,7)
cols[7] = (1,1,3)
cols[8] = (2,1,2,1,8,2,1)
cols[9] = (2,2,1,2,1,1,1,2)
cols[10] = (1,7,3,2,1)
cols[11] = (1,2,3,1,1,1,1,1)
cols[12] = (4,1,1,2,6)
cols[13] = (3,3,1,1,1,3,1)
cols[14] = (1,2,5,2,1)
cols[15] = (2,2,1,1,1,1,1,2,1)
cols[16] = (1,3,3,2,1,8,1)
cols[17] = (6,2,1)
cols[18] = (7,1,4,1,1,3)
cols[19] = (1,1,1,1,4)
cols[20] = (1,3,1,3,7,1)
cols[21] = (1,3,1,1,1,2,1,1,4)
cols[22] = (1,3,1,4,3,3)
cols[23] = (1,1,2,2,2,6,1)
cols[24] = (7,1,3,2,1,1)

def show_header(): #bah just fixed for 25 right now
    print '0123456789012345678901234'
    
def row(size_list, starts_list):
    """
    return row as series of characters
    """
    #out = '0' * grid_size
    out = ''
    c = 0
    #print 'sizes, starts:', size_list, starts_list
    for i in range(0, len(size_list)):
    	#print 'c, i, starts[i]:', c, i, starts_list
        if starts_list[i] > c: # next start is after current row
            out = out + ('0' * (starts_list[i] - c))
        out = out + ('1' * size_list[i])
        c = starts_list[i] + size_list[i]
    if c < 25:
        out = out + ('0' * (25 - c))
    return out      

def leftest(size_list):
    """
    Return "row-solution" (list of starts) for a row that puts each run as far left as possible
    """
    starts_list = []
    c = 0
    for run in size_list:
        starts_list.append(c)
        c = c + run + 1
    #print starts_list
    return starts_list
    
def is_rightest(size_list, starts_list):
	"""
	Returns True if all the non-rightest runs are jammed as far right against the rightest one as possible.
	"""
	l = len(size_list)
	rightest_start = starts_list[-1]
	leftest_start = starts_list[0]
	sum_left_lengths = sum(size_list[0:-1]) + (l-1) # sum of lengths (excl rightest) plus spaces
	if rightest_start - leftest_start > sum_left_lengths:
		return False
	else:
		return True

def next_row(size_list, starts_list):
    """
    Return "next row-solution" list of starts after current solution
    Do this recursively:
    * start at right-most run
    * if rest of runs are jammed as far right as possible against it..
     * then bump them back to far-left and move right-most 1 more to the right (unless it's already as far right as possible)
    * else:
     * do next_row(all but rightmost) (ooh recursive!)
    """
    if is_rightest(size_list, starts_list):
    	if start_list[-1] + size_list[-1] == grid_size:
    		return False
    	new_starts_list = leftest(size_list[0:-1])
    	new_starts_list.append(starts_list[-1] + 1)
    else:
    	new_starts_list = next_row(size_list[0:-1], starts_list[0:-1])
    	new_starts_list.append(starts_list[-1])
    return new_starts_list
    
def first_solution():
    """
    Make the first grid-solution of using leftest() for every row
    """
    rows = {}
    for i in range(0, grid_max):
        rows[i] = row(sizes[i], leftest(sizes[i]))
    return rows 
    
def display(rows): # output a solution grid
    show_header()
    #print rows
    for row in rows:
        print rows[row]
    
def col(i, solution):
    """
    Return column i from solution grid (looks like rows[i])
    """
    col = ""
    for row in solution:
        col = col + solution[row][i]
    return col
    
def test_col(i, col):
    """
    Return whether a column from a solution grid matches the spec cols
    """
    col_runs = []
    state = 'out'
    l = 0
    for j in col:
        #print 'j, state, l, col: ', j, state, l, col
        if (state == 'out') and (j == '0'):
            continue
        elif (state == 'in') and (j == '1'):
            l = l + 1
            continue
        elif (state == 'out') and (j == '1'):
            l = 1
            state = 'in'
            continue
        else: # (state == 'in') and (j == '0'):
            col_runs.append(l)
            state = 'out'
            l = 0
            continue
    if (state == 'in') and (l > 0):
        col_runs.append(l)
    print 'col_runs:', col_runs
    if col_runs == cols[i]:
    	return True
    else:
    	return False

def test_solution(solution):
	"""
	Test all columns of solution_grid against the spec cols
	"""
	for i in range(0, grid_max):
		print 'test col i:', i
		if not test_col(i, col(i, solution)):
			return False
	return True
    
def run_solutions():
	i = 0
	row_to_shift = 0
	solution = first_solution()
	while not test_solution(solution):
		print i, 'fail'
		i = i+1
		shifted_row = next_row(sizes[row_to_shift], solution[row_to_shift])
		if not shifted_row: # meaning returned False, so all-right, so on to next row
			rows[row_to_shift] = row(sizes[row_to_shift], leftest(sizes[row_to_shift]))
			row_to_shift = row_to_shift + 1
			shifted_row = next_row(sizes[row_to_shift], solution[row_to_shift])
	print i, '------------- Success ------------'
	display(solution)
		

if __name__ == '__main__':
    show_header()
    print row(sizes[0], leftest(sizes[0]))
    #print row(sizes[1], leftest(sizes[1]))
    #display(first_solution())
    #print col(1, first_solution())
    #print test_col(1, col(1, first_solution()))
    #print test_solution(first_solution())
    print row(sizes[0], next_row(sizes[0], leftest(sizes[0])))


    