import heapq
class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free = [(w, i) for i, w in enumerate(servers)]  
        heapq.heapify(free)
        busy = []  
        res = []
        t = 0
        for j, dur in enumerate(tasks):
            t = max(t, j) 
            if not free:
                t = max(t, busy[0][0])
            while busy and busy[0][0] <= t:
                _, w, i = heapq.heappop(busy)
                heapq.heappush(free, (w, i))
            w, i = heapq.heappop(free)
            res.append(i)
            heapq.heappush(busy, (t + dur, w, i))
        return res