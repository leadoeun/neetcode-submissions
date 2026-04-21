class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        maplist = []
        wordlist = []
        for word in strs:
            wordmap = {}
            for s in word:
                if s in wordmap.keys():
                    wordmap[s] += 1
                else:
                    wordmap[s] = 1

            try:
                idx = maplist.index(wordmap) 
            except ValueError:
                idx = -1
            if idx != -1:
                wordlist[idx].append(word)
            else:
                maplist.append(wordmap)
                wordlist.append([word])
                
            


            
        
        return wordlist
        