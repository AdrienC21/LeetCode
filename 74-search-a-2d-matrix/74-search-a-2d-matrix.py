class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if (target < matrix[0][0]) or (target > matrix[-1][-1]):
            return False
        left = 0
        right = len(matrix) - 1
        while left < right:
            mid = (left + right) // 2
            if (target >= matrix[mid][0]) and (target <= matrix[mid][-1]):
                left = mid
                break
            elif matrix[mid][0] > target:
                if target <= matrix[mid-1][-1]:
                    right = mid - 1
                else:
                    return False
            else:
                if target >= matrix[mid+1][0]:
                    left = mid + 1
                else:
                    return False
        row = matrix[left]
        if (target < row[0]) or (target > row[-1]):
            return False
        left = 0
        right = len(row) - 1
        while left < right:
            mid = (left + right) // 2
            if row[mid] == target:
                return True
            elif row[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return (row[left] == target)