from collections import deque

def print_nice(matrix):
    for row in matrix:
        print("".join(row))
    print()

def compute():
    filepath = "input.txt"  # or "input.txt"
    points = []
    with open(filepath) as f:
        lines = f.read().splitlines()
        for line in lines:
            if not line.strip():
                continue
            x_str, y_str = line.split(",")
            points.append((int(x_str), int(y_str)))

    # Safety: if no points, nothing to do
    if not points:
        print("No points")
        return

    # Build grid big enough for all coordinates + margin
    max_x = max(x for x, _ in points)
    max_y = max(y for _, y in points)
    # Add a border of 2 around just to be safe for flood-fill
    W = max_x + 3
    H = max_y + 3

    grid = [["." for _ in range(W)] for _ in range(H)]

    # Mark red tiles
    for x, y in points:
        grid[y][x] = "#"

    # Draw green edges between consecutive red tiles (wrap around)
    def draw_segment(x1, y1, x2, y2):
        if x1 == x2:
            # Vertical
            step = 1 if y2 >= y1 else -1
            for yy in range(y1, y2 + step, step):
                if grid[yy][x1] != "#":  # keep red as '#'
                    grid[yy][x1] = "X"
        elif y1 == y2:
            # Horizontal
            step = 1 if x2 >= x1 else -1
            for xx in range(x1, x2 + step, step):
                if grid[y1][xx] != "#":
                    grid[y1][xx] = "X"
        else:
            # Puzzle guarantees axis-aligned segments
            raise ValueError("Non axis-aligned segment between points!")

    n = len(points)
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        draw_segment(x1, y1, x2, y2)

    # Flood-fill from outside to find all '.' reachable from the border (outside region)
    visited = [[False] * W for _ in range(H)]
    q = deque()

    # Enqueue all border cells that are '.'
    for x in range(W):
        for y in (0, H - 1):
            if grid[y][x] == "." and not visited[y][x]:
                visited[y][x] = True
                q.append((x, y))
    for y in range(H):
        for x in (0, W - 1):
            if grid[y][x] == "." and not visited[y][x]:
                visited[y][x] = True
                q.append((x, y))

    # BFS
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while q:
        x, y = q.popleft()
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < W and 0 <= ny < H:
                if not visited[ny][nx] and grid[ny][nx] == ".":
                    visited[ny][nx] = True
                    q.append((nx, ny))

    # Any '.' that is NOT visited is inside the polygon → green
    for y in range(H):
        for x in range(W):
            if grid[y][x] == "." and not visited[y][x]:
                grid[y][x] = "X"

    # Optional: see the reconstructed red/green grid
    # print_nice(grid)

    # Now brute-force all pairs of red corners for part 2
    reds = points[:]  # list of (x, y)
    max_area = 0

    for i in range(len(reds)):
        x1, y1 = reds[i]
        for j in range(i + 1, len(reds)):
            x2, y2 = reds[j]
            # Must be opposite corners of a non-degenerate rectangle
            if x1 == x2 or y1 == y2:
                continue

            minx, maxx = sorted((x1, x2))
            miny, maxy = sorted((y1, y2))

            # Check that every cell in the rectangle is red or green
            ok = True
            for yy in range(miny, maxy + 1):
                row = grid[yy]
                for xx in range(minx, maxx + 1):
                    if row[xx] == ".":  # outside (neither red nor green)
                        ok = False
                        break
                if not ok:
                    break

            if ok:
                area = (maxx - minx + 1) * (maxy - miny + 1)
                if area > max_area:
                    max_area = area

    print(f"max_AREA IS {max_area}")


if __name__ == "__main__":
    compute()
