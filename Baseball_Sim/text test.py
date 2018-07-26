def getSum(fileName):
	nums = []
	infile = open(fileName, 'r')
	for line in infile:
		line = line.split()
		nums.append(float(line[1]))
		print(line)
	print(sum(nums))
getSum('all_last.txt')