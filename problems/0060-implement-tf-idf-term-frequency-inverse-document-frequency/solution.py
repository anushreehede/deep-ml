import numpy as np
import math
def compute_tf_idf(corpus, query):
	"""
	Compute TF-IDF scores for a query against a corpus of documents.
    
	:param corpus: List of documents, where each document is a list of words
	:param query: List of words in the query
	:return: List of lists containing TF-IDF scores for the query words in each document
	"""
	tf_map = {}
	for j, doc in enumerate(corpus):
		doc_len = len(doc)
		for word in doc:
			if word not in tf_map:
				tf_map[word] = {j: 0}
			if j not in tf_map[word]:
				tf_map[word][j] = 0
			tf_map[word][j] += 1

	df_map = {}
	N = len(corpus)
	for word in tf_map:
		df_map[word] = math.log((N+1) / (len(tf_map[word]) + 1)) + 1
		for doc_id in tf_map[word]:
			tf_map[word][doc_id] /= len(corpus[doc_id])
	
	tf_idf_scores = []
	for doc_id in range(N):
		doc_tf_idf = []
		for q in query:
			tfidf = ((tf_map[q][doc_id] if doc_id in tf_map[q] else 0.0) * df_map[q]) if q in df_map else 0.0
			doc_tf_idf.append(round(tfidf, 5))
		tf_idf_scores.append(doc_tf_idf)

	return tf_idf_scores

