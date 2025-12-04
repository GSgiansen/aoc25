def comput():
    with open ('input.txt', 'r') as file:
        lines = file.read()
    lines = lines.split(",")
    ans = 0
    st = set()
    for line in lines:
        nums = line.split("-")
        print(nums)
        if nums[0][0] == "0" or nums[1][0] == "0":
            # print(f"skipped")
            continue
        ### at each number we split up to n//2 distance and check if its possible
        nums[0], nums[1] = int(nums[0]), int(nums[1])
        for num in range(nums[0], nums[1] + 1):
            s = str(num)
            if len(s) % 2 == 1:
                continue
            split = s[:len(s) // 2]
            if split == s[len(s) // 2:]:
                # print(s)
                print(num)
                st.add(num)
                # ans += num
    print(sum(st))
    return sum(st)
                
if __name__ == "__main__":
    comput()