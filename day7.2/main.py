from collections import defaultdict
def compute():
    filepath = "input.txt"
    with open(filepath) as f:
        grid = f.read().splitlines()

    m, n = len(grid), len(grid[0])

    for r in range(m):
        if "S" in grid[r]:
            start_row = r
            start_col = grid[r].index("S")
            break

    active = {start_col:1}
    ans = 1
    for r in range(start_row + 1, m):
        row = grid[r]
        new_active = defaultdict(int)

        for c in active:
            if not (0 <= c < n):
                continue
            num_timelines = active[c]
            if row[c] == "^":
                ans += num_timelines
                if c - 1 >= 0:
                    new_active[(c - 1)] += num_timelines
                if c + 1 < n:
                    new_active[(c + 1)] += num_timelines
            else:

                new_active[(c)] += num_timelines
        active = new_active
    print("ans is", ans)

    

    return             
if __name__ == "__main__":
    
    compute()