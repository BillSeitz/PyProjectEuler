"""
Solve GHQC Xmas-2015 puzzle http://gizmodo.com/can-you-solve-the-uk-intelligence-agencys-christmas-puz-1747265899
By BillSeitz 

sizes = {row_num:(len1, len2...)}
starts = {row_num: (start1, start2...)}

Remember to always use 0 as first index!

Definitions:
* row is a list of start-positions (starts_list) (combined with sizes_list)
* row_bits is a rendered string of 0/1 chars for a row
* solution is hash of rows where each row has 2 items: a starts_list list and a row_bits string
 * each of those is keyed hash
 * solution{'1':{'starts_list':[0,4,7], 'row_bits':'1100011'}}
 * whenever change starts_list, change row_bits at same time
* col_bits is 1 column cutting down a grid
 * when changing 1 row you have to change All col_bits

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

def show_header(): # bah just fixed for 25 right now
    print '0123456789012345678901234'
    
def row_bits(sizes_list, starts_list):
    """
    returns row_bits series of characters for given row
    """
    #out = '0' * grid_size
    out = ''
    c = 0
    #print 'sizes, starts:', sizes_list, starts_list
    for i in range(0, len(sizes_list)):
        #print 'c, i, starts[i]:', c, i, starts_list
        if starts_list[i] > c: # next start is after current row
            out = out + ('0' * (starts_list[i] - c))
        out = out + ('1' * sizes_list[i])
        c = starts_list[i] + sizes_list[i]
    if c < 25:
        out = out + ('0' * (25 - c))
    return out      

def leftest(sizes_list):
    """
    Return starts_list "row-solution" for a row that puts each run as far left as possible
    """
    starts_list = []
    c = 0
    for run in sizes_list:
        starts_list.append(c)
        c = c + run + 1
    #print 'starts:', starts_list
    return starts_list
    
def is_all_rightest(sizes_list, starts_list, total_len):
    """
    Returns True if All runs are jammed as far right as possible.
    """
    #print 'is_all_rightest lists:', sizes_list, starts_list
    num_runs = len(sizes_list)
    leftest_start = starts_list[0]
    min_tot_lengths = sum(sizes_list) + num_runs - 1 # sum of lengths plus spaces
    #print 'is_all_rightest lists, tot-leftest, min_tot:', sizes_list, starts_list, total_len - leftest_start, min_tot_lengths
    if total_len - leftest_start > min_tot_lengths:
        return False
    else:
        return True

def is_sub_rightest(sizes_list, starts_list):
    """
    Returns True if all the non-rightest runs are jammed as far right against the right-most as possible.
    """
    #print 'is_sub_rightest lists:', sizes_list, starts_list
    num_runs = len(sizes_list) - 1
    leftest_start = starts_list[0]
    rightest_start = starts_list[-1]
    min_tot_lengths = sum(sizes_list[0:-1]) + num_runs # sum of lengths plus spaces
    #print 'is_sub_rightest lists, tot-leftest, min_tot:', sizes_list, starts_list, rightest_start - leftest_start, min_tot_lengths
    if rightest_start - leftest_start > min_tot_lengths:
        return False
    else:
        return True

def next_row(sizes_list, starts_list):
    """
    Return starts_list of "next row-solution" after current solution.
    We know that we don't have all the runs right-jammed because that was tested in shift()
    Do this recursively (this is different from the shift() recursion):
    * start at right-most run
    * if rest of runs are jammed as far right as possible against it..
     * then bump them back to far-left and move right-most 1 more to the right (unless it's already as far right as possible)
    * else:
     * do next_row(all but rightmost) (ooh recursive!)
    """
    if is_sub_rightest(sizes_list, starts_list):
    	#print 'in next_row is_rightest so...'
        if starts_list[-1] + sizes_list[-1] == grid_size:
            return False
        new_starts_list = leftest(sizes_list[0:-1])
        new_starts_list.append(starts_list[-1] + 1)
    else:
        new_starts_list = next_row(sizes_list[0:-1], starts_list[0:-1]) #recursive bit
        new_starts_list.append(starts_list[-1])
    #print 'next_row: new_starts_list:', new_starts_list
    return new_starts_list

def shift(solution, row_to_shift):
	print 'shifting at row', row_to_shift
	if is_all_rightest(sizes[row_to_shift], solution[row_to_shift]['starts_list'], grid_size):
		starts_list = leftest(sizes[row_to_shift])
		solution[row_to_shift]['starts_list'] = starts_list
		solution[row_to_shift]['row_bits'] = row_bits(sizes[row_to_shift], starts_list)
		row_to_shift = row_to_shift + 1
		solution, row_to_shift = shift(solution, row_to_shift) # recursive bit
	else:
		starts_list = next_row(sizes[row_to_shift], solution[row_to_shift]['starts_list'])
		solution[row_to_shift]['starts_list'] = starts_list
		solution[row_to_shift]['row_bits'] = row_bits(sizes[row_to_shift], starts_list)
	return (solution, row_to_shift)
		
	    
def first_solution():
    """
    Make the first grid-solution of using leftest() for every row
    """
    solution = {}
    for i in range(0, grid_size):
    	#print 'i:', i
    	starts = leftest(sizes[i])
        bits = row_bits(sizes[i], starts) # do at same time to keep in synch
        solution[i] = {'starts_list':starts, 'row_bits': bits}
    #print 'solution', solution
    return (solution) 
    
def display(solution): # output a solution grid
    show_header()
    for row in solution.keys():
        print solution[row]['row_bits']
    
def col_bits(i, solution):
    """
    Return column i from solution grid (looks like rows_bits[i])
    """
    col_bits = ""
    print 'solution type, len', type(solution), len(solution)
    for row in solution.keys():
        col_bits = col_bits + solution[row]['row_bits'][i]
    	#print 'i, row, row_bits, col_bits', i, row, solution[row]['row_bits'], col_bits
    #print 'col_bits final:', col_bits
    return col_bits
    
def test_col(i, solution):
    """
    Return whether a column from a solution grid matches the spec cols
    """
    col_bits_i = col_bits(i, solution)
    col_runs = []
    state = 'out'
    l = 0
    for j in col_bits_i:
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
    print 'col_runs, cols[i]:', col_runs, cols[i]
    if col_runs == cols[i]:
        return True
    else:
        return False

def test_solution(solution):
    """
    Test all columns of solution_grid against the spec cols until first Fail
    """
    for i in range(0, grid_max):
        print 'testing col:', i
        if not test_col(i, solution):
            return False
    return True
    
def run_solutions():
    i = 0 # solution counter
    print 'starting solution num', i
    row_to_shift = 0
    output_freq = 10
    solution = first_solution()
    while not test_solution(solution) and (i<999999):
        print 'test num', i, 'fails'
        i = i+1
        (solution, row_to_shift) = shift(solution, row_to_shift)
        print 'starting solution num at row', i, row_to_shift
        if i * 1.0 / output_freq == int(i * 1.0 / output_freq):
	        display(solution)
    print i, '------------- Success ------------'
    display(solution)
        

if __name__ == '__main__':
    show_header()
    print row_bits(sizes[0], leftest(sizes[0]))
    #print row_bits(sizes[1], leftest(sizes[1]))
    #display(first_solution())
    #print 'col_bits[1]:', col_bits(1, first_solution())
    #print test_col(1, first_solution())
    #print test_solution(first_solution())
    #print row_bits(sizes[0], next_row(sizes[0], leftest(sizes[0])))
    run_solutions()


    