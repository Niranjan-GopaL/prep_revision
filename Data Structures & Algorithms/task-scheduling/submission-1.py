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
        
        counts = Counter(tasks)
        f_max = max(counts.values())

        # Count how many tasks have this absolute maximum frequency
        n_max = sum(1 for count in counts.values() if count == f_max)

        # Formula implementation
        ans = (f_max - 1) * (n + 1) + n_max

        # If the formula yields less than total tasks, it means no idles are needed
        return max(ans, len(tasks))