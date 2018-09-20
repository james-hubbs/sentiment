## Presidential Sentiment Analysis Using Twitter Data

### Introduction
In this project, I scraped 6000 tweets about President Trump and 6000 tweets about President Obama and preformed a baseline sentiment analysis to determine whether or not the average sentiment between the two sets of tweets was different.

Methods Used: web scraping, sentiment analysis, data visualizations, inferential statistics.

### Data Collection
The data were scraped on 9/19/2018 using the tweet_scraper.py module found within my [Scrapers repository](https://github.com/james-hubbs/Scrapers).

### Methodology
Determining the sentiment or opinion of a given piece of text is a difficult task, and modern methods accomplish this through deep learning. This project takes a simpler, knowledge-based approach. I make use of the NLP library TextBlob and combine information returned from its sentiment module along with information generated from scratch. Specifically, a given tweet is scored by taking the average of its TextBlob polarity and its "simple score." This simple score is calculated by looking up each word of the tweet in a dictionary of positive/negative words. If p is the number of positive words in the tweet, and n the number of negative words, then that tweet recieves a simple score of (-1)*n + (1)p. Values are then normalized within [-1, 1]. This is then averaged with the TextBlob polarity to determine the final sentiment score for the tweet.

### Results
To see the results, visit the [results notebook](https://github.com/james-hubbs/sentiment/blob/master/results.ipynb).

### Sources
The lists of positive/negative words used in the sentiment scoring function were taken from:

Minqing Hu and Bing Liu. "Mining and Summarizing Customer Reviews." 
Proceedings of the ACM SIGKDD International Conference on Knowledge  
and Data Mining (KDD-2004), Aug 22-25, 2004, Seattle, Washington, USA
