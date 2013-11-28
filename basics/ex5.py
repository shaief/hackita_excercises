
def palindrom(user_word):
	for i in range(len(user_word)/2):
		if (user_word[i] <> user_word[-i-1]):
			print user_word +" is not a palindrom!"
			return
	print user_word + " is a palindrom!!!"
	return

def palindrom_one_liner(user_word):
	if user_word == user_word[::-1]:
		return True
	return False

print "enter a word: "
u_word = raw_input()

print palindrom_one_liner(u_word)
