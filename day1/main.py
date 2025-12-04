def comput():
    with open ('input.txt', 'r') as file:
        lines = file.readlines()

    point = 50

    ans = 0
    for line in lines:
        print(f"point is {point}")
        num = int(line[1:])
        rotate = num - (num // 100 * 100)
        if line[0] == "L":
            point -= rotate
            point = point % 100
            
        else:
            point += rotate
            point = point % 100
        
        if point == 0:
            ans += 1
    print(ans)
if __name__ == "__main__":
    comput()