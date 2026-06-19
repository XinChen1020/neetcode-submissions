class Twitter:

    def __init__(self):

        # O()
        self.tweet_feeds = defaultdict(deque)
        self.followers = defaultdict(set)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_feeds[userId].append((self.timestamp, tweetId))
        if len(self.tweet_feeds[userId]) > 10:
            self.tweet_feeds[userId].popleft()
        self.timestamp -= 1



    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        users = self.followers[userId] | {userId}

        for user in users:
            feed = self.tweet_feeds[user]
            if feed:
                idx = len(feed) - 1  # newest tweet is at the right
                timestamp, tweetId = feed[idx]
                heapq.heappush(heap, (timestamp, tweetId, user, idx - 1))

        results = []

        while heap and len(results) < 10:
            timestamp, tweetId, user, next_idx = heapq.heappop(heap)
            results.append(tweetId)

            if next_idx >= 0:
                next_timestamp, next_tweetId = self.tweet_feeds[user][next_idx]
                heapq.heappush(heap, (next_timestamp, next_tweetId, user, next_idx - 1))

        return results

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
