class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        # sort by biggest attack, then lowest defense
        properties.sort(key=lambda x: (-x[0], x[1]))
        count = 0
        max_def = 0  # defense > 0
        for _, defense in properties:
            if defense < max_def:  # => lower attack, and lower defense
                count +=  1
            else:
                max_def = defense  # update maximum defense
        return count
