import math,string,itertools,fractions,heapq,collections,re,array,bisect,random

class BoxUnion:
    def area(self, rectangles):
    	for rectangle in rectangles:
        	matrix = []
        	max_right = max_top = 0
        	min_left = min_bottom = 20000
        	for rectangle in rectangles:
        		left, right, bottom, top = [int(x) for x in rectangle.split()]
        		if left < min_left:
        			min_left = left
        		if right > max_right:
        			max_right = right
        		if bottom < min_bottom:
        			min_bottom = bottom
        		if top > max_top:
        			max_top = top
        	print(min_left, max_right, min_bottom, max_top)
        		
        return 9

# BEGIN KAWIGIEDIT TESTING
# Generated by KawigiEdit-pf 2.3.0
import sys
import time
def KawigiEdit_RunTest(testNum, p0, hasAnswer, p1):
	sys.stdout.write(str("Test ") + str(testNum) + str(": [") + str("{"))
	for i in range(len(p0)):
		if (i > 0):
			sys.stdout.write(str(","))
		
		sys.stdout.write(str("\"") + str(p0[i]) + str("\""))
	
	sys.stdout.write(str("}"))
	print(str("]"))
	obj = BoxUnion()
	startTime = time.clock()
	answer = obj.area(p0)
	endTime = time.clock()
	res = True
	print(str("Time: ") + str((endTime - startTime)) + str(" seconds"))
	if (hasAnswer):
		print(str("Desired answer:"))
		print(str("\t") + str(p1))
	
	print(str("Your answer:"))
	print(str("\t") + str(answer))
	if (hasAnswer):
		res = answer == p1
	
	if (not res):
		print(str("DOESN'T MATCH!!!!"))
	elif ((endTime - startTime) >= 2):
		print(str("FAIL the timeout"))
		res = False
	elif (hasAnswer):
		print(str("Match :-)"))
	else:
		print(str("OK, but is it right?"))
	
	print(str(""))
	return res

all_right = True
tests_disabled = False


# ----- test 0 -----
disabled = False
p0 = ("200 300 203 304",)
p1 = 12
all_right = (disabled or KawigiEdit_RunTest(0, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 1 -----
disabled = False
p0 = ("0 0 10 10","20 20 30 30")
p1 = 200
all_right = (disabled or KawigiEdit_RunTest(1, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 2 -----
disabled = False
p0 = ("0 500 20000 501","500 0 501 20000")
p1 = 39999
all_right = (disabled or KawigiEdit_RunTest(2, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 3 -----
disabled = False
p0 = ("4 6 18 24","7 2 12 19","0 0 100 100")
p1 = 10000
all_right = (disabled or KawigiEdit_RunTest(3, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 4 -----
disabled = False
p0 = ("1 3 5 6","3 1 7 5","4 4 9 7")
p1 = 35
all_right = (disabled or KawigiEdit_RunTest(4, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 5 -----
disabled = False
p0 = ("0 0 20000 20000","0 0 20000 20000","0 0 20000 20000")
p1 = 400000000
all_right = (disabled or KawigiEdit_RunTest(5, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

if (all_right):
	if (tests_disabled):
		print(str("You're a stud (but some test cases were disabled)!"))
	else:
		print(str("You're a stud (at least on given cases)!"))
	
else:
	print(str("Some of the test cases had errors."))

# END KAWIGIEDIT TESTING
#Powered by KawigiEdit-pf 2.3.0!
