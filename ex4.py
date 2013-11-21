"""
4th exc --> gimatryia
"""

user_string = "aaa"

def gimatry(user_string):
	val = 0
	for s in user_string:
		val += ord(s) - ord('a') + 1
	return val

val1 = gimatry(user_string)

print val1