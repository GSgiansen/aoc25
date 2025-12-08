from collections import defaultdict, Counter
from sortedcontainers import SortedList
import heapq

def calc_euc(pt1, pt2):
    return (abs(pt1[0] - pt2[0])** 2 + abs(pt1[1] - pt2[1])** 2+ abs(pt1[2] - pt2[2])** 2)
def compute():
    filepath = "input.txt"
    points = []
    with open(filepath) as f:
        lines = f.read().splitlines()
        for line in lines:
            line = line.split(",")
            points.append((int(line[0]), int(line[1]), int(line[2])))
    n = len(points)
    dsu = DSU(n)
    counter = 0
    d = set()
    a = SortedList()
    for i in range(len(points)):
        if points[i] == -1:
            continue
        for j in range(len(points)):
            if i == j:
                continue
            if (i, j) in d or (j, i) in d:
                continue
            a.add((calc_euc(points[i], points[j]), i, j))
            d.add((i, j))
    connections = 0
    for dist, i, j in a:
        connections += 1
        dsu.union(i, j)
        comp_sizes = Counter(dsu.find(i) for i in range(n))
        if len(comp_sizes) == 1:
            print(f"final ans is {points[i][0]* points[j][0]}")
            return
    ans = 1
    comp_sizes = Counter(dsu.find(i) for i in range(n))
    
    arr = heapq.nlargest(3,  comp_sizes.values())
    print(comp_sizes)
    # print(parents)
    print(ans * arr[0] * arr[1] * arr[2])
    
    return     
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        # path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False  # no merge
        # union by size
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True   
if __name__ == "__main__":
    
    compute()
    
