def compute():
    filepath = "input_small.txt"
    with open(filepath) as f:
        grid = f.read().splitlines()

    m, n = len(grid), len(grid[0])

    for r in range(m):
        if "S" in grid[r]:
            start_row = r
            start_col = grid[r].index("S")
            break

    active = {start_col}
    ans = 0
    for r in range(start_row + 1, m):
        row = grid[r]
        new_active = set()

        for c in active:
            if not (0 <= c < n):
                continue

            if row[c] == "^":
                ans += 1
                if c - 1 >= 0:
                    new_active.add(c - 1)
                if c + 1 < n:
                    new_active.add(c + 1)
            else:

                new_active.add(c)

        active = new_active

    print("ans is", ans)


    return             
if __name__ == "__main__":
    
    compute()