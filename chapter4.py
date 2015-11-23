import timeit


edges = []
for line in open("twitter.txt"):
    name_a, name_b = line.strip().split(';')
    edges.append((name_a, name_b))

'''
print(edges[:10])
'''


def following(user, edges):
	"returns list of all users USER is following"
	followees = []
	for follower, followee in edges:
		if follower == user:
			followees.append(followee)
	return followees
	
'''
print(following("@Fox", edges))


%timeit following("@Fox", edges)

timeit.Timer('following("@Fox", edges)').repeat(3, 1000)
'''


def starts_with_vowel(word):
	vowel = 'aeiouAEIOU'
	if word[0] in vowel:
		return True
	else:
		return False
		

'''		
print(starts_with_vowel("egg") == True)
print(starts_with_vowel("bacon") == False)
'''


def add_suffix(word, suffix):
	"Returns WORD with SUFFIX attached"
	word += suffix
	return word

'''
print(add_suffix("egg", "ay") == "eggay")
print(add_suffix("egg", "oing") == "eggoing")
'''





