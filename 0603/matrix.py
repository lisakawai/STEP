import numpy, time

# Open txt file
f = open('plot.txt', 'w') 

for n in xrange(100):

	a = numpy.zeros((n, n)) # Matrix A
	b = numpy.zeros((n, n)) # Matrix B
	c = numpy.zeros((n, n)) # Matrix C

	# Initialize the matrices to some values.
	for i in xrange(n):
	    for j in xrange(n):
	        a[i, j] = i * n + j
	        b[i, j] = j * n + i
	        c[i, j] = 0

	begin = time.time()

	for i in xrange(n):
		for j in xrange(n):
			for k in xrange(n):
				c[i, j] += a[i, k] * b[k, j]

	end = time.time()
	
	# Write time to txt file
	f.write('{} {}\n'.format(n, (end - begin)))

f.close()