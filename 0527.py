#-*- coding: utf-8 -*-

#define class
class dic:
	def __init__(self, ini, sort):
		self.ini  = ini
		self.sort = sort

# input the dic
f = open('/usr/share/dict/words','r')
strList = f.readlines()
classList = []

# sort the words in dic
for line in strList:	
  	a = (line.lower()).replace('\n','') # transform into lowerdcase letters and delete '\n'
  	a = ''.join(sorted(list(a)))        # split the word and sort it, and join again
  	classList.append(dic(line,a))       # make list of class

# sort the list ordered by self.sort
import operator
classList.sort( key = operator.attrgetter('sort'))

# close file
f.close()

# input letters
print 'please input a string of 16 letters'
x = raw_input()

# judge whether or not is it correct number of letters
if (len(x) != 16):
	print 'this data is not correct'
else:
	x = x.lower()  # transform into lowercase letters
	print 'searching ...'

ans = ''     # initialize ans
x_init = x   # use as a contant string 

for c in classList:
	for i in range(len(c.sort)):

		# if letter is in x, delete the letter once (in order to manage double or triple letter)
		if x.find(c.sort[i]) != -1:   
			x = x.replace(c.sort[i],'',1)

			# if not break until the last letter and longer than previous ans, then update ans 
			if i == len(c.sort) - 1:
				if len(c.sort) > len(ans):
					ans = c.ini

		# if can not find the letter, break
		else:
			x = x_init     # initialize x again
			break

print 'the answer is %s' % ans, 

