class Twitter:

    def __init__(self):
        self.tweet_feeds = defaultdict(deque)
        self.followers = defaultdict(set)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_feeds[userId].append((self.timestamp, tweetId))
        if len(self.tweet_feeds[userId]) > 10:
            self.tweet_feeds[userId].popleft()
        self.timestamp -= 1



    def getNewsFeed(self, userId: int) -> List[int]:
        followee = self.followers[userId]
        candidaties = []
        for f in followee:
            candidaties += self.tweet_feeds[f]
        candidaties += self.tweet_feeds[userId]
        heapq.heapify(candidaties)
        
        results = []

        while candidaties and len(results) < 10:
            results.append(heapq.heappop(candidaties)[1])

        return results

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
