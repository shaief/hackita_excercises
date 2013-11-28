
def palindrom(user_word):
	for i in range(len(user_word)/2):
		if (user_word[i] <> user_word[-i-1]):
			print user_word +" is not a palindrom!"
			return
	print user_word + " is a palindrom!!!"
	return

def palindrom_one_liner(user_word):
	[x=1 if (user_word[i] <> user_word[-i-1]) for i in range(len(user_word)/2)]
	print user_word + " is a palindrom!!!"
	return

print "enter a word: "
u_word = raw_input()

palindrom_one_liner(u_word)
