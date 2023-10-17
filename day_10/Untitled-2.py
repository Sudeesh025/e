# Python3 program to check for
# balanced brackets.

# function to check if
# brackets are balanced


def areBracketsBalanced(expr):
	count=0
	stack = []
	rem=0
	# Traversing the Expression
	for char in expr:
		if char in ["(", "{", "["]:
			stack.append(char)
			count=count+1
			rem=rem+1
		else:
			if not stack:
				return False
			current_char = stack.pop()
			if current_char == '(':
				if char != ")":
					return count
				else:
					count=count+1
					rem=rem-1
			if current_char == '{':
				if char != "}":
					return count
				else:
					rem=rem-1
					count=count+1
			if current_char == '[':
				if char != "]":
					return count
				else:
					rem=rem-1
					count=count+1
	if(rem==0):
		return rem
	else:
		return count



expr =input()
a=areBracketsBalanced(expr)
print(a)
