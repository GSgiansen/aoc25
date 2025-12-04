def comput():
    with open ('input.txt', 'r') as file:
        lines = file.readlines()

    point = 50

    ans = 0
    for line in lines:
        print(f"\npoint is {point}")
        num = int(line[1:])
        cycles = num // 100
        rotate = num - (num // 100 * 100)
        prev_point = point
        flag = False
        ans += cycles
        if line[0] == "L":
            point -= rotate
            if prev_point != 0 and point < 0:
                print(f"rotated left past 0 to {point}")
                ans += 1
                flag = True
            point = point % 100
            
            
        else:
            point += rotate
            if point > 99:
                print(f"rotated right past 0 to {point}")
                ans += 1
                flag = True
            point = point % 100
            
        
        if point == 0 and not flag:
            print(f"landed on 0")
            ans += 1
    print(ans)
if __name__ == "__main__":
    comput()