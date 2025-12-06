from rangetree import RangeTree
def comput():
    filepath = 'input.txt'
    ranges = []
    ingredients = []
    with open(filepath, 'r') as f:
        flag = False
        for line in f:
            if line.strip() == "":  # Check if the line is empty after stripping whitespace
                flag = True
            elif flag:
                ingredients.append(line.rstrip('\n'))
            else:
                ranges.append(line.rstrip('\n')) # Remove only trailing newline characters
    ranges = [[int(x.split("-")[0]), int(x.split("-")[1])] for x in ranges]
    ingredients = [int(x) for x in ingredients]
    # s = set()
    ranges.sort()
    new_ranges = []
    for s, e in ranges:
        if not new_ranges or s > new_ranges[-1][-1]:
            new_ranges.append([s, e])
        else:
            new_ranges[-1][-1] = max(e, new_ranges[-1][-1])
    # print(f"new_ranges {new_ranges}")
    r = RangeTree()
    for i in range(len(new_ranges)):
        start, end = new_ranges[i]
        r[start:end+1] = i
    ans = 0
    for ingredient in ingredients:
        if r.get(ingredient, -1) != -1:
            ans += 1
    print(f"ans is {ans}")
            
if __name__ == "__main__":
    
    comput()