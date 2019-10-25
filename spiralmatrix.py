import unittest

class MyMatrix:
    matrix = [[int]]
    listNum = 0
    listSize = 0
    def spiralOrder(self, matrix: [[int]]) -> [[int]]:
        finalList = []
        listSize = len(matrix[0]) - 1
        listNum = len(matrix) - 1

        i = 0
        while(i <= listSize):
            #print("!!!", i, "!!!")
            #print(matrix)
            j = 0
            listNum = len(matrix) - 1
#            print("BEGIN:", matrix)
            if(len(matrix) != 0):
#                print("IF")
                # First row
                for k in range(len(matrix[0])):
                    finalList.append(matrix[0][k])
                matrix.remove(matrix[0])
#                print("FIRST", "Matrix:", matrix, "finalList:", finalList, "listNum:", listNum)
                # Last column
#                print(matrix)
                if(len(matrix) != 0):
                    listSize = len(matrix[0]) - 1
                    j = 0
                    while(j < listNum):
#                        print(matrix, j, listSize)
                        finalList.append(matrix[j][listSize])
                        matrix[j].remove(matrix[j][listSize])
                        j += 1
#                print("SECOND", "Matrix:", matrix, "finalList:", finalList, "listNum:", listNum)
                # Bottom row
                if(len(matrix) != 0):
                    listNum = len(matrix) - 1
                    listSize = len(matrix[listNum]) - 1
                    j = listSize
                    while(j >= 0):
#                        print(matrix, listNum, j)
                        finalList.append(matrix[listNum][j])
                        matrix[listNum].remove(matrix[listNum][j])
                        j -= 1
                    matrix.remove(matrix[listNum])
#                print("THIRD", "Matrix:", matrix, "finalList:", finalList, "listNum:", listNum)
                # First column
                j = 0
                i = listNum - 1
                listNum -= 1
                if(len(matrix) != 0):
                    while(i >= 0 and matrix):
                        finalList.append(matrix[i][0])
                        matrix[i].remove(matrix[i][0])
                        i -= 1
                    #matrix.remove(matrix[listNum][0])
#                print("FOURTH", "Matrix:", matrix, "finalList:", finalList, "listNum:", listNum)
                print(matrix, finalList)
            else:
                print("----------ELSE-----------\n",finalList,"\n|||||||||||||||||||||")
                return finalList

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
        self.assertEqual(obj.spiralOrder([
[1, 2, 3, 4, 5],
[6, 7, 8, 9, 10],
[11, 12, 13, 14, 15],
[16, 17, 18, 19, 20]
]), [1,2,3,4,5,10,15,20,19,18,17,16,11,6,7,8,9,14,13,12])

if __name__ == '__main__':
    unittest.main()
