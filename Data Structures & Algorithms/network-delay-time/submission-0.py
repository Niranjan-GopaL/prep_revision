import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # 1. make adj list
        # 2. dikjstra's algo 

        dist=[float('inf')]*(n+1)
        dist[k]=0
        g=[ [] for _ in range(n+1)]
        for u,v,w in times:
            g[u].append((v,w))
        pq = []
        # (distance_from_source, node) is pushed into pq
        heapq.heappush(pq, (0,k))
        while pq:
            d,u=heapq.heappop(pq)
            if d>dist[u]:continue # we need d only so that we don't process longer edges
            for v,w in g[u]:
                if dist[u]+w < dist[v]: # if going to v through u is helpful
                    dist[v]=dist[u]+w
                    heapq.heappush(pq,(dist[v], v))
        mx=max(dist[1:])
        return -1 if mx==float('inf') else mx