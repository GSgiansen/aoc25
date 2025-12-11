from collections import defaultdict, Counter
import heapq

def compute():
    filepath = "input.txt"
    points = []
    with open(filepath) as f:
        lines = f.read().splitlines()
        for line in lines:
            line = line.split(",")
            points.append((int(line[0]), int(line[1])))
    # print(points)
    ### want the top right most point and the bottom left most point
    max_area = 0
    for i in range(len(points)):
        for j in range(len(points)):
            if i == j:
                continue
            print(f"{points[i], points[j]}")
            max_area = max(max_area, abs(points[i][0] - points[j][0] + 1) * abs(points[i][1] - points[j][1] + 1))
    print(f"ans is {max_area}")
    return      
if __name__ == "__main__":
    
    compute()
    
