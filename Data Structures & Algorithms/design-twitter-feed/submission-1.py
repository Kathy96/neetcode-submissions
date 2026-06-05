class Twitter:

    def __init__(self):
        self.relationship = {} # key=followerId, value=set(followeeId)
        self.tweets = {} # key=userId, value = [(time, tweetId)]
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        if userId not in self.relationship:
            self.relationship[userId] = set()
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        self.relationship[userId].add(userId)
        for followeeId in self.relationship[userId]:
            if followeeId in self.tweets:
                for time, tweetId in self.tweets[followeeId]:
                    heapq.heappush(minHeap, (time, tweetId))
                    if len(minHeap) > 10:
                        heapq.heappop(minHeap)
        res = []
        while minHeap:
            res.append(heapq.heappop(minHeap)[1])
        return res[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.relationship:
            self.relationship[followerId] = set()
        self.relationship[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.relationship[followerId]:
            self.relationship[followerId].remove(followeeId)
