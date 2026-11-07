import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free = [(w, i) for i, w in enumerate(servers)]  # (weight, index)
        heapq.heapify(free)
        busy = []  # (free_time, weight, index)
        res = []
        t = 0

        for j, dur in enumerate(tasks):
            t = max(t, j)  # task j arrives at second j

            # If no server is free, jump ahead to the earliest finish time
            if not free:
                t = max(t, busy[0][0])

            # Release all servers that have finished by time t
            while busy and busy[0][0] <= t:
                _, w, i = heapq.heappop(busy)
                heapq.heappush(free, (w, i))

            w, i = heapq.heappop(free)
            res.append(i)
            heapq.heappush(busy, (t + dur, w, i))

        return res