import math,string,itertools,fractions,heapq,collections,re,array,bisect,random

class ReportAccess:
    def whoCanSee(self, username, allowed_data, report_data):
        allowed_users = []

        for user, access_level in zip(username, allowed_data):
            for allowed_access_level in report_data:
                if allowed_access_level not in access_level.split():
                    break
            else:
                allowed_users.append(user)
        return sorted(allowed_users)


# BEGIN KAWIGIEDIT TESTING
# Generated by KawigiEdit-pf 2.3.0
import sys
import time
def KawigiEdit_RunTest(testNum, p0, p1, p2, hasAnswer, p3):
	sys.stdout.write(str("Test ") + str(testNum) + str(": [") + str("{"))
	for i in range(len(p0)):
		if (i > 0):
			sys.stdout.write(str(","))
		
		sys.stdout.write(str("\"") + str(p0[i]) + str("\""))
	
	sys.stdout.write(str("}") + str(",") + str("{"))
	for i in range(len(p1)):
		if (i > 0):
			sys.stdout.write(str(","))
		
		sys.stdout.write(str("\"") + str(p1[i]) + str("\""))
	
	sys.stdout.write(str("}") + str(",") + str("{"))
	for i in range(len(p2)):
		if (i > 0):
			sys.stdout.write(str(","))
		
		sys.stdout.write(str("\"") + str(p2[i]) + str("\""))
	
	sys.stdout.write(str("}"))
	print(str("]"))
	obj = ReportAccess()
	startTime = time.clock()
	answer = obj.whoCanSee(p0, p1, p2)
	endTime = time.clock()
	res = True
	print(str("Time: ") + str((endTime - startTime)) + str(" seconds"))
	if (hasAnswer):
		print(str("Desired answer:"))
		sys.stdout.write(str("\t") + str("{"))
		for i in range(len(p3)):
			if (i > 0):
				sys.stdout.write(str(","))
			
			sys.stdout.write(str("\"") + str(p3[i]) + str("\""))
		
		print(str("}"))
	
	print(str("Your answer:"))
	sys.stdout.write(str("\t") + str("{"))
	for i in range(len(answer)):
		if (i > 0):
			sys.stdout.write(str(","))
		
		sys.stdout.write(str("\"") + str(answer[i]) + str("\""))
	
	print(str("}"))
	if (hasAnswer):
		if (len(answer) != len(p3)):
			res = False
		else:
			for i in range(len(answer)):
				if (answer[i] != p3[i]):
					res = False
				
			
		
	
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
p0 = ("joe","nick","ted")
p1 = ("clients products","products orders","clients orders")
p2 = ("clients","products")
p3 = ("joe",)
all_right = (disabled or KawigiEdit_RunTest(0, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 1 -----
disabled = False
p0 = ("kathy","john","dan","steve","cheryl","tony")
p1 = ("users data","data orders","users permissions","system users controls","default","admin users")
p2 = ("users",)
p3 = ("dan","kathy","steve","tony")
all_right = (disabled or KawigiEdit_RunTest(1, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 2 -----
disabled = False
p0 = ("jim","scott","barbara")
p1 = ("users order products","products shipping","tracking products orders")
p2 = ("admin",)
p3 = ()
all_right = (disabled or KawigiEdit_RunTest(2, p0, p1, p2, True, p3) ) and all_right
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
