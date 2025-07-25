from typing import List
#main logic
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for row_num in range(numRows):
            row = [1] * (row_num + 1)
            for j in range(1, row_num):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
            triangle.append(row)
        return triangle
    
# Example usage:
#input logic
numRows = int(input("Enter the number of rows: "))
sol = Solution()
#output logic
result = sol.generate(numRows)
print("Pascal's Triangle:")
for row in result:
    print(row)