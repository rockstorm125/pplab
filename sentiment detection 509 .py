import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class TwitterClient(object):

    def __init__(self):

        consumer_key = ''
        consumer_secret = ''
        access_token = ''
        access_token_secret = ''

        try:

            self.auth = OAuthHandler(consumer_key, consumer_secret)

            self.auth.set_access_token(access_token, access_token_secret)

            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")

    def clean_tweet(self, tweet):

        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w+:\/\/\S+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):

        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_tweets(self, query, count=10):

        # empty list to store parsed tweets
        tweets = []

        try:
            # call twitter api to fetch tweets
            fetched_tweets = self.api.search(q=query, count=count)

            # parsing tweets one by one
            for tweet in fetched_tweets:
                # empty dictionary to store required params of a tweet
                parsed_tweet = {}

                # saving text of tweet
                parsed_tweet['text'] = tweet.text
                # saving sentiment of tweet
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)

                # appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)

                else:
                    tweets.append(parsed_tweet)

            # return parsed tweets
            return tweets

        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))

    def get_vader_tweets(self, query, count=10):

        tweets = []

        try:

            fetched_tweets = self.api.search(q=query, count=count)

            for tweet in fetched_tweets:

                parsed_tweet_1 = {}

                parsed_tweet_1['text'] = tweet.text

                parsed_tweet_1['sentiment'] = self.sentiment_score(tweet.text)

                if tweet.retweet_count > 0:

                    if parsed_tweet_1 not in tweets:
                        tweets.append(parsed_tweet_1)

                else:
                    tweets.append(parsed_tweet_1)

            return tweets

        except tweepy.TweepError as e:
            print("Error : " + str(e))

    def sentiment_score(self, tweet):
        sid_obj = SentimentIntensityAnalyzer()

        sentiment_dict = sid_obj.polarity_scores(self.clean_tweet(tweet))

        if sentiment_dict['compound'] >= 0.05:
            return ("Positive")

        elif sentiment_dict['compound'] <= - 0.05:
            return ("Negative")

        else:
            return ("Neutral")

    def vader_analysis(self, tweet):
        sid_obj = SentimentIntensityAnalyzer()

        sentiment_dict = sid_obj.polarity_scores(self.clean_tweet(tweet))

        print("Overall sentiment dictionary is : ", sentiment_dict)
        print("sentence was rated as ", sentiment_dict['neg'] * 100, "% Negative")
        print("sentence was rated as ", sentiment_dict['neu'] * 100, "% Neutral")
        print("sentence was rated as ", sentiment_dict['pos'] * 100, "% Positive")

        print("Sentence Overall Rated As", end=" ")

        if sentiment_dict['compound'] >= 0.05:
            print("Positive \n")

        elif sentiment_dict['compound'] <= - 0.05:
            print("Negative \n")

        else:
            print("Neutral \n")

    def textblob_sentiment(self, tweet):

        analysis = TextBlob(self.clean_tweet(tweet))
        print("Polarity of the tweet: ", analysis.sentiment.polarity)
        print("subjectivity of the tweet: ", analysis.sentiment.subjectivity)
        print(" Tweet rated by Textblob as:", end=" ")
        if analysis.sentiment.polarity > 0:
            print('positive')
        elif analysis.sentiment.polarity == 0:
            print('neutral')
        else:
            print('negative')


def main():
    # creating object of TwitterClient Class
    api = TwitterClient()
    # calling function to get tweets
    que = "Farmers law"  # the query to be searched in twitter.
    tweets = api.get_tweets(query=que, count=10)
    print("----------------------------------------------------------------------------------------------------------")
    print("                                    TextBlob sentiment analysis                                           ")
    print("----------------------------------------------------------------------------------------------------------")

    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    print("Positive tweets percentage: {} %".format(100 * len(ptweets) / len(tweets)))
    # picking negative tweets from tweets
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    # percentage of negative tweets
    print("Negative tweets percentage: {} %".format(100 * len(ntweets) / len(tweets)))
    # percentage of neutral tweets
    print("Neutral tweets percentage: {} % ".format(100 * (len(tweets) - (len(ntweets) + len(ptweets))) / len(tweets)))

    # printing first 5 positive tweets
    print("\n\nPositive tweets:")
    for tweet in ptweets[:2]:
        print(tweet['text'])

    # printing first 5 negative tweets
    print("\n\nNegative tweets:")
    for tweet in ntweets[:2]:
        print(tweet['text'])
    print("----------------------------------------------------------------------------------------------------------")
    print("                                    Vader sentiment analysis                                              ")
    print("----------------------------------------------------------------------------------------------------------")
    tweets_vader = api.get_vader_tweets(query=que, count=10)

    ptweets_vader = [tweet for tweet in tweets_vader if tweet['sentiment'] == 'Positive']

    print("Positive tweets percentage: {} %".format(100 * len(ptweets_vader) / len(tweets_vader)))

    ntweets_vader = [tweet for tweet in tweets_vader if tweet['sentiment'] == 'Negative']

    print("Negative tweets percentage: {} %".format(100 * len(ntweets_vader) / len(tweets_vader)))

    print("Neutral tweets percentage: {} % ".format(
        100 * (len(tweets_vader) - (len(ntweets_vader) + len(ptweets_vader))) / len(tweets_vader)))

    print("\n\nVader Positive tweets:")
    for tweet in ptweets_vader[:2]:
        print(tweet['text'])

    # printing first 5 negative tweets
    print("\n\nVader Negative tweets:")
    for tweet in ntweets_vader[:2]:
        print(tweet['text'])

    print("----------------------------------------------------------------------------------------------------------")
    print("                                Vader sentiment analysis showcase                                         ")
    print("----------------------------------------------------------------------------------------------------------")

    try:
        print(str(ptweets_vader[0]))
        print("\n")
        api.vader_analysis(str(ptweets_vader[0]))

    except:
        print("no positive tweets according to Vader \n ")

    try:
        print(str(ntweets_vader[0]))
        print("\n")
        api.vader_analysis(str(ntweets_vader[0]))
    except:
        print("no negative tweets according to Vader \n")

    print("----------------------------------------------------------------------------------------------------------")
    print("                                Textblob sentiment analysis showcase                                      ")
    print("----------------------------------------------------------------------------------------------------------")

    try:
        print(str(ptweets[0]))
        print("\n")
        api.textblob_sentiment(str(ptweets[0]))
        print("\n")
    except:
        print("no positive tweets according to Textblob \n")

    try:
        print(str(ntweets[0]))
        print("\n")
        api.textblob_sentiment(str(ntweets[0]))
        print("\n")
    except:
        print("no negative tweets according to Textblob \n")


if __name__ == "__main__":
    # calling main function
    main()
