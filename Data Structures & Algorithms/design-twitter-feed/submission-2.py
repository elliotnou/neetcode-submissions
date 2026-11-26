class Twitter:

    def __init__(self):
        # list of userIDs
        # dict of userID -> list of tweetIDs
        # dict of userID -> following userIDs
        self.users = set()
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)
        self.postnum = 1
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.postnum, tweetId])
        self.postnum += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        # heapify the tweets and keep replacing until everything is from themselves or from someone they follow
        # join all the tweets from everyone this person follows
        # 

        # n is the number of people userId follows - heap should be this long.
        feed, heap = [], []
        for user in self.follows[userId] | {userId}:
            if self.tweets[user]:
                idx = len(self.tweets[user]) - 1
                time, tweetId = self.tweets[user][idx]                 
                heapq.heappush(heap, (-time, tweetId, user, idx)) # [postnum, tweetId, userId]
        # we've added all the first to the heap

        while heap and len(feed) < 10:
            time, tweet, user, idx = heapq.heappop(heap)
            feed.append(tweet)
            if idx > 0:
                time, tweetId = self.tweets[user][idx - 1]
                heapq.heappush(heap, (-time, tweetId, user, idx-1))

        return feed




    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
        
