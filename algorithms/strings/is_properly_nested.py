def is_properly_nested(expr):
	counter = 0
	for ch in expr:
		if ch == '(':
			counter += 1
		elif ch == ')':
			counter -= 1
			if counter < 0:
				return False
				
	return counter == 0
		

print(is_properly_nested("(8 * 3) + (20 / (7 - 3))"))
