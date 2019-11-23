class Graph():
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            for j in range(size):
                self.adjMatrix[i].append(0)

    def toString(self):
        for i in self.adjMatrix:
            for j in i:
                print(j)

'''class Graph(object):
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size '''
    #print(self.adjMatrix)
if __name__ == "__main__":
    obj = Graph(5)
    obj.toString()
