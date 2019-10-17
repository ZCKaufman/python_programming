import unittest

class MyMatrix:
    matrix = [[int]]
    listNum = 0
    listSize = 0
    def spiralOrder(self, matrix: [[int]]) -> [[int]]:
        finalList = []
        listNum = len(matrix) - 1
        listSize = len(matrix[0]) - 1

        for i in range(0, len(matrix[0]) - 1, 1):
            finalList.append(matrix[0][i])
        for i in range(0, len(matrix), 1):
            finalList.append(matrix[i][listSize])

        print(finalList)

    #def horizontalCount(start: int, end: int, )

# Testing
obj = MyMatrix()
class TestReverseWords(unittest.TestCase):

    def test_MyString(self):
        self.assertEqual(obj.spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]), [1,2,3,6,9,8,7,4,5])
        self.assertEqual(obj.spiralOrder([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]), [1,2,3,4,8,12,11,10,9,5,6,7])

if __name__ == '__main__':
    unittest.main()
