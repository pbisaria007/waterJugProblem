# Water jug problem - Shadab Khan. MIS : 111403071
# Uses concept of graph search. Each (x, y) = node on graph.

# Input
print("Enter capacity of jug 1:")
M = int(input())
print("Enter capacity of jug 2:")
N = int(input())
print("Enter final value needed in jug 1:")
finalVal = int(input())

# Apply a specific rule to any (x, y) value
def rule(n, x, y):
	#0 fill up jug 1
    if n == 0:
        x = M
    #1 fill up jug 2
    elif n == 1:
        y = N
    #2 empty jug 1
    elif n == 2:
        x = 0
    #3 empty jug 2
    elif n == 3:
        y = 0
    #4 pour jug 1 in jug 2
    elif n == 4:
        if x >= N - y:
            x, y = x - (N - y), N
        else:
            x, y = 0, y + x
    #5 pour jug 2 in jug 1
    elif n == 5:
        if y >= M - x:
            x, y = M, y - (M - x)
        else:
            x, y = x + y, 0
    #6 empty jug 1 in jug 2
    elif n == 6:
        x, y = 0, y + x
        if y > N:
            y = N
    #7 empty jug 2 in jug 1
    elif n == 7:
        x, y = x + y, 0
        if x > M:
            x = M
    return x, y
            
# check if the end condition is reached
def checkSol(x, y):
    if x == finalVal:
#        print("in checksol", x,y)
        return True
    else:
#        print("in cS, false", x, y)
        return False
        
visitedNodes = []
steps = []

def checkRule(r, x, y):
	x, y = rule(r, x, y)
	if (x, y) in visitedNodes:
		return False
	else:
		return True

def findSol(x, y):
#	print("start", x, y)
	if checkSol(x, y):
#		print ("out checksol",x, y)
		return True
	for i in range(0, 8):
		if checkRule(i, x, y):
			tx, ty = x, y
			x, y = rule(i, x, y)
			steps.append(i)
			visitedNodes.append((x, y))
#			print(i)
#			print(visitedNodes)
			if findSol(x, y):
				return True
			x, y = tx, ty
			steps.pop()
			visitedNodes.pop()
	return False

def ruleInWords(i):
	if i == 0:
		print("fill up jug 1");
	elif i == 1:
		print("fill up jug 2");
	elif i == 2:
		print("empty jug 1");
	elif i == 3:
		print("empty jug 2");
	elif i == 4:
		print("pour jug 1 in jug 2");
	elif i == 5:
		print("pour jug 2 in jug 1");
	elif i == 6:
		print("empty jug 1 in jug 2");
	elif i == 7:
		print("empty jug 2 in jug 1");

def printSol():
#    print(steps)
    print("Solution :: ->")
    count = 1
    print(visitedNodes[0])
    for i in steps:
    	ruleInWords(i)
    	print(visitedNodes[count])
    	count += 1
    
visitedNodes.append((0, 0))
if findSol(0, 0):
	printSol()
else:
	print("No solution.")
