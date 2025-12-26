def listaPrimos2(a, b):
	order = range(a, b)
	if a > b:
		order = range(b, a)
	
	for i in order:
		if i == 1 or i == 2:
			print(i)
		for j in range(2,i):
			if i%j == 0:
				break
			elif j == i-1:
				print(i)