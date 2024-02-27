class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        lis = []
        while i < j:
            front = height[i]
            back = height[j]
            height2 = min(front, back)
            value = (j - i) * height2
            lis.append(value)

            if front < back:
                i += 1
                while i<j and height[i] > front:
                    front = height[i]
                    back = height[j]
                    height2 = min(front, back)
                    value = (j - i) * height2
                    lis.append(value)     
            else:
                j -= 1
                while i<j and height[j] > back:
                    front = height[i]
                    back = height[j]
                    height2 = min(front, back)
                    value = (j - i) * height2
                    lis.append(value)
        return max(lis)

s = Solution()
print(s.maxArea([2,3,4,5,18,17,6]))




