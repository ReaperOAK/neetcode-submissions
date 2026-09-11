class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)  # userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set)  # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        if len(self.tweetMap[userId]) > 10:
            self.tweetMap[userId].pop(0)
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.followMap[userId].add(userId)
        minHeap=[]
        for followee in self.followMap[userId]:
            i=len(self.tweetMap[followee])-1
            if i>=0:
                count,tweetId=self.tweetMap[followee][i]
                minHeap.append([count,tweetId,followee,i])
        heapq.heapify(minHeap)
        res=[]

        while minHeap and len(res)<10:
            count,tweetId,followee,index=heapq.heappop(minHeap)
            res.append(tweetId)
            if index>0:
                count,tweetId=self.tweetMap[followee][index-1]
                heapq.heappush(minHeap, [count,tweetId,followee,index-1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)