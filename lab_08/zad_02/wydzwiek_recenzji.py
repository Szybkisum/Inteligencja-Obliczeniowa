from nltk.sentiment.vader import SentimentIntensityAnalyzer
import text2emotion as te

with open("positive.txt", "r") as article_file:
    positive_review = article_file.read()

with open("negative.txt", "r") as article_file:
    negative_review = article_file.read()

sid = SentimentIntensityAnalyzer()

scores_pos = sid.polarity_scores(positive_review)
emo_pos = te.get_emotion(positive_review)
print(positive_review, "\n")
print("Positive review with Vader:", scores_pos, "\n")
print("Positive review with Text2Emotion:", emo_pos, "\n")


scores_neg = sid.polarity_scores(negative_review)
emo_neg = te.get_emotion(negative_review)
print( negative_review, "\n")
print("Negative review with Vader:", scores_neg, "\n")
print("Negative review with Text2Emotion", emo_neg, "\n")