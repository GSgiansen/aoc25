from collections import deque
import re


def solve_machine(pattern, options):
    n = len(pattern)

    target = 0
    for i, c in enumerate(pattern):
        if c == '#':
            target |= 1 << i

    # Convert each button to a bitmask
    masks = []
    for opt in options:
        mask = 0
        for a in opt:
            if not a:
                continue
            idx = int(a)
            mask |= 1 << idx
        masks.append(mask)

    start = 0
    if start == target:
        return 0
    q = deque([(start, 0)])
    seen = {start}

    while q:
        state, presses = q.popleft()
        if state == target:
            return presses

        for m in masks:
            ns = state ^ m
            if ns not in seen:
                seen.add(ns)
                q.append((ns, presses + 1))

    # If somehow unreachable
    return float("inf")


def parse_line(line):
    matches = re.findall(r'\[([.#]+)\]|\(([\d,]+)\)|\{([0-9, ]+)\}', line)

    pattern = None
    options = []

    for g1, g2, g3 in matches:
        if g1:  # the [pattern]
            pattern = g1
        elif g2:  # a (button)
            opts = g2.split(',')
            options.append(opts)
        # g3 is joltage, ignore

    return pattern, options


def compute():
    filepath = "input.txt"

    machines = []

    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            pattern, options = parse_line(line)
            machines.append((pattern, options))

    total = 0
    for pattern, options in machines:
        ans = solve_machine(pattern, options)
        print(f"min operations {ans} for {pattern}")
        total += ans

    print(f"final s is {total}")


if __name__ == "__main__":
    compute()
