import tweepy
from textblob import TextBlob

consumer_key = 'Xs2WCj4FcQPDVWFkwmJeB9ifB'
consumer_secret = 'XsPYqgiVmJTvSVUis8y3xQpZ4r1NYJAXvB6DktJFTxoJKFvQII'

access_token = '850423134087991297-hpniDUvR8UJ55TGQvT7cHFk2pjNmXCY'
access_token_secret = 'KbkEtQ2VvttKkpQ1h2jy2g11RUl1J8YEw8qNmdN3TccEy'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

file = open('result.csv', 'w')

for tweet in public_tweets:
	print(tweet.text)
	file.write(tweet.text)
	file.write('\n')
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
	result = 'positive' if analysis.sentiment.polarity > 0 else 'negative'
	file.write('\n--------------\n' + result + '\n--------------\n')
	file.write('\n')

file.close()