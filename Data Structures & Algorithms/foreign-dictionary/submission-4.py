# obsrvation 1 : they gave the input words in sorted order (according to their order)
# CYCLE in the DAG causes invalid input
# if w_i and w_i+1 have same prefix BUT wi is LONGER => invalid
# then just topo sort + cycle detect

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)

        # This is wrong, but the below is correct (something about uniqueness) ?? check later
        # adjacency set() so that we don't have duplicates
        # g={}
        # for w in words:
        #     for c in w:
        #         g[c] = set()

        g = {c: set() for w in words for c in w}    


        # we have a DAG
        for i in range(n-1):
            w1 = words[i]
            w2 = words[i+1]
            # check if w2 is a prefix of w1 and shorter
            if len(w1) > len(w2) and w1[:len(w2)] == w2 :
                return ""
            lenght=min(len(w1), len(w2) )
            for j in range(lenght):
                if w1[j] != w2[j]: # w1[j] -> w2[j]
                    g[w1[j]].add(w2[j]) 
                    break
        

        # VERY IMPORTANT LESSON :
        # Be very careful while returning Nones and ""
        # any successful run will return None and in the check=="" if check is None, it'll still trigger it

        # Toposort ordering with cycle detection
        # vis = [0]*26
        # ans = []
        # def dfs(i):
        #     vis[ord(i)-97]=1
        #     for v in g[i]:
        #         if vis[ord(v)-97]==0:
        #             check = dfs(v)
        #             if check == "":
        #                 return ""
        #         elif vis[ord(v)-97]==1:
        #             return ""
        #     ans.append(i) # according to finish time of a node
        #     vis[ord(i)-97]=2
        # vis = [0]*26


        vis = [0]*26
        ans = []
        def dfs(i):
            vis[ord(i)-97]=1
            for v in g[i]:
                if vis[ord(v)-97]==0:
                    if not dfs(v):
                        return False
                elif vis[ord(v)-97]==1:
                    return False
            ans.append(i) # according to finish time of a node
            vis[ord(i)-97]=2
            return True

        # This is wrong cuz we need to traverse t
        
        # for i in g.keys():
        #     if  vis[ord(i)-97]==0:
        #         dfs(i)

        for i in range(26):
            c = chr(i+97)
            if  c in g and vis[i]==0:
                if not dfs(c):
                    return ""


        return ''.join(ans[::-1])