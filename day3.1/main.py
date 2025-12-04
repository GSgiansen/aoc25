from collections import Counter
import heapq
def comput():
    with open ('input.txt', 'r') as file:
        lines = file.read().splitlines()
    print(lines)
    ans = 0
    for line in lines:
        max_char_so_far = 0
        max_num_so_far = 0
        for c in line:
            c = int(c)
            max_num_so_far = max(max_char_so_far * 10 + c, max_num_so_far)
            max_char_so_far = max(c, max_char_so_far)
        # print(f"ans is {max_num_so_far}")
        ans += max_num_so_far 
    print(ans)
        
                
if __name__ == "__main__":
    comput()