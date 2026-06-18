class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # The optimal way of scheduling (under this constrain) : 
        # ==> ALWAYS TRY TO PIPELINE.
        # once you use "A" you need to wait for "t + n" units to use "A" again
        # 1. make a freq_map
        # 2. pick the task with the most frequency, ( so we have a cooldown of n sec)
        # 3. now keep on picking the other elements


        # hash_map = {}
        # for task in tasks:
        #     if task not in hash_map:
        #         hash_map[task]=[1,1]  # frequency, time when we can pick this again
        #     else:
        #         hash_map[task][0]+=1
        # t=1
        # while 1:
        #     all_elems_done = 1
        #     for task, info in hash_map.items():
        #         if info[0] != 0 : # there are still characters to be scheduled
        #             all_elems_done = 0
        #             if t >= info[1] :
        #                 # info[1] = t + n + 1 # not same as below right ? 
        #                 # info is a seprate object ?
                        
        #                 # These two are same
        #                 # hash_map[task][1] = t + n + 1
        #                 # hash_map[task][0] -= 1 
        #                 info[1] = t + n + 1
        #                 info[0] -= 1 
        #         t+=1
        #         if all_elems_done :
        #             break
        # return t

        # 1. Count frequencies
        counts = Counter(tasks)

        # 2. Max-Heap: store negative counts because Python has a min-heap
        # We only care about the frequencies, not the actual task names ("A", "B", etc.)
        max_heap = [-cnt for cnt in counts.values()]
        heapq.heapify(max_heap)

        # 3. Cooldown queue: stores tuples of (neg_freq, time_when_available)
        cooldown_queue = deque()

        time = 0

        # Run until both the ready pool (heap) and waiting pool (queue) are empty
        while max_heap or cooldown_queue:
            time += 1

            # Check if any task in the cooldown queue is ready to be released
            if cooldown_queue and cooldown_queue[0][1] == time:
                ready_task_neg_cnt, _ = cooldown_queue.popleft()
                heapq.heappush(max_heap, ready_task_neg_cnt)

            # If we have tasks available to execute, pick the one with highest frequency
            if max_heap:
                # Pop the task with the most remaining work (most negative)
                neg_cnt = heapq.heappop(max_heap)
                # "Execute" it by reducing its remaining count (adding 1 towards 0)
                neg_cnt += 1

                # If there are still instances of this task left, put it in cooldown
                if neg_cnt < 0:
                    cooldown_queue.append((neg_cnt, time + n + 1))

            # If max_heap is empty but cooldown_queue has items,
            # the CPU automatically idles for this 'time' unit.

        return time