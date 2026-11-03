import numpy as np
from collections import Counter

def calculate_bm25_scores(corpus, query, k1=1.5, b=0.75):
	# Your code here
	if len(corpus) == 0 or len(query) == 0:
		raise ValueError

	tf_map = {}
	N = len(corpus)
	avgdl = sum([len(doc) for doc in corpus]) / N
	for j, doc in enumerate(corpus):
		doc_len = len(doc)
		for word in doc:
			if word not in tf_map:
				tf_map[word] = {j: 0}
			if j not in tf_map[word]:
				tf_map[word][j] = 0
			tf_map[word][j] += 1

	scores = np.zeros(len(corpus))
	for doc_id, doc in enumerate(corpus):
		doc_len = len(doc)
		scores[doc_id] = np.sum(np.array([np.log((N + 1) / (len(tf_map[term]) + 1)) * tf_map[term][doc_id] * (k1+1) / (tf_map[term][doc_id] + (k1 * (1 - b + (b * doc_len / avgdl)))) if term in tf_map and doc_id in tf_map[term] else 0.0 for term in query]))

	return np.round(scores, 3)