class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Input: strs = ["act","pots","tops","cat","stop","hat"]

        {{a:1}}

        Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
        """
        strs_table = {}

        for string in strs:
            sorted_string = ''.join(sorted(string))
            print(sorted_string)
            if sorted_string not in strs_table:
                strs_table[sorted_string] = []

            strs_table[sorted_string].append(string)

        return list(strs_table.values())