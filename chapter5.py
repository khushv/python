# http://nbviewer.ipython.org/github/fbkarsdorp/python-course/blob/master/Chapter%204%20-%20Programming%20principles.ipynb

from chapter3 import *
from collections import defaultdict

def automatic_readability_index(n_chars, n_words, n_sents):
	#computes ARI given N_CHARS, N_WORDS, N_SENTS	
	return ((4.71 * (n_chars/n_words)) + (0.5*(n_words/n_sents)) - 21.43)
	

#print(abs(automatic_readability_index(300, 40, 10) - 15.895) < 0.001)

def extract_counts(sentences):
	#takes SENTENCEs input and returns number of characters, number of words and number of sentences as tuple
	n_chars = 0
	n_words = 0
	n_sents = len(sentences)
	for sentence in sentences:
		for word in sentence:
			n_words += 1 
			for char in word:
				n_chars += 1
	return n_chars, n_words, n_sents

'''

sentences = [["this", "was", "rather", "easy"], 
             ["Please", "give", "me", "something", "more", "challenging"]]

n_chars, n_words, n_sents = extract_counts(sentences)
print(automatic_readability_index(n_chars, n_words, n_sents))
'''

def compute_ARI(sentences):
	#computers ARI from SENTENCES
	n_chars, n_words, n_sents = extract_counts(sentences)
	return automatic_readability_index(n_chars, n_words, n_sents)
'''
print(abs(compute_ARI(sentences) - 4.442) < 0.001)


##############################
##############################
##############################
##############################
##############################
'''



def predict_author(text, feature_database):
	"predict author behind text"
	return classify(score(extract_features(text), feature_database))


	
def classify(scores):
	return max(scores.keys(), key=(lambda k: scores[k]))


def extract_features(filename):
	return tokenize(read_corpus_file(filename))


feature_database = defaultdict(lambda: defaultdict(int))

def extract_author(filename):
	test = remove_dir(filename)
	test2 = remove_ext(test)
	return test2

'''
extract_author("Austen-emma.txt")
print(extract_author("/path/to/Austen-emma.txt") == "Austen")
print(extract_author("Austen-emma.txt") == "Austen")
'''

def update_Counts(author, text, feature_database):
	#adds author and text into database
	feature_database.append(author, text)
	return feature_database


feature_database = defaultdict(lambda: defaultdict(int))

feature_database = update_counts("Anonymous", "This was written with a lack of inspiration", feature_database)
								 
test_database = defaultdict(lambda: defaultdict(int))

for word in "This was written with a lack of inspiration".split():
    test_database["Anonymous"][word] += 1
print(sorted(feature_database.items()) == sorted(test_database.items())



