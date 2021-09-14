from searchtweets import ResultStream, gen_request_parameters, load_credentials, collect_results
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    #note: depending on how you installed (e.g., using source code download versus pip install), you may need to import like this:
    #from vaderSentiment import SentimentIntensityAnalyzer

search_args = load_credentials("C:\\Users\\super\\PycharmProjects\\Tweetio\\twitter_keys.yaml",
                                       yaml_key="search_tweets_v2",
                                       env_overwrite=False)
query = gen_request_parameters("snow", results_per_call=100, granularity=None)
print(query)

tweets = collect_results(query,
                         max_tweets=100,
                         result_stream_args=search_args)   # change this if you need to
[print(tweet, end='\n\n') for tweet in tweets[0:10]]

print(tweets[0]["data"][0]['text'])

newlist = [tweet for tweet in tweets[0]["data"]]
print(newlist[1]['text'])

analyzer = SentimentIntensityAnalyzer()
for item in range(len(newlist)):
    vs = analyzer.polarity_scores(newlist[item]['text'])
    print(vs)
