from collections import Counter
import heapq
    
def comput():
    with open ('input.txt', 'r') as file:
        l = file.read().splitlines()
    lines = [list(line) for line in l]
    
    m = len(lines)
    n = len(lines[0])
    directions = [-1, 0, 1]
    def check_adj(i, j):
        if i < 0 or i >= m or j < 0 or j >= n:
            return 0
        count = 0
        for x in directions:
            for y in directions:
                if x == y and x == 0:
                    continue
                newi, newj = x + i, y + j
                if newi < 0 or newi >= m or newj < 0 or newj >= n:
                    continue
                if lines[newi][newj] == "@":
                    count += 1
        return count
    main_ans = 0
    # print(lines)
    while True:
        ans = 0
        visited = set()
        for i in range(m):
            for j in range(n):
                check = check_adj(i, j)
                
                if check < 4 and lines[i][j] == "@":
                    # print(visited)
                    visited.add((i, j))
                    ans += 1
        for tup in visited:
            lines[tup[0]][tup[1]] = "."
        # print(lines)

        main_ans += ans
        if ans == 0 or not visited:
            break
    print(f"ans is {main_ans}")
                
if __name__ == "__main__":
    comput()