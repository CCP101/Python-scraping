from twitter import Twitter, OAuth

#Make sure to add the access tokens and consumer keys for your application
t = Twitter(auth=OAuth("Access Token","Access Token Secret","Consumer Key","Consumer Secret"))
pythonTweets = t.search.tweets(q = "#python")
print(pythonTweets)
# twitter refuse my application of API for academy,this can`t  be active