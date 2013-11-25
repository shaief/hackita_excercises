print "enter a string: "
user_string = raw_input()
char_dict = {}
for s in user_string:
    if s not in char_dict:
        char_dict[s]=0
    char_dict[s] += 1
print char_dict

import collections
count_dict = collections.Counter()
for s in user_string:
    count_dict[s] += 1
print count_dict