from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    return wordnet.NOUN

with open("article.txt", "r") as article_file:
    content = article_file.read().lower()
print("a) artykuł o filmie dokumentalnym 20 lat po premierze")

word_tokens = word_tokenize(content)
print("b) Liczba słów po tokenizacji:", len(word_tokens))

stop_words = stopwords.words('english')
filtered_words = [w for w in word_tokens if not w in stop_words]
print("c) Liczba słów po usunięciu stop-words:", len(filtered_words))

filtered_words = [w for w in filtered_words if w.isalpha()]
print("d) Liczba słów po usunięciu dodatkowych słów:", len(filtered_words))

lemmatizer = WordNetLemmatizer()
pos_tags = pos_tag(filtered_words)
lemmetized_words = [lemmatizer.lemmatize(w, get_wordnet_pos(t)) for w, t in pos_tags]
print("e) Liczba słów po lematyzacji:", len(set(lemmetized_words)))

word_freq = Counter(lemmetized_words)
print("f) Wektor zliczonych słów:", word_freq)

most_common = word_freq.most_common(10)
words, counts = zip(*most_common)
plt.figure(figsize=(10, 5))
plt.bar(words, counts, color='skyblue')
plt.title("Top 10 najczęstszych słów")
plt.xlabel("Słowa")
plt.ylabel("Liczba wystąpień")
plt.savefig("bag_hist.png")

text_for_cloud = ' '.join(lemmetized_words)
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_for_cloud)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Chmura tagów")
plt.savefig("bag_cloud.png")