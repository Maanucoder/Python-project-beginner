#function
def iscorrect(Number,Table):
	i=1
	for item in Table
#To check that table correct or not.
		if item==Number*i:
			i=i+1
#such that table only gave 10 multiple
		elif  i>10:
			break
#if function find any mistake
		else:
			print("he is frood")
			print(f"he cheat, {item} is wrong, correct is {Number*i}")
			i=i+1
