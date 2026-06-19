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
        # O(n)
        self.followers[userId].add(userId)
        followee = self.followers[userId]
        min_heap = []

        if len(followee) >= 10:
            # If more than 10 followees,
            # Find the 10 followees
            # need to use max heap since to always pop the least negative
            # timestamp (by keeping them as -timestamp here)
            max_heap = []

            # Find the 10 followee with the most recent tweet
            for f in followee:
                if f in self.tweet_feeds:

                    # idx = position of the tweet that's taking into consideration
                    idx = len(self.tweet_feeds[f]) - 1
                    timestamp, tweet_id = self.tweet_feed[f][idx]
                    heapq.heappush(max_heap, [-timestamp, tweet_id, f, idx - 1])

                    if len(max_heap) > 10:
                        heapq.heappop(max_heap)
            # Add their most recent tweet records in the min_heap
            while max_heap:
                timestamp, tweetId, f, idx = heapq.heappop(max_heap)
                heapq.heappush(min_heap, [-timestamp, tweetId, f, idx])
        
        else:
            # If less than 10 followees, we push to min_heap directly
            for f in followee:
                if f in self.tweet_feeds:
                    idx = len(self.tweet_feeds[f]) - 1
                    timestamp, tweet_id = self.tweet_feeds[f][idx]
                    heapq.heappush(min_heap, [timestamp, tweet_id, f, idx - 1])



        # Start popping from min_heap to get result
        results = []


        while min_heap and len(results) < 10:
            timestamp, tweet_id, f, idx = heapq.heappop(min_heap)
            results.append(tweet_id)
            
            # if the pulled user still have tweet left, add it to the min_heap
            # to take into consideration
            if idx >= 0:
                timestamp, tweet_id = self.tweet_feeds[f][idx]
                heapq.heappush(min_heap, [timestamp, tweet_id, f, idx - 1])
        return results

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
