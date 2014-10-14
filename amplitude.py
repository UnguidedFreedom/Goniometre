"""[(t1,<1),(t2,<2),(t3,<3)]"""

def anglemin(ls):
	mini = 360
	i=0
	while i < len(ls):
		if ls[i][1] < mini:
			mini = ls[i][1]
		i+=1
	return mini

def anglemax(ls):
	maxi = 0
	i=0
	while i < len(ls):
		if ls[i][1] > maxi:
			maxi = ls[i][1]
		i+=1
	return maxi

def amplitude(ls):
	mini = anglemin(ls)
	maxi = anglemax(ls)
	return maxi-mini
