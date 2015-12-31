# counting.py by BillSeitz Dec'2015 to practice recursive shifting for GHCQ test

def shift(vals, dig):
	if vals[dig] == '9':
		vals[dig] = '0'
		dig = dig - 1
		shift(vals, dig)
	else:
		vals[dig] = str(int(vals[dig]) + 1)
	return vals

def run():
	val = '000'
	lenval = len(val)
	counter = 0
	while val < '999':
		vals = list(val)
		dig = lenval - 1
		vals = shift(vals, dig)
		#print vals
		val = ''.join(vals)
		print vals
	print 'done'

if __name__ == '__main__':
	run()