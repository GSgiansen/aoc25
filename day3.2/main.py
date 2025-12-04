from collections import Counter
import heapq
def comput():
    with open ('input.txt', 'r') as file:
        lines = file.read().splitlines()
    print(lines)
    ### take the top 12 most important elements while preserving their order
    ans = 0
    # def dfs(index, s, n, line, count):
    #     if index == n or count == 12:
    #         return s
    #     ### we either dont take or take 2 choices
    #     choice_one = dfs(index + 1, s* 10 + int(line[index]), n, line, count + 1)
    #     choice_two = dfs(index + 1, s, n, line, count)
    #     # print(f"1, 2 is {choice_one, choice_two}")
        
    #     return max(choice_one, choice_two)

    def lawl(line):
        ### dp[i] = max(dp[i + 1] * 10 + line[index ], dp[i])
        ### dp[i][count] = max(dp[i + 1][count] * 10 + line[index ], dp[i])
        n = len(line)
        # dp = [[0 for i in range(n)] for _ in range(12)]
        dp = [[-1 for _ in range(12 + 1)] for i in range(n + 1)]
        dp[0][0] = 0
        for i in range(n):
            digit = int(line[i])
            for c in range(13):
                if dp[i][c] == -1:
                    continue
                dp[i+1][c] = max(dp[i + 1][c], dp[i][c])
                if c < 12:
                    dp[i+1][c+1] = max(dp[i+1][c+1] , dp[i][c] * 10 + digit)
        return max(dp[n])
    for line in lines:
        ### smnaller numbers need as right index as possible
        ## greedy is not possibnlle we can do dfs with min
        min_ans = lawl(line)
        print(f"min is {min_ans}")
        ans += min_ans
    print(ans)
        
                
if __name__ == "__main__":
    comput()