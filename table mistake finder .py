
def iscorrect(Number,Table):
	i=1
	for item in Table:
		if item==Number*i:
			i=i+1
		elif  i>10:
			break
		else:
			print("he is frood")
			print(f"he cheat, {item} is wrong, correct is {Number*i}")
			i=i+1

iscorrect(7,[7,23,14,54,68,35,35,8,4])