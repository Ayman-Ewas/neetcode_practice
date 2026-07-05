class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        for i in strs:
            flag = True
            original = ''.join(sorted(i))
            for j in range(len(result)):
                # for k in range(len(result[j])):
                exist = ''.join(sorted(result[j][0]))
                if original == exist:   
                    result[j].append(i)
                    flag = False
                    

            if flag == True:
                result.append([i])            

        return result