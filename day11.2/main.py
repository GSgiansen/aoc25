from collections import defaultdict
from functools import lru_cache

def compute():
    filepath = "input.txt"
    adjlst = defaultdict(list)
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            node, neighbours = line.split(":")
            node = node.strip()
            for nxt in neighbours.split():
                if nxt:
                    adjlst[node].append(nxt)

    @lru_cache(maxsize=None)
    def count_paths(node: str, seen_dac: bool, seen_fft: bool) -> int:
        if node == "dac":
            seen_dac = True
        if node == "fft":
            seen_fft = True

        if node == "out":
            return 1 if (seen_dac and seen_fft) else 0

        total = 0
        for nxt in adjlst[node]:
            total += count_paths(nxt, seen_dac, seen_fft)
        return total

    ans = count_paths("svr", False, False)
    print(f"answer is {ans}")
    return ans


if __name__ == "__main__":
    compute()
