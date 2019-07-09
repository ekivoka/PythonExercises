with open("test.txt", "r") as a, open("rev.txt", "w") as b:
	x = a.read().splitlines()
	b.write("\n".join(x[::-1]))
