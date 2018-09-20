"""sentiment.py: A script used for the project __Presidential Sentiment Analysis Using Twitter Data__"""

import os
import csv
import string
from textblob import TextBlob


def getwords():
    """Returns the li
    sts of positive/negative words"""
    positives = []
    negatives = []

    with open("words/positive-words.txt") as file:
        for line in file:
            positives.append(line.strip())

    with open("words/negative-words.txt") as file:
        for line in file:
            negatives.append(line.strip())

    return positives, negatives


def gettweets(filename):
    """ Reads in tweet data from sentiment\data\filename
        Removes punctuation and returns a list of the tweets
    """
    translator = str.maketrans('', '', string.punctuation)

    with open("data/{}".format(filename), 'r') as file:
        reader = csv.reader(file)
        tweets = []
        for row in reader:
            text = row[4]
            text = text.translate(translator).strip().lower()  # Remove punctuation
            tweets.append(text)

        tweets.remove("tweet text")  # Remove the header

    return tweets


def normalize(x, min, max):
    """Normalize a score x so that it falls within [-1, 1]"""
    return 2*((x-min)/(max - min)) - 1


def scores(tweets):
    """
    Scores each element in a list of strings for its sentiment.

    Parameters -- tweets: a list of strings to be scored for sentiment
    Returns -- A list of scores corresponding to each element in the
               inputted list. Each value is within [-1, 1]. Negative
               values indicates negative sentiment; positive values
               indicate positive sentiment.
    """
    positives, negatives = getwords()

    simple_scores = []
    polarity_scores = []

    for tweet in tweets:
        words = tweet.split()
        score = 0
        for word in words:
            if positives.__contains__(word):
                score += 1
            if negatives.__contains__(word):
                score -= 1
        simple_scores.append(score)

        testimonial = TextBlob(tweet)
        polarity_scores.append(testimonial.sentiment.polarity)

    minimum = min(simple_scores)
    maximum = max(simple_scores)
    normal_scores = [normalize(x, minimum, maximum) for x in simple_scores]

    final_scores = [(x+y)/2 for x, y in zip(normal_scores, polarity_scores)]
    return final_scores


def classify(score):
    """Classifies a score using a simple decision rule"""
    if score <= -0.15:
        return "Negative"
    elif score >= 0.15:
        return "Positive"
    elif -0.15 < score < -0.05 or 0.05 < score < 0.15:
        return "Unsure"
    else:
        return "Neutral"


def to_csv(scores, classes, tweets, filename):
    """Write scores/classes/tweets to CSV"""
    with open("data/{}".format(filename), 'w', newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Sentiment Scores", "Classification", "Tweet Text"])
        for score, cls, tweet in zip(scores, classes, tweets):
            writer.writerow([score, cls, tweet])

        print("Created {} in {}\data".format(filename, os.getcwd()))


if __name__ == '__main__':
    # Read in Trump tweet data
    trump_tweets = gettweets("trump.csv")
    trump_tweets += gettweets("trump2.csv")

    # Compute scores, classify, and write results to csv
    trump_scores = scores(trump_tweets)
    trump_cls = [classify(x) for x in trump_scores]
    to_csv(trump_scores, trump_cls, trump_tweets, "trumpresults.csv")

    # Read in Obama tweet data
    obama_tweets = gettweets("obama.csv")
    obama_tweets += gettweets("obama2.csv")

    # Compute scores, classify, and write results to csv
    obama_scores = scores(obama_tweets)
    obama_cls = [classify(x) for x in obama_scores]
    to_csv(obama_scores, obama_cls, obama_tweets, "obamaresults.csv")