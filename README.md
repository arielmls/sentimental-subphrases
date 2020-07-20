# sentimental-subphrases
This project is an experiment to determine if Google's BERT can be used to determine the sub-phrase of a sentence which determines its sentiment (positive/negative).

The idea is that BERT will be very successful at determining the relationship between phrases and sentiments, even when the words of the phrase only create that sentiment when in the context of each other. 

embed_corpus(corpus):
corpus: List of Strings
Returns a BERT embedding of corpus

get_string_permutations(l):
l: String
Returns a list of permutations of all of the possible subphrases of l. 
EX: 
get_string_permutations("I like to eat") => ["I", "I like", "I like to", "I like to eat", "like", "like to", "like to eat", "to", "to eat", "eat"]

Sentence.sentimental_subphrase():
self.sentence: String
self.comparisons: BERT embedding
Returns the subphrase of self.sentence with the highest cosine similarity (of its embedding) to comparisons
EX:
s = Sentence("Looking forward to your gig in Ireland", embed_corpus(["good"])
s.sentimental_subphrase() => "looking forward"


This code has not been thoroughly tested for accuracy, however the tests that have been done yielded promising results. For example, it found that in the sentence, "Looking forward to your gig in Ireland", the subphrase that implies positive sentiment is "looking forward," despite "looking" and "forward" not having inherent positive sentiment out of context. 
