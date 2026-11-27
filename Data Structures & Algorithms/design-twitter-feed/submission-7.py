class Twitter:

    def __init__(self):
        self.follows = defaultdict(set) # user -> following list
        self.tweets = defaultdict(list) # user -> tweets
        self.count = 0

        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.count, tweetId]) # [order of post, userId, tweetId]
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # we create a heap of length k (maxheap, as we want the most recent posts i.e. highest count)
        # fetch the most recent from EACH person the user is following (including themself)
        # 10 times, add the heappop to the ret, then heappush THAT person's next most recent.
        heap = []

        for f in self.follows[userId] | {userId}:
            if self.tweets[f]:
                count, tweetId = self.tweets[f][-1]
                heapq.heappush(heap, (-count, tweetId, f, 1))
        
        ret = []
        while heap and len(ret) < 10:
            _, tweetId, f, idx = heapq.heappop(heap)
            ret.append(tweetId)
            idx += 1
            if len(self.tweets[f]) >= idx:
                count, tweetId = self.tweets[f][-idx]
                heapq.heappush(heap, (-count, tweetId, f, idx))
        
        return ret
            



        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
        
