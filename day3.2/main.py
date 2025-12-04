from collections import Counter
import heapq
def comput():
    with open ('input_small.txt', 'r') as file:
        lines = file.read().splitlines()
    print(lines)
    ### take the top 12 most important elements while preserving their order
    ans = 0
    for line in lines:
        lst_pairs = sorted([(line[i], i) for i in range(len(line))])
        min_ans = lst_pairs[:12]
        min_ans = sorted(lambda x: x[1], min_ans)
        line_ans = 0
        for value, index in min_ans:
            line_ans = line_ans * 10 + value
        ans += line_ans
    

        
        
    print(ans)
        
                
if __name__ == "__main__":
    comput()