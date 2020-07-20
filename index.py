from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


def embed_corpus(corpus):
    embedder = SentenceTransformer('bert-base-nli-mean-tokens')
    return embedder.encode(corpus)

def get_string_permutations(l):
    permutations = []
    for i in range(len(l)):
        elem = ""
        for j in range(len(l) - i):
            elem += " " + l[i + j]
            permutations.append(elem)
    return permutations

def index_of_max(l):
    index = 0
    for i in range(1, len(l)):
        if l[i] > l[index]:
            index = i
    return index

class Sentence:
    def __init__(self, sentence, comparisons):
        self.sentence = sentence
        self.comparisons = comparisons

    def sentimental_subphrase(self):
        permutations = get_string_permutations(self.sentence.split(" "))
        embeddings = embed_corpus(permutations)
        similarity_scores = cosine_similarity(embeddings, self.comparisons)
        best_score_index = index_of_max(similarity_scores)
        return permutations[best_score_index]
        
#TESTS
pos_comparisons1 = embed_corpus(["good"])
neg_comparisons1 = embed_corpus(["bad"])

sentence1 = "Car not happy, big big dent in boot! Hoping theyre not going to write it off, crossing fingers and waiting"
sentence2 = "i lost all my friends, i`m alone and sleepy"
sentence3 = "His snoring is so annoying n it keeps me from sleeping (like right now, lol) but I honestly wud miss it if it eva left  I love him."
sentence4 = "Looking forward to your gig in Ireland"

s1 = Sentence(sentence1, neg_comparisons1)
s2 = Sentence(sentence2, neg_comparisons1)
s3 = Sentence(sentence3, neg_comparisons1)
s4 = Sentence(sentence4, pos_comparisons1)

print(s1.sentence +" SUBPHRASE: " +  s1.sentimental_subphrase())
print(s2.sentence +" SUBPHRASE: " +  s2.sentimental_subphrase())
print(s3.sentence +" SUBPHRASE: " +  s3.sentimental_subphrase())
print(s4.sentence +" SUBPHRASE: " +  s4.sentimental_subphrase())
