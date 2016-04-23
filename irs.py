import glob, os, re
from collections import defaultdict

def tokenize(text, lowercase=True):
	text = text.lower() if lowercase else text
	for match in re.finditer(r"\w+(\.?\w+)*", text):
		yield match.group()

class IRSystem:
	'''Simple Information Retrieval System'''
	
	def __init__(self):
		self.tdf = defaultdict(set)
		self.doc_ids = []

	def index_document(self, doc_id, words):
		self.doc_ids.append(doc_id)

	def index_collection(self, filenames):
		for filename in filenames:
			self.index_document(os.path.basename(filename), 
								tokenize(open(filename).read()))

s = IRSystem()
s.index_collection(glob.glob('haggard/*.txt'))

print('The Ghost Kings 8184.txt' in s.tdf['master'])
print('Cleopatra 2769.txt' in s.tdf['children'])
